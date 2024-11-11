#!/bin/bash

if [ ! -f "requirements.txt" ]; then
    echo "Error: requirements.txt file not found!"
    exit 1
fi

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

source venv/bin/activate

echo "Installing packages from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. Virtual environment is ready and packages are installed."

source venv/bin/activate