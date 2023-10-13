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


""" обработчик команд с шлавного меню """
@bot.message_handler(content_types=['text', 'photo'])
def murkup_replay(message):
    if(message.text == "О нас"):
        markup_inl = types.InlineKeyboardMarkup()
        bt_how_get_there_ = types.InlineKeyboardButton("добраться", url="https://yandex.ru/maps/213/moscow/?from=api-maps&ll=37.509382%2C55.755584&mode=routes&origin=jsapi_2_1_79&rtext=~55.755584%2C37.509382&rtt=auto&ruri=~&z=15")
        bt_food_delivery_ = types.InlineKeyboardButton(" Доставка еды", callback_data='bt_food_delivery_')
        bt_coffe_ = types.InlineKeyboardButton(" Кофе с собой", callback_data='bt_coffe_')
        bt_food_my_ = types.InlineKeyboardButton(" Еда на вынос", callback_data='bt_food_my_')
        markup_inl.add(bt_how_get_there_, bt_food_delivery_, bt_coffe_, bt_food_my_)
        bot.send_message(message.chat.id, 'О нас',  reply_markup=markup_inl)
    elif(message.text == 'Каталог'):
        markup_inl = types.InlineKeyboardMarkup()
        bt_snacks = types.InlineKeyboardButton("Закуски", callback_data='snacks')
        bt_hot_dishes = types.InlineKeyboardButton("Горячие блюда", callback_data='hot_dishes')
        bt_sauces = types.InlineKeyboardButton("Соусы", callback_data='sauces')
        bt_side_dishes = types.InlineKeyboardButton("Гарниры", callback_data='side_dishes')
        bt_pizza = types.InlineKeyboardButton("Пицца", callback_data='pizza')
        bt_salads = types.InlineKeyboardButton("Салаты", callback_data='salads')
        bt_burgers = types.InlineKeyboardButton("Бургеры", callback_data='burgers')
        bt_desserts = types.InlineKeyboardButton("Десерты", callback_data='desserts')
        bt_children_menu = types.InlineKeyboardButton("Детское меню", callback_data='childrens_menu')
        bt_other = types.InlineKeyboardButton("Другое", callback_data='other')
        markup_inl.add(bt_snacks, bt_hot_dishes, bt_sauces, bt_side_dishes, bt_pizza, bt_salads, bt_burgers, bt_desserts, bt_children_menu, bt_other)
        bot.send_message(message.chat.id, '<b>Каталог</b>, выбирите тип блюда', parse_mode='html', reply_markup=markup_inl)
    elif(message.text == 'Отзывы'):
        markup_inl = types.InlineKeyboardMarkup()
        bt_otzov = types.InlineKeyboardButton("Отзывы", url="https://mucho.clients.site/#rating")
        markup_inl.add(bt_otzov)
        bot.send_message(message.chat.id, 'наши отзыв можно посмотреть тут: ', reply_markup=markup_inl)
    elif(message.text == 'Фото'):
        bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/get-altay/5499862/2a00000182ba83fb925cb7d8d3c029d306b7/L')
        bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/get-altay/7379963/2a0000018400064f51094ae86b568e06e5c6/L')
        bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/get-altay/9728306/2a00000189033096808236417b557011956d/L')
        bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/get-altay/1992662/2a00000184c4c257ba6740c681919911c488/L')
        bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/get-altay/5110793/2a000001810f7944bbed84cf6c8cbc39e95b/L')
        bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/get-altay/4335885/2a00000182ba8871cff17d6f083d0d3ecbfd/L')
        bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/get-altay/1003687/2a00000185c464eb232f76686683005eafdd/L')
        bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/get-altay/6143287/2a0000018359280a74d78f6b012ee12edde5/L')
        bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/get-altay/6487610/2a0000018337d092e2ab6cc180a1cb61454e/L')
        bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/get-altay/4255939/2a00000182ba8820c81b80ce7dc6f0cac322/L')
    elif(message.text == 'Контакты'):
        pass

""" обработчик команд О нас """

if __name__ == "__main__":
    bot.polling(none_stop = True)
