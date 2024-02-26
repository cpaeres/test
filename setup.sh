echo "Iniciando configuración del entorno..."

# Instalar dependencias de Python
pip install -r requirements.txt

# Configurar Streamlit para que se ejecute correctamente en Heroku
mkdir -p ~/.streamlit

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
