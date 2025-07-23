import telebot
from telebot import types

# Замените на ваш токен от BotFather
TOKEN = "8060277478:AAHvva3J3Rf85gkOz5st7BmUkGvWGdF9cRU"

bot = telebot.TeleBot(TOKEN)

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

if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
