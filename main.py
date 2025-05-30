import telebot
from telebot import types
import time

API_TOKEN = "7589231796:AAFeFZ9oLsFFHSU8kqejxT4kXHQy-mDMnIc"
bot = telebot.TeleBot(API_TOKEN)
RLM = '\u200F'

# مرحله اول: دستور /start و درخواست متن
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "لطفا متن خود را ارسال کنید:")

# مرحله دوم: دریافت متن و ارسال دکمه برای ارسال راست‌چین
@bot.message_handler(func=lambda m: True)
def get_text_and_show_button(message):
    # متن دریافتی
    user_text = message.text
    # ذخیره متن در یه فیلد (برای ساده بودن اینجا داخل خود فانکشن ذخیره می‌کنیم)
    # اگر میخوای متن رو ذخیره کنی، باید از دیتابیس یا دیکشنری استفاده کنی (اختیاری)
    
    # ساخت دکمه
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    send_button = types.KeyboardButton("ارسال متن راست‌چین شده")
    markup.add(send_button)
    
    # ذخیره متن به صورت ساده داخل متغیر در خود بات نیست،  
    # پس برای نمونه، متن رو مستقیم داخل متغیر global می‌ذاریم:
    global last_text
    last_text = user_text
    
    bot.send_message(message.chat.id, "روی دکمه زیر بزن تا متن راست‌چین‌شده ارسال بشه:", reply_markup=markup)

# مرحله سوم: وقتی دکمه زده شد، متن راست‌چین ارسال می‌شه
@bot.message_handler(func=lambda m: m.text == "ارسال متن راست‌چین شده")
def send_rtl_text(message):
    global last_text
    if last_text:
        rtl_text = RLM + last_text
        bot.send_message(message.chat.id, rtl_text)
    else:
        bot.send_message(message.chat.id, "متنی برای ارسال وجود ندارد. لطفا اول یک متن بفرستید.")

# اجرای ربات با تلاش مجدد
while True:
    try:
        bot.polling(non_stop=True)
    except Exception as e:
        print("خطای polling:", e)
        time.sleep(5)
