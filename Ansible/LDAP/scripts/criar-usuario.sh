#!/usr/bin/env bash
# Uso: ./criar-usuario.sh <username> <nome_completo> <email> <senha>

USERNAME="$1"
FULLNAME="$2"
EMAIL="$3"
PASSWORD="$4"

if [ -z "$USERNAME" ] || [ -z "$FULLNAME" ] || [ -z "$EMAIL" ] || [ -z "$PASSWORD" ]; then
  echo "Uso: $0 <username> <nome_completo> <email> <senha>"
  echo "Exemplo: $0 joao \"Joao Silva\" joao@email.com Senha123"
  exit 1
fi

# Pega o próximo UID disponível (mais robusto)
BASE_DN="dc=ipa,dc=local"
BIND_DN="cn=admin,$BASE_DN"
BIND_PW="Admin@123"

# Busca todos os uidNumber existentes
UID_LIST=$(ldapsearch -x -H ldap://localhost -D "$BIND_DN" -w "$BIND_PW" -b "$BASE_DN" "(objectClass=posixAccount)" uidNumber 2>/dev/null | grep "^uidNumber:" | awk '{print $2}' | sort -n)

if [ -z "$UID_LIST" ]; then
  # Se não houver nenhum usuário, começa do 10000
  NEXT_UID=10000
else
  # Pega o maior UID e soma 1
  LAST_UID=$(echo "$UID_LIST" | tail -1)
  NEXT_UID=$((LAST_UID + 1))
fi

# Garante que o UID é um número válido
if ! [[ "$NEXT_UID" =~ ^[0-9]+$ ]]; then
  echo "❌ Erro ao calcular UID. Usando valor padrão 10000."
  NEXT_UID=10000
fi

# Gera hash da senha
HASHED_PW=$(slappasswd -s "$PASSWORD")

# Extrai nome e sobrenome
GIVEN_NAME=$(echo "$FULLNAME" | awk '{print $1}')
SURNAME=$(echo "$FULLNAME" | awk '{print $NF}')

# Cria o arquivo LDIF
cat > /tmp/user.ldif <<EOF
dn: uid=$USERNAME,ou=People,$BASE_DN
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: posixAccount
uid: $USERNAME
cn: $FULLNAME
givenName: $GIVEN_NAME
sn: $SURNAME
mail: $EMAIL
uidNumber: $NEXT_UID
gidNumber: $NEXT_UID
homeDirectory: /home/$USERNAME
loginShell: /bin/bash
userPassword: $HASHED_PW
EOF

# Cria o grupo com o mesmo GID
cat >> /tmp/user.ldif <<EOF

dn: cn=$USERNAME,ou=Groups,$BASE_DN
objectClass: top
objectClass: posixGroup
cn: $USERNAME
gidNumber: $NEXT_UID
memberUid: $USERNAME
EOF

# Aplica
ldapadd -x -D "$BIND_DN" -w "$BIND_PW" -f /tmp/user.ldif

if [ $? -eq 0 ]; then
  echo ""
  echo "✅ Usuário '$USERNAME' criado com sucesso!"
  echo "   UID: $NEXT_UID"
  echo "   Grupo: $USERNAME (GID: $NEXT_UID)"
  echo ""
  echo "🔑 Para testar:"
  echo "   ldapwhoami -x -D 'uid=$USERNAME,ou=People,$BASE_DN' -w '$PASSWORD'"
else
  echo "❌ Falha ao criar usuário. Verifique os logs acima."
fi
