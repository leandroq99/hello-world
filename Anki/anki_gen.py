#!/usr/bin/env python3
"""
anki_gen.py — Gerador de flashcards para Anki (AllInOne add-on)
Suporta entrada: PDF ou Markdown/TXT
Saída: CSV compatível com o note type "AllInOne (kprim, mc, sc)"

Uso:
    python anki_gen.py material.pdf --deck "Git e GitHub" --tags "gh900 devops"
    python anki_gen.py anotacoes.md --deck "Python" --tags "python fundamentos"
    python anki_gen.py material.pdf --num-cards 20 --qtype 2
"""

import argparse
import csv
import json
import os
import re
import sys
import textwrap
from pathlib import Path

# ── Dependências opcionais instaladas em runtime ───────────────────────────────
def ensure_deps():
    import importlib, subprocess
    pkgs = {"pymupdf": "pymupdf", "anthropic": "anthropic"}
    for mod, pkg in pkgs.items():
        if importlib.util.find_spec(mod) is None:
            print(f"[setup] Instalando {pkg}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q"])

ensure_deps()

import fitz          # PyMuPDF
import anthropic


# ── Constantes ─────────────────────────────────────────────────────────────────
QTYPE_LABELS = {0: "Kprim", 1: "Multiple Choice", 2: "Single Choice"}

# Cabeçalho exato do note type AllInOne (kprim, mc, sc)
CSV_HEADER = ["Text", "Q_1", "Q_2", "Q_3", "Q_4", "Q_5", "Answers", "QType", "Tags"]

SYSTEM_PROMPT = """\
Você é um especialista em criar flashcards de alta qualidade para o Anki usando o add-on AllInOne (kprim, mc, sc).

Dado um conteúdo de estudo, você deve gerar flashcards no formato JSON descrito abaixo.

REGRAS PARA BONS FLASHCARDS:
- Cada card testa UMA ideia específica — não tente cobrir múltiplos conceitos em um card.
- O campo "text" é a pergunta ou enunciado do card.
- Os campos "q1" a "q5" são as alternativas (use no mínimo 3, máximo 5).
- O campo "answers" indica quais alternativas são corretas: "1" = correta, "0" = incorreta, separados por espaço.
  Exemplo com 4 alternativas, sendo a 2ª correta: "0 1 0 0"
- O campo "qtype" indica o tipo:
    0 = Kprim (múltiplas podem ser corretas ou incorretas — todas devem ser julgadas)
    1 = Multiple Choice (uma ou mais corretas entre as opções)
    2 = Single Choice (exatamente uma correta — mais comum para certificações)
- Prefira qtype=2 (Single Choice) para conteúdos de certificação/prova.
- Alternativas incorretas (distractors) devem ser plausíveis, não obviamente erradas.
- Evite alternativas como "Todas as anteriores" ou "Nenhuma das anteriores".
- Escreva no mesmo idioma do material recebido.

FORMATO DE SAÍDA — responda SOMENTE com JSON válido, sem markdown, sem texto extra:
{
  "cards": [
    {
      "text": "Enunciado da pergunta",
      "q1": "Alternativa A",
      "q2": "Alternativa B",
      "q3": "Alternativa C",
      "q4": "Alternativa D",
      "q5": "",
      "answers": "1 0 0 0",
      "qtype": 2
    }
  ]
}

Se uma alternativa não for necessária, deixe o campo como string vazia "".
O número de valores em "answers" deve ser igual ao número de alternativas não-vazias.
"""


# ── Extração de texto ──────────────────────────────────────────────────────────
def extract_text_from_pdf(path: Path) -> str:
    doc = fitz.open(str(path))
    pages = []
    for page in doc:
        pages.append(page.get_text())
    doc.close()
    text = "\n\n".join(pages)
    # Limpa espaços excessivos mantendo parágrafos
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def extract_text_from_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def extract_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        print(f"[info] Extraindo texto do PDF: {path.name}")
        return extract_text_from_pdf(path)
    elif suffix in (".md", ".txt", ".markdown"):
        print(f"[info] Lendo arquivo de texto: {path.name}")
        return extract_text_from_markdown(path)
    else:
        # Tenta ler como texto mesmo assim
        try:
            return path.read_text(encoding="utf-8").strip()
        except Exception:
            raise ValueError(f"Formato não suportado: {suffix}. Use PDF, MD ou TXT.")


# ── Chamada à Claude API ───────────────────────────────────────────────────────
def generate_cards(content: str, num_cards: int, qtype: int, api_key: str) -> list[dict]:
    client = anthropic.Anthropic(api_key=api_key)

    # Trunca conteúdo muito longo para não estourar o contexto
    max_chars = 60_000
    if len(content) > max_chars:
        print(f"[aviso] Conteúdo truncado para {max_chars} caracteres.")
        content = content[:max_chars] + "\n\n[... conteúdo truncado ...]"

    user_prompt = textwrap.dedent(f"""
        Analise o conteúdo abaixo e gere exatamente {num_cards} flashcards.
        Tipo de questão preferencial: {QTYPE_LABELS[qtype]} (qtype={qtype})
        
        Cubra os conceitos mais importantes do material, priorizando:
        1. Definições e conceitos-chave
        2. Diferenças entre termos similares
        3. Casos de uso e quando aplicar cada conceito
        4. Fatos que costumam cair em provas/certificações

        CONTEÚDO:
        ───────────────────────────────────
        {content}
        ───────────────────────────────────
        
        Gere os {num_cards} flashcards agora em JSON.
    """).strip()

    print(f"[api] Gerando {num_cards} flashcards com Claude...")
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}]
    )

    raw = response.content[0].text.strip()

    # Remove markdown code block se presente
    raw = re.sub(r'^```(?:json)?\s*', '', raw)
    raw = re.sub(r'\s*```$', '', raw)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"[erro] Resposta da API não é JSON válido:\n{raw[:500]}")
        raise RuntimeError(f"Falha ao parsear JSON da API: {e}")

    return data.get("cards", [])


# ── Geração do CSV ─────────────────────────────────────────────────────────────
def cards_to_csv(cards: list[dict], output_path: Path, tags: str, deck: str):
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        # Cabeçalho especial que o Anki usa para identificar deck e note type
        f.write(f"#separator:Comma\n")
        f.write(f"#html:false\n")
        f.write(f"#notetype:AllInOne (kprim, mc, sc)\n")
        if deck:
            f.write(f"#deck:{deck}\n")
        f.write(f"#columns:{','.join(CSV_HEADER)}\n")

        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for card in cards:
            q1 = card.get("q1", "")
            q2 = card.get("q2", "")
            q3 = card.get("q3", "")
            q4 = card.get("q4", "")
            q5 = card.get("q5", "")
            answers = card.get("answers", "")
            qtype = card.get("qtype", 2)

            # Valida número de answers vs alternativas não-vazias
            opts = [o for o in [q1, q2, q3, q4, q5] if o.strip()]
            ans_values = answers.strip().split()
            if len(ans_values) != len(opts):
                print(f"[aviso] Card '{card.get('text','')[:40]}...' tem {len(opts)} alternativas mas {len(ans_values)} respostas. Ajustando.")
                # Tenta corrigir: assume primeiro como correto se divergir muito
                if len(ans_values) > len(opts):
                    ans_values = ans_values[:len(opts)]
                else:
                    ans_values += ["0"] * (len(opts) - len(ans_values))
                answers = " ".join(ans_values)

            row = [
                card.get("text", ""),
                q1, q2, q3, q4, q5,
                answers,
                str(qtype),
                tags
            ]
            writer.writerow(row)

    print(f"[ok] {len(cards)} cards salvos em: {output_path}")


# ── CLI ────────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Gera flashcards Anki (AllInOne) a partir de PDF ou Markdown usando Claude API."
    )
    parser.add_argument("input", type=Path, help="Arquivo de entrada (.pdf, .md ou .txt)")
    parser.add_argument("--deck", default="Meu Deck", help="Nome do deck no Anki (padrão: 'Meu Deck')")
    parser.add_argument("--tags", default="", help="Tags separadas por espaço (ex: 'git github gh900')")
    parser.add_argument("--num-cards", type=int, default=15, help="Número de cards a gerar (padrão: 15)")
    parser.add_argument("--qtype", type=int, choices=[0, 1, 2], default=2,
                        help="Tipo de questão: 0=Kprim, 1=MultipleChoice, 2=SingleChoice (padrão: 2)")
    parser.add_argument("--output", type=Path, default=None,
                        help="Arquivo de saída .csv (padrão: mesmo nome do input com sufixo _anki.csv)")
    parser.add_argument("--api-key", default=None,
                        help="Chave da API Anthropic (ou defina a variável ANTHROPIC_API_KEY)")
    args = parser.parse_args()

    # Valida input
    if not args.input.exists():
        print(f"[erro] Arquivo não encontrado: {args.input}")
        sys.exit(1)

    # API Key
    api_key = args.api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("[erro] Defina a variável de ambiente ANTHROPIC_API_KEY ou use --api-key.")
        sys.exit(1)

    # Output path
    output = args.output or args.input.parent / (args.input.stem + "_anki.csv")

    # Pipeline
    content = extract_text(args.input)
    print(f"[info] Conteúdo extraído: {len(content):,} caracteres")

    cards = generate_cards(content, args.num_cards, args.qtype, api_key)
    print(f"[info] {len(cards)} cards gerados pela API")

    cards_to_csv(cards, output, args.tags, args.deck)

    print()
    print("─" * 50)
    print("PRÓXIMOS PASSOS:")
    print("  1. Abra o Anki Desktop")
    print("  2. File → Import")
    print(f"  3. Selecione: {output.name}")
    print("  4. Confirme: Note type = 'AllInOne (kprim, mc, sc)'")
    print("  5. Clique em Import — pronto!")
    print("─" * 50)


if __name__ == "__main__":
    main()
