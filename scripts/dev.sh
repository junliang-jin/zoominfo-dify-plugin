#!/bin/bash
# Development helper script for ZoomInfo Dify Plugin

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}ZoomInfo Dify Plugin - Development Helper${NC}"
echo "=============================================="

case "$1" in
    "activate")
        echo -e "${YELLOW}Activating virtual environment...${NC}"
        source .venv/bin/activate
        echo -e "${GREEN}Virtual environment activated!${NC}"
        echo "Python version: $(python --version)"
        ;;
    "install")
        echo -e "${YELLOW}Installing dependencies...${NC}"
        source .venv/bin/activate
        uv pip install -r requirements.txt
        echo -e "${GREEN}Dependencies installed!${NC}"
        ;;
    "test")
        echo -e "${YELLOW}Testing imports...${NC}"
        source .venv/bin/activate
        python -c "import dify_plugin; import requests; print('All imports successful!')"
        ;;
    "clean")
        echo -e "${YELLOW}Cleaning virtual environment...${NC}"
        rm -rf .venv
        echo -e "${GREEN}Virtual environment removed!${NC}"
        echo "Run 'uv venv' to recreate it."
        ;;
    *)
        echo "Usage: $0 {activate|install|test|clean}"
        echo ""
        echo "Commands:"
        echo "  activate  - Activate the virtual environment"
        echo "  install   - Install dependencies"
        echo "  test      - Test that all imports work"
        echo "  clean     - Remove virtual environment"
        echo ""
        echo "Examples:"
        echo "  $0 activate"
        echo "  $0 install"
        echo "  $0 test"
        ;;
esac
