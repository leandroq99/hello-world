# 📚 anki_gen — Gerador de Flashcards para Anki

Gera flashcards automaticamente a partir de PDFs ou Markdown, compatíveis com o add-on **AllInOne (kprim, mc, sc)** do Anki.

## Pré-requisitos

- Python 3.9+
- Anki Desktop instalado: https://apps.ankiweb.net
- Add-on AllInOne instalado no Anki (código: `1566095810`)
- Chave de API da Anthropic: https://console.anthropic.com

## Instalação

```bash
# Clone ou baixe os arquivos
# Instale as dependências (o script faz isso automaticamente, mas você pode instalar antes):
pip install anthropic pymupdf
```

## Configuração da API Key

```bash
# Linux / macOS
export ANTHROPIC_API_KEY="sk-ant-..."

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY = "sk-ant-..."

# Ou passe direto no comando com --api-key
```

## Uso

```bash
# Básico — gera 15 cards de um PDF
python anki_gen.py material.pdf --deck "Git e GitHub" --tags "gh900"

# Mais cards, com tags múltiplas
python anki_gen.py anotacoes.md --deck "Python" --tags "python fundamentos" --num-cards 25

# Escolher tipo de questão (0=Kprim, 1=MultipleChoice, 2=SingleChoice)
python anki_gen.py material.pdf --deck "AWS" --qtype 1 --num-cards 20

# Especificar arquivo de saída
python anki_gen.py slides.md --deck "Docker" --output docker_cards.csv
```

## Tipos de Questão

| QType | Nome | Descrição |
|-------|------|-----------|
| `0` | Kprim | 4 afirmações, cada uma é V ou F independentemente |
| `1` | Multiple Choice | Uma ou mais alternativas corretas |
| `2` | Single Choice | Exatamente uma correta (ideal para certificações) |

## Importando no Anki

1. Abra o **Anki Desktop**
2. **File → Import**
3. Selecione o arquivo `_anki.csv` gerado
4. Confirme que o **Note type** está como `AllInOne (kprim, mc, sc)`
5. Clique em **Import**

> O arquivo CSV já inclui cabeçalhos especiais (`#notetype`, `#deck`) que o Anki 2.1.54+ lê automaticamente — você não precisa selecionar o deck manualmente.

## Estrutura do CSV gerado

```
#separator:Comma
#html:false
#notetype:AllInOne (kprim, mc, sc)
#deck:Git e GitHub
#columns:Text,Q_1,Q_2,Q_3,Q_4,Q_5,Answers,QType,Tags

"O que é HEAD no Git?","Ponteiro para o commit mais recente do branch ativo","O primeiro commit do repositório","O branch remoto principal","O índice da staging area","","1 0 0 0","2","gh900"
```

## Campos do AllInOne

| Campo | Descrição |
|-------|-----------|
| `Text` | Enunciado / pergunta |
| `Q_1` a `Q_5` | Alternativas (deixe vazio se não usar) |
| `Answers` | `1`=correta, `0`=incorreta, separados por espaço |
| `QType` | `0`, `1` ou `2` |
| `Tags` | Tags separadas por espaço |
