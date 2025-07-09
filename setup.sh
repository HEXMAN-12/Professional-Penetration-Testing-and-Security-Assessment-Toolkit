#!/bin/bash

# On Linux Environment
sudo apt update
sudo apt install python3.11-venv   # or the relevant Python version package

# Create and activate the virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install flask werkzeug pikepdf msoffcrypto-tool python-magic

# Run the Flask application
python app.py

# Install external tools (system-wide): On Ubuntu/Debian:
sudo apt-get install hash-identifier cewl medusa aircrack-ng wordlists

# Verify directories and files:
mkdir uploads

# Run the Flask app:
python app.py