# 📚 Guia do Anki - Gerador de Flashcards

Automatize a criação de flashcards a partir de PDFs e Markdown para otimizar seu aprendizado.

## 📖 O que é Anki?

Anki é um software de **repetição espaçada** que ajuda a memorizar informações através de flashcards. Com este projeto, você pode gerar automaticamente flashcards a partir de documentos.

## 🎯 O que é anki_gen?

**anki_gen** é um gerador automático de flashcards compatível com o add-on **AllInOne** do Anki, que suporta:

- 📋 Questões de Múltipla Escolha (MC)
- ✔️ Questões de Única Resposta (SC)
- ❌ Questões Kprim (K-Prim)

## ⚙️ Pré-requisitos

- **Python 3.9+** instalado
- **Anki Desktop** — [Baixar aqui](https://apps.ankiweb.net)
- **Add-on AllInOne** — Código: `1566095810`
- **API Key da Anthropic** — [Criar aqui](https://console.anthropic.com)

## 📦 Instalação

### Passo 1: Clonar/Baixar o Repositório

```bash
git clone <repo-url>
cd Anki
```

### Passo 2: Instalar Dependências

```bash
pip install anthropic pymupdf
```

Ou deixe que o script instale automaticamente na primeira execução.

## 🔐 Configurar API Key

### Linux / macOS

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

### Windows (PowerShell)

```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-..."
```

### Windows (CMD)

```cmd
set ANTHROPIC_API_KEY=sk-ant-...
```

### Alternativa: Passar na Linha de Comando

```bash
python anki_gen.py --api-key "sk-ant-..." input.pdf
```

## 🚀 Como Usar

### Sintaxe Básica

```bash
python anki_gen.py <arquivo-entrada> [opções]
```

### Exemplos

#### 1. Gerar a partir de PDF

```bash
python anki_gen.py documento.pdf
```

#### 2. Gerar a partir de Markdown

```bash
python anki_gen.py notas.md
```

#### 3. Especificar arquivo de saída

```bash
python anki_gen.py documento.pdf --output meus_flashcards.txt
```

#### 4. Definir número de questões

```bash
python anki_gen.py documento.pdf --count 20
```

## 📤 Importar para Anki

### Passo 1: Gerar o Arquivo

```bash
python anki_gen.py seu_documento.pdf
```

Isso criará um arquivo de saída (padrão: `output.txt`).

### Passo 2: Abrir Anki

Abra o Anki Desktop e selecione ou crie um baralho (deck).

### Passo 3: Importar

1. Clique em **"Arquivo"** → **"Importar"**
2. Selecione o arquivo de saída (`.txt` ou `.apkg`)
3. Clique em **"Importar"**
4. Configure as opções conforme necessário

### Passo 4: Estudar

Comece a estudar! O Anki usará repetição espaçada para otimizar sua memorização.

## 📋 Formatos de Entrada Suportados

| Formato | Extensão | Descrição |
|---------|----------|-----------|
| PDF | `.pdf` | Documentos em PDF |
| Markdown | `.md` | Notas em formato Markdown |
| Texto Puro | `.txt` | Arquivos de texto simples |

## 📊 Tipos de Questões Geradas

### 1. **Multiple Choice (MC)**
```
Pergunta?
a) Opção 1
b) Opção 2
c) Opção 3
d) Opção 4

Resposta: c)
```

### 2. **Single Choice (SC)**
```
Pergunta?
- Opção correta
- Opção errada 1
- Opção errada 2

Resposta: Opção correta
```

### 3. **Kprim (K-Prim)**
```
Qual é verdadeiro?
✓ Afirmação 1
✗ Afirmação 2
✓ Afirmação 3
✗ Afirmação 4
```

## 🛠️ Opções Avançadas

| Opção | Descrição |
|-------|-----------|
| `--api-key` | API Key da Anthropic |
| `--output` | Arquivo de saída |
| `--count` | Número de flashcards |
| `--language` | Idioma (padrão: português) |
| `--difficulty` | Nível de dificuldade |

## 💡 Dicas de Uso

✅ **Use com textos bem estruturados** — PDFs com boa formatação geram melhores flashcards  
✅ **Comece com poucos flashcards** — Use `--count 5` para testar  
✅ **Revise as questões geradas** — A IA é útil mas nem sempre perfeita  
✅ **Combine com outras fontes** — Crie flashcards manualmente também  
✅ **Estude regularmente** — A repetição espaçada funciona com consistência  

## 🐛 Solução de Problemas

### Erro: "Chave de API inválida"
```
Solução: Verifique se a variável de ambiente está definida corretamente
export ANTHROPIC_API_KEY="sk-ant-..."
```

### Erro: "Arquivo não encontrado"
```
Solução: Certifique-se de que o arquivo existe e está no caminho correto
python anki_gen.py ./Anki/documento.pdf
```

### Erro: "Módulo não encontrado"
```
Solução: Reinstale as dependências
pip install --upgrade anthropic pymupdf
```

## 📚 Recursos Úteis

- [Anki - Site Oficial](https://apps.ankiweb.net)
- [Add-on AllInOne](https://ankiweb.net/shared/info/1566095810)
- [Anthropic API Docs](https://docs.anthropic.com)
- [Repetição Espaçada](https://pt.wikipedia.org/wiki/Repetição_espaçada)

## 📝 Exemplo de Fluxo Completo

```bash
# 1. Preparar documento
# (criar documento.pdf ou documento.md)

# 2. Definir API Key
export ANTHROPIC_API_KEY="sk-ant-..."

# 3. Gerar flashcards
python anki_gen.py documento.pdf --output meus_cards.txt --count 20

# 4. Abrir Anki e importar meus_cards.txt

# 5. Estudar os flashcards!
```

---

**Nível:** Iniciante a Intermediário | **Atualizado:** Maio 2026
