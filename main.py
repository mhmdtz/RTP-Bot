import telebot
import os

# دریافت توکن از متغیر محیطی
API_TOKEN = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(API_TOKEN)

# کاراکتر RLM برای راست‌چین کردن
RLM = '\u200F'

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    rtl_text = RLM + message.text
    bot.reply_to(message, rtl_text)

# اجرای مداوم ربات
bot.polling(non_stop=True)
