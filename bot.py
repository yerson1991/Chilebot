from telegram.ext import Application, CommandHandler

TOKEN = "8373537941:AAFnP7UcsMI4-VvU7EfoabospT4uxnEIHfQ"

async def start(update, context):
    await update.message.reply_text("¡Hola! Soy tu ChileBot, ya estoy funcionando ✅")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
