import telebot
from telebot import types

bot = telebot.TeleBot('5322324188:AAGsEpCEQCFR9DtI6bN6fv0f3CNPDCadEMk')

@bot.message_handler(commands=['start'])
def start_comand(message):
    markup = types.InlineKeyboardMarkup()
    bt1 = types.InlineKeyboardButton(text='y', callback_data='yes')
    bt2 = types.InlineKeyboardButton(text='n', callback_data='no')
    markup.add(bt1, bt2)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=markup)

@bot.message_handler(commands=['help'])
def main():
    pass


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'yes':
        pass


if __name__ == "__main__":
    bot.polling(none_stop = True)
