# 🤖 NetDare Bot - Peru City

Bot de Telegram profesional para búsqueda de jugadores en el juego Peru City.

## 📋 Características

- ✅ Búsqueda por DNI, Teléfono y Nombre
- ✅ Sistema de créditos escalable
- ✅ Menú interactivo con botones
- ✅ Base de datos MySQL
- ✅ Panel de administrador
- ✅ Soporte para miles de usuarios simultáneos

## 🚀 Instalación

### Requisitos
- Python 3.9+
- MySQL/MariaDB
- Token de Bot Telegram

### Pasos

1. **Clonar/Descargar el proyecto**
```bash
cd C:\xampp\htdocs\netdare-bot
```

2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

3. **Crear base de datos**
```bash
mysql -u root -p < database/schema.sql
```

4. **Configurar variables de entorno**
```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar .env con tus datos
# BOT_TOKEN=Tu_Token_De_Telegram
# ADMIN_ID=Tu_ID_De_Telegram
```

5. **Insertar datos de prueba**
```bash
python datos_prueba.py
```

6. **Ejecutar el bot**
```bash
python bot.py
```

## 📝 Estructura del Proyecto

```
netdare-bot/
├── bot.py                 # Bot principal
├── config.py              # Configuración
├── database.py            # Conexión a BD
├── datos_prueba.py        # Datos de prueba
├── database/
│   └── schema.sql        # Esquema de BD
├── requirements.txt       # Dependencias
├── .env.example          # Variables de entorno
└── README.md
```

## 🎮 Uso

**Comandos disponibles:**
- `/start` - Menú principal
- `/cmds` - Ver comandos
- `/miinfo` - Tu información

**Búsquedas:**
- 🔍 DNI: 5 créditos
- 📱 Teléfono: 4 créditos
- 👤 Nombre: 3 créditos

## 💳 Sistema de Créditos

1. Jugador compra créditos en Peru City
2. Admin ve la compra
3. Admin usa comando admin para dar créditos
4. Usuario puede hacer búsquedas

## 📊 Base de Datos

- `usuarios_juego` - Jugadores registrados
- `usuarios_telegram` - Usuarios del bot
- `transacciones_creditos` - Historial de créditos
- `busquedas` - Historial de búsquedas

## 🔐 Seguridad

- Autenticación por Telegram ID
- Validación de créditos
- Logs de transacciones
- Rate limiting (implementable)

## 📈 Funciones Futuras

- [ ] Árbol genealógico
- [ ] Historial de denuncias
- [ ] Reputación de jugadores
- [ ] Ubicación en mapa
- [ ] Historial delictivo
- [ ] Chat entre jugadores
- [ ] Panel web de admin

## 🆘 Soporte

Para reportar bugs o sugerencias, contacta al admin.

## 👥 Autores

- **Desarrollador Bot**: Haiku Claude
- **Juego Peru City**: Dare
- **Gestor Proyecto**: Net

---

**Última actualización**: 2026-10-04
