import telebot
from decouple import config


token = config('TOKEN')

# стикеры
yes_sticker = 'CAACAgIAAxkBAAEIBZdkBYdNUQeQJ6ChZ2cOPL3u5C4SrAACAQADwDZPExguczCrPy1RLgQ'
no_sticker = 'CAACAgIAAxkBAAEIBZdkBYdNUQeQJ6ChZ2cOPL3u5C4SrAACAQADwDZPExguczCrPy1RLgQ'
bot = telebot.TeleBot(token)

#klaviatuers
Keyboard = telebot.types.InlineKeyboardMarkup()
b1 = telebot.types.InlineKeyboardButton('да', callback_data='yes')
b1 = telebot.types.InlineKeyboardButton('нет', callback_data='no')
Keyboard.add(b1, b2)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'привет выбери кнопку', reply_markup=keyboard())
# func - функция фильтр в данном случае разрешаются все сооб

@bot.callback_query_handler(func=lambda x: True)
def reply_to_button(call):
    if call.data == 'yes':
        bot.send_sticker(call.from_user.id, yes_sticker)
    elif call.data == 'no':
        bot.send_sticker(call.from_user.id, no_sticker)


bot.polling()


