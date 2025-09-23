from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "AQUI_VA_TU_TOKEN"  # Reemplaza con tu token del BotFather

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot en Railway 🚀")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
