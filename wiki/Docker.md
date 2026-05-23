# 🐳 Guia do Docker

Uma introdução prática a Docker, containerização e comandos essenciais.

## 📖 O que é Docker?

Docker é uma plataforma de **containerização** que permite empacotar e executar aplicações de forma isolada e consistente em qualquer ambiente.

### Conceitos Principais

| Conceito | Descrição |
|----------|-----------|
| **Container** | Isolamento leve de uma aplicação/processo do SO, consumindo poucos recursos |
| **Imagem** | Template usado para criar containers (como um blueprint) |
| **Registry** | Repositório centralizado de imagens (ex: Docker Hub) |
| **Microserviços** | Quebra de aplicações monolíticas em serviços independentes |

## 🛠️ Instalação

### Método Simples (Linux)

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

### Verificar Instalação

```bash
docker --version
```

## 🎓 Comandos Essenciais

### Gerenciamento de Imagens

| Comando | Descrição |
|---------|-----------|
| `docker search <name>` | Pesquisa uma imagem |
| `docker pull <image>` | Faz download da imagem |
| `docker images` | Lista todas as imagens instaladas |
| `docker rmi <image-id>` | Remove uma imagem |

### Exemplos

```bash
# Pesquisar e baixar uma imagem
docker search hello-world
docker pull hello-world

# Baixar uma versão específica (com tag)
docker pull mariadb:20.2

# Listar imagens instaladas
docker images
```

### Gerenciamento de Containers

| Comando | Descrição |
|---------|-----------|
| `docker run <image>` | Executa/cria um container |
| `docker ps` | Lista containers em execução |
| `docker ps -a` | Lista todos os containers (em execução e finalizados) |
| `docker start <container-id>` | Inicia um container parado |
| `docker stop <container-id>` | Para um container |
| `docker rm <container-id>` | Remove um container |

### Exemplos

```bash
# Executar uma imagem
docker run hello-world

# Listar containers
docker ps          # Apenas em execução
docker ps -a       # Todos

# Parar e remover containers
docker stop <container-id>
docker rm <container-id>
```

### Interação com Containers

| Comando | Descrição |
|---------|-----------|
| `docker exec -it <container-id> /bin/bash` | Abre terminal interativo no container |
| `docker logs <container-id>` | Exibe logs do container |
| `docker cp <file> <container-id>:/path` | Copia arquivo para o container |

### Exemplo

```bash
# Baixar Debian e executar interativamente
docker pull debian
docker run -dit debian

# Acessar o container
docker exec -it <container-id> /bin/bash
```

## 🚀 Flags Importantes no docker run

| Flag | Descrição |
|------|-----------|
| `-d, --detach` | Executa em background (retorna ID do container) |
| `-it` | Aloca terminal pseudo-TTY (permite interação) |
| `-p 8080:80` | Mapeia porta (host:container) |
| `-e VAR=value` | Define variável de ambiente |
| `-v /host:/container` | Monta volume (compartilha arquivo/pasta) |
| `--name my-app` | Define nome do container |

## 📚 Aplicações Comuns

### MySQL

```bash
docker pull mysql:latest
docker run -d --name mysql-app -e MYSQL_ROOT_PASSWORD=senha -p 3306:3306 mysql
```

### MariaDB

```bash
docker pull mariadb:20.2
docker run -d --name mariadb-app -e MYSQL_ROOT_PASSWORD=senha -p 3306:3306 mariadb:20.2
```

## 🔗 Recursos Úteis

- [Docker Hub - Repositório oficial](https://hub.docker.com)
- [Documentação Oficial do Docker](https://docs.docker.com)
- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/cli/)

## 📝 Notas Adicionais

- Se você não baixar a imagem antes de executar `docker run`, o Docker fará isso automaticamente
- Containers são efêmeros por padrão — quando removidos, os dados dentro são perdidos
- Use volumes para persistir dados entre containers

---

**Nível:** Iniciante | **Atualizado:** Maio 2026
