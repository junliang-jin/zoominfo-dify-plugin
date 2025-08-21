#!/bin/bash
# Script to activate the virtual environment for the ZoomInfo Dify Plugin

echo "Activating virtual environment for ZoomInfo Dify Plugin..."
source .venv/bin/activate
echo "Virtual environment activated!"
echo "Python version: $(python --version)"
echo "Installed packages:"
pip list
