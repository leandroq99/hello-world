#!/usr/bin/env bash
# Uso: ./listar-grupo.sh <nome_do_grupo>

GRUPO="$1"

if [ -z "$GRUPO" ]; then
  echo "Uso: $0 <nome_do_grupo>"
  echo "Exemplo: $0 desenvolvedores"
  exit 1
fi

echo "📋 Usuários no grupo '$GRUPO':"
echo "----------------------------------------"

ldapsearch -x -H ldap://localhost -D "cn=admin,dc=ipa,dc=local" -w 'Admin@123' -b "ou=Groups,dc=ipa,dc=local" "(cn=$GRUPO)" memberUid | grep memberUid | awk '{print $2}'

if [ $? -ne 0 ]; then
  echo "❌ Grupo '$GRUPO' não encontrado ou sem membros"
fi
