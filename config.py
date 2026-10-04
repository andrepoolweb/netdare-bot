import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID', 0))

# Base de Datos
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_NAME = os.getenv('DB_NAME', 'netdare_db')
DB_PORT = int(os.getenv('DB_PORT', 3306))

# Configuración
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# Costos de búsquedas (en créditos)
COSTOS = {
    'dni': 5,
    'telefono': 4,
    'nombre': 3
}

# Mensajes
MENSAJES = {
    'sin_creditos': '❌ No tienes suficientes créditos para esta búsqueda.',
    'busqueda_no_encontrada': '❌ Usuario no encontrado en la base de datos.',
    'creditos_actualizado': '✅ Créditos actualizados correctamente.',
    'sin_permiso': '❌ No tienes permiso para usar este comando.'
}
