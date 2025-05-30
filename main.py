import telebot
import time

# توکن ربات
API_TOKEN = "7589231796:AAFeFZ9oLsFFHSU8kqejxT4kXHQy-mDMnIc"

bot = telebot.TeleBot(API_TOKEN)
RLM = '\u200F'

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    rtl_text = RLM + message.text
    try:
        bot.reply_to(message, rtl_text)
    except Exception as e:
        print("خطا در ارسال پیام:", e)

# اجرای ربات با تلاش مجدد در صورت خطا
while True:
    try:
        bot.polling(non_stop=True)
    except Exception as e:
        print("خطای polling:", e)
        time.sleep(5)
