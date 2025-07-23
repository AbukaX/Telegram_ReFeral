import telebot
from telebot import types
import os
from flask import Flask
import threading

# Получаем токен из переменной окружения или используем заглушку
TOKEN = os.environ.get('TOKEN', '8060277478:AAHvva3J3Rf85gkOz5st7BmUkGvWGdF9cRU')

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(message):
    # Создаем клавиатуру с кнопками
    keyboard = types.InlineKeyboardMarkup()
    
    # Добавляем кнопки
    referral_button = types.InlineKeyboardButton("Реферал", callback_data="referral")
    cancel_button = types.InlineKeyboardButton("Отмена", callback_data="cancel")
    
    keyboard.add(referral_button, cancel_button)
    
    bot.send_message(
        message.chat.id, 
        "Выберите действие:", 
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "referral":
        # При нажатии на "Реферал" отправляем сообщение
        bot.send_message(call.message.chat.id, "реферал")
        
        # Удаляем кнопки (редактируем сообщение без клавиатуры)
        bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None
        )
        
    elif call.data == "cancel":
        # При нажатии на "Отмена" закрываем кнопки
        bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None
        )
        
        # Опционально: отправляем сообщение об отмене
        bot.send_message(call.message.chat.id, "Действие отменено")

# Простой веб-сервер для Render
@app.route('/')
def health_check():
    return "Бот работает! 🤖"

@app.route('/status')
def status():
    return {"status": "running", "bot": "active"}

def run_bot():
    """Запуск бота в отдельном потоке"""
    print("Бот запущен...")
    bot.infinity_polling(none_stop=True)

if __name__ == "__main__":
    # Запускаем бота в отдельном потоке
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Запускаем Flask для Render (Web Service)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
