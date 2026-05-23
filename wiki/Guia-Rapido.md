# 🚀 Guia Rápido - Comandos Essenciais

Referência rápida dos comandos mais usados em cada tecnologia.

## 🐳 Docker - Comandos Rápidos

```bash
# Instalação
curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh

# Verificar versão
docker --version

# Pesquisar e baixar
docker search hello-world
docker pull ubuntu:latest
docker pull mariadb:20.2

# Listar
docker images              # Imagens
docker ps                  # Containers em execução
docker ps -a               # Todos os containers

# Executar
docker run hello-world                    # Uma vez
docker run -dit ubuntu                    # Interativo em background
docker run -d -p 3306:3306 mariadb        # Com mapeamento de porta

# Gerenciar containers
docker exec -it <container-id> /bin/bash  # Acessar terminal
docker stop <container-id>                # Parar
docker start <container-id>               # Iniciar
docker rm <container-id>                  # Remover

# Logs
docker logs <container-id>
docker logs -f <container-id>  # Acompanhar em tempo real
```

## ⚙️ Ansible - Comandos Rápidos

```bash
# Instalação
pip install ansible

# Verificar versão
ansible --version

# Executar playbook
ansible-playbook playbook.yml
ansible-playbook playbook.yml -i inventory.ini
ansible-playbook playbook.yml -v         # Verbose
ansible-playbook playbook.yml --check    # Dry-run

# Ansible Ad-hoc
ansible all -i inventory.ini -m ping
ansible all -m setup
ansible group_name -m shell -a "comando"
```

## 📚 Anki - Comandos Rápidos

```bash
# Instalação
pip install anthropic pymupdf

# Gerar flashcards
python anki_gen.py documento.pdf
python anki_gen.py notas.md --output cards.txt
python anki_gen.py file.pdf --api-key "sk-ant-..."

# Definir chave de API
export ANTHROPIC_API_KEY="sk-ant-..."  # Linux/Mac
$env:ANTHROPIC_API_KEY = "sk-ant-..."   # Windows PowerShell
```

## 🎯 Fluxos de Trabalho

### Docker: Criar e Executar Container

```bash
docker pull ubuntu:latest
docker run -dit --name meu-container ubuntu
docker exec -it meu-container /bin/bash
# ... fazer coisas ...
docker stop meu-container
docker rm meu-container
```

### Ansible: Executar Playbook

```bash
cd Ansible/
ansible-playbook 03-template-instance-start.yml --check  # Preview
ansible-playbook 03-template-instance-start.yml          # Executar
```

### Anki: Gerar e Importar

```bash
python Anki/anki_gen.py ~/Downloads/estudo.pdf
# Abrir Anki Desktop
# Arquivo → Importar → Selecionar output.txt
```

## 📋 Atalhos Úteis

### Docker

| Atalho | Significado |
|--------|-----------|
| `-d` | Detach (background) |
| `-it` | Interactive + TTY |
| `-p` | Port mapping |
| `-e` | Environment variable |
| `-v` | Volume mount |

### Ansible

| Flag | Significado |
|------|-----------|
| `-i` | Inventory file |
| `-v` | Verbose (pode usar -vvv) |
| `--check` | Dry-run |
| `-t` | Tags específicas |

## 🔍 Troubleshooting Rápido

### Docker não encontra imagem?
```bash
docker pull nome-da-imagem
```

### Container não inicia?
```bash
docker logs <container-id>
docker logs -f <container-id>  # Ver logs em tempo real
```

### Ansible conecta mal?
```bash
ansible all -i inventory.ini -m ping  # Testar conectividade
```

### API Key do Anki inválida?
```bash
echo $ANTHROPIC_API_KEY  # Verificar se está definida
```

## 📚 Links Rápidos

- 🐳 Docker Hub: https://hub.docker.com
- 📖 Ansible Docs: https://docs.ansible.com
- 🤖 Anthropic API: https://console.anthropic.com
- 📚 Anki: https://apps.ankiweb.net

---

**Atualizado:** Maio 2026 | **Uso:** Referência rápida
