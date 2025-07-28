#!/bin/bash

# Setup script for Proyecto-6-Web-iii
# This script activates the virtual environment and installs dependencies

echo "🚀 Configurando el proyecto..."

# Navigate to project directory
cd "$(dirname "$0")/Proyecto"

# Check if virtual environment exists
if [ ! -d "env" ]; then
    echo "❌ Error: No se encontró el entorno virtual 'env'"
    echo "💡 Creando nuevo entorno virtual..."
    python -m venv env
fi

# Activate virtual environment
echo "📦 Activando entorno virtual..."
source env/bin/activate

# Install dependencies
echo "📚 Instalando dependencias..."
pip install -r Proyecto/requirements.txt

echo "✅ ¡Configuración completada!"
echo ""
echo "Para ejecutar el servidor:"
echo "  cd Proyecto"
echo "  source env/bin/activate"
echo "  cd Proyecto"
echo "  python manage.py runserver"
echo ""
echo "O simplemente ejecuta: ./run_server.sh"