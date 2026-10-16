import telebot, os
from flask import Flask
import threading

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 8331973941
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "⭐ أهلا بك في صكوك نجم\n\nالاستثمار بالنجوم فقط\nالحد الأدنى 1000 نجمة\n\nأرسل عدد النجوم التي تريد شراءها (مثال: 1000)")

@bot.message_handler(func=lambda m: True)
def all_msg(m):
    try:
        n = int(m.text)
        if n < 1000:
            bot.send_message(m.chat.id, "❌ الحد الأدنى 1000 نجمة")
            return
        bot.send_message(ADMIN_ID, f"⭐ عميل جديد\n\n👤 {m.from_user.first_name}\n🆔 @{m.from_user.username}\nID: {m.from_user.id}\n⭐ طلب: {n} نجمة\n💰 {n} ريال")
        bot.send_message(m.chat.id, f"✅ تم تسجيل طلبك {n} نجمة\nسيتواصل معك @N_j_m9")
    except:
        bot.send_message(m.chat.id, "أرسل رقم فقط مثل: 1000")

@app.route('/')
def home(): return "Bot @SukukNjm_bot Running"
def run(): app.run(host='0.0.0.0', port=int(os.getenv("PORT", 8080)))
threading.Thread(target=run).start()
bot.infinity_polling()
