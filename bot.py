from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 🔑 Coloca tu token aquí
TOKEN = 8373537941:AAFnP7UcsMI4-VvU7EfoabospT4uxnEIHfQ

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot 🤖. Estoy funcionando en Railway 🚀")

# Responder mensajes normales
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def main():
    # Crear la aplicación
    app = Application.builder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Iniciar bot
    print("Bot iniciado 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
