#!/bin/bash

set -e

echo "=========================================="
echo "  iniciando Jenkins"
echo "=========================================="

mkdir -p /relatorios
chown jenkins:jenkins /relatorios
chmod 755 /relatorios
echo "[OK] Permissões do diretório /relatorios ajustadas."

if [[ -S /var/run/docker.sock ]]; then
    chmod 666 /var/run/docker.sock
    echo "[OK] Permissão do Docker socket ajustada."
else
    echo "[AVISO] Docker socket não encontrado em /var/run/docker.sock."
    echo "        Certifique-se de que o volume está montado no docker-compose.yml."
fi

echo "[INFO] Iniciando Jenkins como usuário jenkins..."
exec gosu jenkins /usr/bin/tini -- /usr/local/bin/jenkins.sh "$@"
