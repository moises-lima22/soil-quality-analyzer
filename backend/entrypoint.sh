#!/bin/bash
set -e

echo "⏳ Executando setup_oracle.py..."
python3 config/setup_oracle.py

echo "🚀 Iniciando app.py..."
exec python3 app.py
