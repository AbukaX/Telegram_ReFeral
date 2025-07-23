from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Кнопки
keyboard = [["Реферал", "Отмена"]]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Выберите действие:", reply_markup=reply_markup)

# Обработка кнопок
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Реферал":
        await update.message.reply_text("Реферал")
    elif text == "Отмена":
        await update.message.reply_text("Клавиатура скрыта", reply_markup=ReplyKeyboardRemove())

# Основной запуск
async def main():
    app = Application.builder().token("ТВОЙ_ТОКЕН_БОТА").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await app.run_polling()

# Запуск
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

