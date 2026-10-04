import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from config import BOT_TOKEN, ADMIN_ID, COSTOS, MENSAJES
from database import db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ===== HANDLERS DE COMANDOS =====

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start - Mostrar menú principal"""
    telegram_id = update.effective_user.id
    nombre_usuario = update.effective_user.username or update.effective_user.first_name

    # Registrar usuario si no existe
    if not db.obtener_usuario_telegram(telegram_id):
        db.registrar_usuario_telegram(telegram_id, nombre_usuario)

    mensaje = """
🔍 **BIENVENIDO A NETDARE** 🔍

Sistema de consulta de datos para Peru City.
Busca información de jugadores registrados.

Selecciona una opción:
    """

    keyboard = [
        [InlineKeyboardButton("🔎 Buscar por DNI", callback_data='buscar_dni')],
        [InlineKeyboardButton("📱 Buscar por Teléfono", callback_data='buscar_telefono')],
        [InlineKeyboardButton("👤 Buscar por Nombre", callback_data='buscar_nombre')],
        [InlineKeyboardButton("💳 Comprar Créditos", callback_data='comprar_creditos')],
        [InlineKeyboardButton("📊 Mis Créditos", callback_data='mis_creditos')],
        [InlineKeyboardButton("❓ Ayuda", callback_data='ayuda')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(mensaje, reply_markup=reply_markup, parse_mode='Markdown')

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manejar clicks en botones"""
    query = update.callback_query
    await query.answer()

    telegram_id = update.effective_user.id
    action = query.data

    if action == 'buscar_dni':
        await query.edit_message_text(
            text="📝 Envía el DNI del usuario que quieres buscar:\n\nEjemplo: 24681379"
        )
        context.user_data['esperando'] = 'dni'

    elif action == 'buscar_telefono':
        await query.edit_message_text(
            text="📱 Envía el número de teléfono:\n\nEjemplo: 987654321"
        )
        context.user_data['esperando'] = 'telefono'

    elif action == 'buscar_nombre':
        await query.edit_message_text(
            text="👤 Envía el nombre completo del usuario:\n\nEjemplo: Juan Pérez"
        )
        context.user_data['esperando'] = 'nombre'

    elif action == 'mis_creditos':
        creditos = db.obtener_creditos(telegram_id)
        await query.edit_message_text(
            text=f"💳 **TUS CRÉDITOS**\n\nCréditos disponibles: **{creditos}**\n\nUsa /start para volver al menú.",
            parse_mode='Markdown'
        )

    elif action == 'comprar_creditos':
        keyboard = [
            [InlineKeyboardButton("1,000 créditos - S/5", callback_data='comprar_1000')],
            [InlineKeyboardButton("5,000 créditos - S/20", callback_data='comprar_5000')],
            [InlineKeyboardButton("10,000 créditos - S/35", callback_data='comprar_10000')],
            [InlineKeyboardButton("◀️ Volver", callback_data='volver')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="💳 **COMPRAR CRÉDITOS**\n\nSelecciona un paquete:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    elif action == 'ayuda':
        await query.edit_message_text(
            text="""❓ **AYUDA - NETDARE**

/start - Mostrar menú principal
/cmds - Ver todos los comandos

**BÚSQUEDAS:**
• DNI: Cuesta 5 créditos
• Teléfono: Cuesta 4 créditos
• Nombre: Cuesta 3 créditos

**CÓMO COMPRAR CRÉDITOS:**
1. Abre Peru City
2. Gana dinero jugando
3. Compra un paquete de créditos
4. Avisa al admin
5. Recibe tus créditos en NetDare

Usa /start para volver al menú.""",
            parse_mode='Markdown'
        )

    elif action == 'volver':
        await start(update, context)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manejar mensajes de texto"""
    telegram_id = update.effective_user.id
    mensaje = update.message.text

    if 'esperando' not in context.user_data:
        await update.message.reply_text("Usa /start para comenzar")
        return

    tipo_busqueda = context.user_data.get('esperando')

    # Verificar créditos
    creditos = db.obtener_creditos(telegram_id)
    costo = COSTOS.get(tipo_busqueda, 0)

    if creditos < costo:
        await update.message.reply_text(
            f"❌ No tienes suficientes créditos.\nNecesitas: {costo}\nTienes: {creditos}\n\nUsa /start para comprar."
        )
        return

    # Realizar búsqueda
    resultado = None
    if tipo_busqueda == 'dni':
        resultado = db.buscar_por_dni(mensaje)
    elif tipo_busqueda == 'telefono':
        resultado = db.buscar_por_telefono(mensaje)
    elif tipo_busqueda == 'nombre':
        resultado = db.buscar_por_nombre(mensaje)

    if resultado:
        # Restar créditos
        db.restar_creditos(telegram_id, costo)

        # Mostrar resultado
        if isinstance(resultado, list):
            respuesta = "📋 **RESULTADOS DE LA BÚSQUEDA**\n\n"
            for usuario in resultado:
                respuesta += f"👤 {usuario['nombre_completo']}\nDNI: {usuario['dni']}\nTeléfono: {usuario.get('telefoneo', 'N/A')}\n\n"
        else:
            respuesta = f"""📋 **INFORMACIÓN DEL USUARIO**

👤 Nombre: {resultado['nombre_completo']}
🆔 DNI: {resultado['dni']}
📱 Teléfono: {resultado.get('telefoneo', 'N/A')}
🎂 Edad: {resultado.get('edad', 'N/A')}
💼 Profesión: {resultado.get('profesion', 'N/A')}
👰 Estado Civil: {resultado.get('estado_civil', 'N/A')}
💰 Dinero en Juego: S/{resultado.get('dinero_juego', 0)}
⭐ Nivel: {resultado.get('nivel', 1)}

✅ Búsqueda exitosa (-{costo} créditos)
Créditos restantes: {creditos - costo}"""

        await update.message.reply_text(respuesta, parse_mode='Markdown')
    else:
        await update.message.reply_text("❌ Usuario no encontrado en la base de datos.")

    context.user_data.pop('esperando', None)

async def cmds(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /cmds - Ver todos los comandos"""
    mensaje = """📋 **COMANDOS DISPONIBLES**

/start - Menú principal
/cmds - Ver este menú
/miinfo - Tu información
/soporte - Contactar soporte

**BÚSQUEDAS:**
• 🔍 DNI (5 créditos)
• 📱 Teléfono (4 créditos)
• 👤 Nombre (3 créditos)

Usa /start para comenzar."""

    await update.message.reply_text(mensaje, parse_mode='Markdown')

def main():
    """Iniciar el bot"""
    print("🚀 Iniciando NetDare Bot...")

    # Conectar a BD
    db.conectar()

    # Crear aplicación
    app = Application.builder().token(BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cmds", cmds))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot listo. Escuchando mensajes...")
    app.run_polling()

if __name__ == '__main__':
    main()
