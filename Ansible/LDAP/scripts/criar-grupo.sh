#!/usr/bin/env bash
# Uso: ./criar-grupo.sh <nome_do_grupo> [gid_number]

GRUPO="$1"
GID="$2"

if [ -z "$GRUPO" ]; then
  echo "Uso: $0 <nome_do_grupo> [gid_number]"
  echo "Exemplo: $0 desenvolvedores"
  echo "Exemplo: $0 desenvolvedores 20001"
  exit 1
fi

BASE_DN="dc=ipa,dc=local"
BIND_DN="cn=admin,$BASE_DN"
BIND_PW="Admin@123"

# Se não informou GID, calcula o próximo disponível
if [ -z "$GID" ]; then
  # Busca todos os gidNumber existentes
  GID_LIST=$(ldapsearch -x -H ldap://localhost -D "$BIND_DN" -w "$BIND_PW" -b "ou=Groups,$BASE_DN" "(objectClass=posixGroup)" gidNumber 2>/dev/null | grep "^gidNumber:" | awk '{print $2}' | sort -n)

  if [ -z "$GID_LIST" ]; then
    # Se não houver nenhum grupo, começa do 10000
    GID=10000
  else
    # Pega o maior GID e soma 1
    LAST_GID=$(echo "$GID_LIST" | tail -1)
    GID=$((LAST_GID + 1))
  fi
fi

# Garante que o GID é um número válido
if ! [[ "$GID" =~ ^[0-9]+$ ]]; then
  echo "❌ GID inválido! Usando valor padrão 10000."
  GID=10000
fi

# Verifica se o grupo já existe
EXISTING=$(ldapsearch -x -H ldap://localhost -D "$BIND_DN" -w "$BIND_PW" -b "ou=Groups,$BASE_DN" "(cn=$GRUPO)" dn 2>/dev/null | grep "^dn:")

if [ -n "$EXISTING" ]; then
  echo "⚠️  Grupo '$GRUPO' já existe!"
  echo "   Para adicionar usuários, use: ./add-usuario-grupo.sh <usuario> $GRUPO"
  exit 1
fi

# Cria o arquivo LDIF
cat > /tmp/group.ldif <<EOF
dn: cn=$GRUPO,ou=Groups,$BASE_DN
objectClass: top
objectClass: posixGroup
cn: $GRUPO
gidNumber: $GID
EOF

# Aplica
ldapadd -x -D "$BIND_DN" -w "$BIND_PW" -f /tmp/group.ldif

if [ $? -eq 0 ]; then
  echo ""
  echo "✅ Grupo '$GRUPO' criado com sucesso!"
  echo "   GID: $GID"
  echo ""
  echo "📋 Para adicionar usuários:"
  echo "   ./add-usuario-grupo.sh <usuario> $GRUPO"
else
  echo "❌ Falha ao criar grupo. Verifique os logs acima."
fi
