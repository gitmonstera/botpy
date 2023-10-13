import telebot
from telebot import types


bot = telebot.TeleBot('5322324188:AAGsEpCEQCFR9DtI6bN6fv0f3CNPDCadEMk')

@bot.message_handler(commands=['start'])
def start_comand(message):
    markup_rep = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt_about_ = types.KeyboardButton("О нас")
    bt_catalog_ = types.KeyboardButton("Каталог")
    bt_reviews_ = types.KeyboardButton("Отзывы")
    bt_foto_ = types.KeyboardButton("Фото")
    bt_contacts_ = types.KeyboardButton("Контакты")
    markup_rep.add(bt_about_, bt_catalog_, bt_reviews_, bt_foto_, bt_contacts_)
    bot.send_message(message.chat.id,
    f'Привет, {message.from_user.first_name}. Бот ресторана Mucho рад видеть тебя если у вас возникнут какие-либо проблемы - /help',
    reply_markup=markup_rep)

@bot.message_handler(commands=['help'])
def help(message):
    markup_inl = types.InlineKeyboardMarkup()
    bt_tg_connect_ = types.InlineKeyboardButton("связь в телеграме", url='https://t.me/MUCHO_REST')
    markup_inl.add(bt_tg_connect_)
    bot.send_message(message.chat.id, 'Возникли проблемы обращайтесь', reply_markup=markup_inl)


if __name__ == "__main__":
    bot.polling(none_stop = True)
