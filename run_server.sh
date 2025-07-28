#!/bin/bash

# Script to run the Django development server
# Este script activa el entorno virtual y ejecuta el servidor

echo "🚀 Iniciando servidor Django..."

# Navigate to project directory
cd "$(dirname "$0")/Proyecto"

# Check if virtual environment exists
if [ ! -d "env" ]; then
    echo "❌ Error: No se encontró el entorno virtual."
    echo "💡 Ejecuta primero: ./setup.sh"
    exit 1
fi

# Activate virtual environment
source env/bin/activate

# Check if Django is installed
if ! python -c "import django" 2>/dev/null; then
    echo "❌ Error: Django no está instalado."
    echo "💡 Ejecuta primero: ./setup.sh"
    exit 1
fi

# Navigate to Django project
cd Proyecto

# Run migrations (just in case)
echo "🔄 Verificando migraciones..."
python manage.py migrate --run-syncdb

# Start the server
echo "🌐 Iniciando servidor en http://127.0.0.1:8000/"
python manage.py runserver