#!/bin/bash

echo "Ativando o ambiente virtual"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo "Iniciando script"
python3 app.py