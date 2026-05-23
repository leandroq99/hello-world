# 📋 Estrutura do Projeto

Guia completo sobre a organização e os arquivos do repositório.

## 🗂️ Árvore de Diretórios

```
hello-world/
├── README.md                          # Documentação principal do projeto
├── LICENSE                            # Licença do projeto
├── file_fixes.yml                     # Playbook Ansible para correções
├── .github/
│   └── copilot-instructions.md        # Instruções para Copilot
├── Docker/
│   └── Docker_notes.txt               # Notas e comandos Docker
├── Ansible/
│   ├── 01-ec2-snapshot.yml            # Criar snapshots EC2
│   ├── 02-asg-scale-down.yml          # Reduzir Auto Scaling Group
│   ├── 03-template-instance-start.yml # Iniciar instância template
│   ├── 04-checkpoint-validation.yml   # Validar checkpoints
│   ├── 05-template-instance-stop.yml  # Parar instância template
│   ├── 06-create-ami.yml              # Criar AMI
│   ├── 07-update-launch-template.yml  # Atualizar Launch Template
│   ├── 08-asg-scale-up.yml            # Aumentar Auto Scaling Group
│   └── aws-ec2-ami-update.yml         # Atualizar AMI (consolidado)
├── Anki/
│   ├── anki_gen.py                    # Script gerador de flashcards
│   ├── README_anki_gen.md             # Documentação do anki_gen
│   ├── Execucao do Projeto...csv      # Dados de exemplo
│   └── [outros arquivos de apoio]
├── main1                              # Arquivo/rascunho de estudos
├── main2                              # Arquivo/rascunho de estudos
├── teste                              # Arquivo de teste
└── wiki/                              # Documentação expandida (esta wiki)
    ├── Home.md                        # Página inicial
    ├── Docker.md                      # Guia detalhado do Docker
    ├── Ansible.md                     # Guia detalhado do Ansible
    ├── Anki.md                        # Guia detalhado do Anki
    └── Estrutura.md                   # Este arquivo
```

## 📄 Descrição dos Arquivos Principais

### Raiz do Repositório

| Arquivo | Descrição |
|---------|-----------|
| **README.md** | Documentação principal com visão geral do projeto |
| **LICENSE** | Licença do repositório (provavelmente MIT ou similar) |
| **file_fixes.yml** | Playbook Ansible para correções (exemplo básico) |
| **main1, main2, teste** | Arquivos e rascunhos usados durante estudos |

### 📁 Pasta: Docker/

**Objetivo:** Documentação sobre Docker e containerização

| Arquivo | Tipo | Descrição |
|---------|------|-----------|
| **Docker_notes.txt** | Texto | Notas completas sobre Docker, comandos CLI e conceitos básicos |

**Conteúdo:**
- Conceitos fundamentais de containerização
- Instruções de instalação
- Comandos principais (run, pull, ps, exec, etc.)
- Exemplos práticos com Debian, MySQL, MariaDB

**Como usar:**
1. Abra o arquivo para referência rápida
2. Use como base para estudar Docker
3. Copie comandos para praticar

### 📁 Pasta: Ansible/

**Objetivo:** Automação de infraestrutura AWS com Ansible

| Arquivo | Tipo | Descrição |
|---------|------|-----------|
| **01-ec2-snapshot.yml** | YAML | Cria snapshots de volumes EC2 |
| **02-asg-scale-down.yml** | YAML | Reduz Auto Scaling Group |
| **03-template-instance-start.yml** | YAML | Inicia instância template |
| **04-checkpoint-validation.yml** | YAML | Valida checkpoints |
| **05-template-instance-stop.yml** | YAML | Para instância template |
| **06-create-ami.yml** | YAML | Cria Amazon Machine Image |
| **07-update-launch-template.yml** | YAML | Atualiza Launch Template |
| **08-asg-scale-up.yml** | YAML | Aumenta Auto Scaling Group |
| **aws-ec2-ami-update.yml** | YAML | Workflow completo de atualização |

**Padrão de Workflow:**

```
1. Iniciar template (03)
   ↓
2. Gerar snapshot (01)
   ↓
3. Validar checkpoint (04)
   ↓
4. Parar template (05)
   ↓
5. Criar AMI (06)
   ↓
6. Atualizar template (07)
   ↓
7. Escalar (02 ou 08)
```

**Como usar:**
```bash
ansible-playbook Ansible/01-ec2-snapshot.yml
ansible-playbook Ansible/06-create-ami.yml
```

### 📁 Pasta: Anki/

**Objetivo:** Automação de criação de flashcards

| Arquivo | Tipo | Descrição |
|---------|------|-----------|
| **anki_gen.py** | Python | Script principal gerador de flashcards |
| **README_anki_gen.md** | Markdown | Documentação completa com instruções |
| **Execucao do Projeto...csv** | CSV | Dados de exemplo para importação |

**Funcionalidades:**
- Converte PDFs em flashcards
- Suporta Markdown como entrada
- Integra com add-on AllInOne do Anki
- Usa Anthropic API para geração inteligente

**Como usar:**
```bash
python Anki/anki_gen.py documento.pdf
python Anki/anki_gen.py notas.md --output flashcards.txt
```

### 📁 Pasta: .github/

**Objetivo:** Configurações específicas do GitHub

| Arquivo | Descrição |
|---------|-----------|
| **copilot-instructions.md** | Instruções para GitHub Copilot |

## 🎯 Fluxo de Aprendizado Recomendado

```
┌─ Iniciante
│  ├─ 1. Leia Docker/Docker_notes.txt
│  ├─ 2. Pratique comandos Docker
│  └─ 3. Leia Anki/README_anki_gen.md
│
├─ Intermediário
│  ├─ 1. Explore playbooks Ansible
│  ├─ 2. Entenda workflow de EC2/AMI
│  └─ 3. Teste anki_gen.py com PDFs
│
└─ Avançado
   ├─ 1. Customize playbooks Ansible
   ├─ 2. Integre com infraestrutura real
   └─ 3. Contribua com novos playbooks
```

## 📊 Estatísticas do Projeto

| Métrica | Valor |
|---------|-------|
| **Pastas principais** | 3 (Docker, Ansible, Anki) |
| **Playbooks Ansible** | 9 arquivos .yml |
| **Scripts Python** | 1 (anki_gen.py) |
| **Documentação** | Múltiplos arquivos .md e .txt |
| **Linguagem** | Português |
| **Nível** | Iniciante a Intermediário |

## 🔗 Relacionamentos

```
Docker
  ├─ Usado em: Alguns playbooks Ansible
  └─ Aplicado em: Estudo de containerização

Ansible
  ├─ Automatiza: Infraestrutura AWS
  ├─ Usa: Playbooks YAML
  └─ Resultado: AMI e Auto Scaling

Anki
  ├─ Gera: Flashcards automaticamente
  ├─ Entrada: PDFs, Markdown
  └─ Saída: Arquivos compatíveis com Anki
```

## 🚀 Como Contribuir

Se quiser adicionar novos arquivos ou pastas:

1. **Para Docker**: Adicione notas em `Docker/`
2. **Para Ansible**: Crie playbooks em `Ansible/` com nome descritivo
3. **Para Anki**: Adicione scripts ou dados em `Anki/`
4. **Para documentação**: Atualize arquivos `.md` correspondentes

## 📝 Convenções

- ✅ Nomes de arquivo em **snake_case** com números de ordem (ex: `01-ec2-snapshot.yml`)
- ✅ Documentação em **português**
- ✅ Exemplos práticos com comandos reais
- ✅ Referências a documentações oficiais
- ✅ Comentários explicativos em código

## ⚠️ Importante

Este é um repositório **educacional**:
- Não é código de produção
- Experimentos e rascunhos são permitidos
- Dados de exemplo podem incluir valores fictícios
- Use com cuidado em ambientes reais

---

**Atualizado:** Maio 2026 | **Versão:** 1.0
