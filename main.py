import telebot
import os
import time

API_TOKEN = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(API_TOKEN)
RLM = '\u200F'

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    rtl_text = RLM + message.text
    try:
        bot.reply_to(message, rtl_text)
    except Exception as e:
        print("Error sending message:", e)

# اجرای ربات با تلاش مجدد
while True:
    try:
        bot.polling(non_stop=True)
    except Exception as e:
        print("Polling error:", e)
        time.sleep(5)
