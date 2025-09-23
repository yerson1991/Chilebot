import os
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("TOKEN")  # Toma el token desde Railway

async def start(update, context):
    await update.message.reply_text("👋 Hola! Soy tu Chilebot funcionando al 100% 🚀")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
