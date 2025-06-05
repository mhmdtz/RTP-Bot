import telebot
from flask import Flask, request, abort

API_TOKEN = "7589231796:AAFeFZ9oLsFFHSU8kqejxT4kXHQy-mDMnIc"
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)
RLM = '\u200F'

# پاسخ به /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "لطفا متن خود را ارسال کنید")

# پاسخ راست‌چین به همه‌ی پیام‌ها
@bot.message_handler(func=lambda m: m.text is not None)
def handle_message(message):
    if message.chat.type in ['private', 'group', 'supergroup']:
        rtl_text = RLM + message.text
        try:
            bot.reply_to(message, rtl_text)
        except Exception as e:
            print("خطا در ارسال پیام:", e)

# پاسخ به inline query
@bot.inline_handler(func=lambda query: True)
def handle_inline_query(inline_query):
    try:
        query_text = inline_query.query
        if not query_text:
            return
        rtl_text = RLM + query_text
        result = telebot.types.InlineQueryResultArticle(
            id='1',
            title="📤 ارسال متن راست‌چین",
            input_message_content=telebot.types.InputTextMessageContent(rtl_text)
        )
        bot.answer_inline_query(inline_query.id, [result])
    except Exception as e:
        print("خطای inline:", e)

# روت برای webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        abort(403)

@app.route('/')
def index():
    return 'Bot is running!'

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
