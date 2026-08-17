#!/usr/bin/env bash
# Uso: ./add-usuario-grupo.sh <username> <nome_do_grupo>

USUARIO="$1"
GRUPO="$2"

if [ -z "$USUARIO" ] || [ -z "$GRUPO" ]; then
  echo "Uso: $0 <username> <nome_do_grupo>"
  echo "Exemplo: $0 leandro devs"
  exit 1
fi

BASE_DN="dc=ipa,dc=local"
BIND_DN="cn=admin,$BASE_DN"
BIND_PW="Admin@123"

# Verifica se o usuário existe
USER_DN=$(ldapsearch -x -H ldap://localhost -D "$BIND_DN" -w "$BIND_PW" -b "ou=People,$BASE_DN" "(uid=$USUARIO)" dn 2>/dev/null | grep "^dn:" | awk '{print $2}')

if [ -z "$USER_DN" ]; then
  echo "❌ Usuário '$USUARIO' não encontrado!"
  exit 1
fi

# Verifica se o grupo existe
GROUP_DN=$(ldapsearch -x -H ldap://localhost -D "$BIND_DN" -w "$BIND_PW" -b "ou=Groups,$BASE_DN" "(cn=$GRUPO)" dn 2>/dev/null | grep "^dn:" | awk '{print $2}')

if [ -z "$GROUP_DN" ]; then
  echo "❌ Grupo '$GRUPO' não encontrado!"
  echo "   Para criar, use: ./criar-grupo-com-usuarios.sh $GRUPO <usuario1> <usuario2> ..."
  exit 1
fi

# Adiciona o usuário ao grupo
cat > /tmp/adduser.ldif <<EOF
dn: $GROUP_DN
changetype: modify
add: memberUid
memberUid: $USUARIO
EOF

ldapmodify -x -D "$BIND_DN" -w "$BIND_PW" -f /tmp/adduser.ldif

if [ $? -eq 0 ]; then
  echo "✅ Usuário '$USUARIO' adicionado ao grupo '$GRUPO'"
else
  echo "❌ Falha ao adicionar usuário ao grupo"
fi
