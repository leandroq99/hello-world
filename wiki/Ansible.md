# ⚙️ Guia do Ansible

Automação de infraestrutura com foco em operações AWS EC2, AMI e Auto Scaling.

## 📖 O que é Ansible?

Ansible é uma ferramenta de **automação de infraestrutura** que permite gerenciar múltiplos servidores através de **playbooks** (arquivos YAML com instruções).

### Características

- 🎯 **Agentless** — Não requer instalação de cliente nos servidores
- 📝 **YAML simples** — Fácil leitura e escrita
- 🔄 **Idempotente** — Pode ser executado múltiplas vezes com segurança
- ☁️ **Multi-cloud** — Compatível com AWS, Azure, GCP, etc.

## 📁 Playbooks Disponíveis

Este projeto contém playbooks para automação de infraestrutura AWS:

### 1. **01-ec2-snapshot.yml**
Cria snapshots (backups) de volumes EC2.

**Uso:**
```bash
ansible-playbook 01-ec2-snapshot.yml
```

### 2. **02-asg-scale-down.yml**
Reduz o número de instâncias em um Auto Scaling Group (ASG).

**Uso:**
```bash
ansible-playbook 02-asg-scale-down.yml
```

### 3. **03-template-instance-start.yml**
Inicia uma instância template para preparação.

**Uso:**
```bash
ansible-playbook 03-template-instance-start.yml
```

### 4. **04-checkpoint-validation.yml**
Valida pontos de verificação (checkpoints) na infraestrutura.

**Uso:**
```bash
ansible-playbook 04-checkpoint-validation.yml
```

### 5. **05-template-instance-stop.yml**
Para uma instância template após preparação.

**Uso:**
```bash
ansible-playbook 05-template-instance-stop.yml
```

### 6. **06-create-ami.yml**
Cria uma Amazon Machine Image (AMI) a partir de uma instância.

**Uso:**
```bash
ansible-playbook 06-create-ami.yml
```

### 7. **07-update-launch-template.yml**
Atualiza um Launch Template com uma nova AMI.

**Uso:**
```bash
ansible-playbook 07-update-launch-template.yml
```

### 8. **08-asg-scale-up.yml**
Aumenta o número de instâncias em um Auto Scaling Group (ASG).

**Uso:**
```bash
ansible-playbook 08-asg-scale-up.yml
```

### 9. **aws-ec2-ami-update.yml**
Playbook consolidado para atualizar AMI em instâncias EC2.

**Uso:**
```bash
ansible-playbook aws-ec2-ami-update.yml
```

## 🏗️ Estrutura de um Playbook

```yaml
- name: Descrição do playbook
  hosts: all                    # Quais hosts executar
  tasks:                        # Lista de tarefas
    - name: Descrição da tarefa
      module_name:              # Qual módulo usar
        parameter: value        # Parâmetros do módulo
```

## 🔑 Conceitos Principais

| Conceito | Descrição |
|----------|-----------|
| **Playbook** | Arquivo YAML com conjunto de tasks |
| **Task** | Ação a ser executada (ex: criar arquivo, instalar pacote) |
| **Module** | Plugin que executa a ação (ex: `file`, `ec2`, `shell`) |
| **Host** | Máquina alvo da execução |
| **Inventory** | Arquivo com lista de hosts |
| **Role** | Conjunto reutilizável de tasks |

## 🚀 Instalação

### Linux/macOS

```bash
pip install ansible
```

### Verificar Instalação

```bash
ansible --version
```

## 📋 Arquivo Inventory (hosts)

```ini
[aws]
ec2-instance-1 ansible_host=10.0.0.1
ec2-instance-2 ansible_host=10.0.0.2

[aws:vars]
ansible_user=ec2-user
ansible_ssh_private_key_file=~/.ssh/key.pem
```

## 💻 Executar Playbooks

### Sintaxe Básica

```bash
# Executar um playbook
ansible-playbook <arquivo>.yml

# Executar com verbosidade (debug)
ansible-playbook <arquivo>.yml -v
ansible-playbook <arquivo>.yml -vv
ansible-playbook <arquivo>.yml -vvv

# Executar em hosts específicos
ansible-playbook <arquivo>.yml -i <inventory-file>

# Executar sem fazer mudanças (dry-run)
ansible-playbook <arquivo>.yml --check
```

## 🔗 Módulos Comuns

| Módulo | Descrição |
|--------|-----------|
| `file` | Gerenciar arquivos e diretórios |
| `ec2` | Gerenciar instâncias EC2 |
| `shell` | Executar comandos shell |
| `copy` | Copiar arquivos |
| `yum` / `apt` | Instalar pacotes |

## 📚 Recursos Úteis

- [Documentação Oficial do Ansible](https://docs.ansible.com)
- [Módulos AWS para Ansible](https://docs.ansible.com/ansible/latest/collections/amazon/aws/)
- [Ansible Galaxy - Roles compartilhados](https://galaxy.ansible.com)

## ⚠️ Boas Práticas

✅ Sempre execute `--check` antes de mudanças em produção  
✅ Use variáveis para valores dinâmicos  
✅ Documente cada playbook e tarefa  
✅ Mantenha o inventory versionado (sem senhas)  
✅ Use roles para organizar playbooks complexos  

---

**Nível:** Intermediário | **Atualizado:** Maio 2026
