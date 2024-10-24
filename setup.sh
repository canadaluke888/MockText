#!/bin/bash 

echo "Creating virtual environment..."
python3 -m venv .venv
echo "Done!"

source .venv/bin/activate  

echo "Install dependencies..."
pip install -r requirements.txt
echo "Done!"

deactivate
