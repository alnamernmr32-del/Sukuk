import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلا بك في منصة صكوك نجم 🌟\n"
        "اكتب /pay للاشتراك\n"
        "الدفع ون كاش: 783022917"
    )

async def pay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أرسل صورة تحويل ون كاش هنا")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pay", pay))
    app.run_polling()

if __name__ == "__main__":
    main()