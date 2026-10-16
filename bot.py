import telebot, os
from flask import Flask
import threading

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 8331973941
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "⭐ Sukuk Njm\nMin 1000 stars\nSend number like: 1000")

@bot.message_handler(func=lambda m: True)
def all_msg(m):
    try:
        n = int(m.text)
        if n < 1000:
            bot.send_message(m.chat.id, "Min 1000")
            return
        bot.send_message(ADMIN_ID, f"⭐ NEW ORDER\nName: {m.from_user.first_name}\nUser: @{m.from_user.username}\nID: {m.from_user.id}\nStars: {n}")
        bot.send_message(m.chat.id, f"✅ Order {n} saved, admin @N_j_m9 will contact")
    except:
        bot.send_message(m.chat.id, "Send number only: 1000")

@app.route('/')
def home():
    return "Bot Running"
def run():
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 8080)))
threading.Thread(target=run).start()
bot.infinity_polling()
