import telebot
from telebot import types

from menu_zac import *
from menu_hot_dishes import *
from menu_sauces import *
from menu_side_dishes import *
from menu_salads import *
from menu_burger import *
from childrens_menu import *
from pizza import *
from soup import *
from other import *


bot = telebot.TeleBot('5322324188:AAGsEpCEQCFR9DtI6bN6fv0f3CNPDCadEMk')

@bot.message_handler(commands=['start'])
def start_comand(message):
    markup_rep = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt_about_ = types.KeyboardButton("О нас")
    bt_catalog_ = types.KeyboardButton("Меню")
    bt_reviews_ = types.KeyboardButton("Отзывы")
    bt_foto_ = types.KeyboardButton("Фото")
    bt_contacts_ = types.KeyboardButton("Контакты")
    markup_rep.add(bt_about_, bt_catalog_, bt_reviews_, bt_foto_, bt_contacts_)
    bot.send_message(message.chat.id,
    f'Привет, {message.from_user.first_name}. Бот ресторана Mucho рад видеть тебя.',
    reply_markup=markup_rep)

@bot.message_handler(commands=['help'])
def help(message):
    markup_inl = types.InlineKeyboardMarkup()
    bt_tg_connect_ = types.InlineKeyboardButton("связь в телеграме", url='https://t.me/MUCHO_REST')
    markup_inl.add(bt_tg_connect_)
    bot.send_message(message.chat.id, 'Возникли проблемы обращайтесь или звоните по телефону  +7(925)562-61-64', reply_markup=markup_inl)


""" обработчик команд с шлавного меню """
@bot.message_handler(content_types=['text'])
def murkup_replay(message):
    if(message.text == "О нас"):
        markup_inl = types.InlineKeyboardMarkup()
        bt_how_get_there_ = types.InlineKeyboardButton("добраться", url="https://yandex.ru/maps/213/moscow/?from=api-maps&ll=37.509382%2C55.755584&mode=routes&origin=jsapi_2_1_79&rtext=~55.755584%2C37.509382&rtt=auto&ruri=~&z=15")
        markup_inl.add(bt_how_get_there_)
        bot.send_message(message.chat.id, 'О нас',  reply_markup=markup_inl)
    elif(message.text == 'Меню'):
        markup_inl = types.InlineKeyboardMarkup()
        bt_snacks = types.InlineKeyboardButton("Закуски", callback_data='snacks')
        bt_hot_dishes = types.InlineKeyboardButton("Горячие блюда", callback_data='hot_dishes')
        bt_sauces = types.InlineKeyboardButton("Соусы", callback_data='sauces')
        bt_side_dishes = types.InlineKeyboardButton("Гарниры", callback_data='side_dishes')
        bt_salads = types.InlineKeyboardButton("Салаты", callback_data='salads')
        bt_burgers = types.InlineKeyboardButton("Бургеры", callback_data='burgers')
        bt_children_menu = types.InlineKeyboardButton("Детское меню", callback_data='childrens_menu')
        bt_soup_ = types.InlineKeyboardButton("Супы", callback_data='soup')
        bt_desserts_ = types.InlineKeyboardButton("Пицца", callback_data='pizza')
        bt_other_ = types.InlineKeyboardButton("Другое", callback_data='other')
        markup_inl.add(bt_snacks, bt_hot_dishes, bt_sauces, bt_side_dishes, bt_salads,
                        bt_burgers, bt_children_menu, bt_soup_, bt_desserts_,  bt_other_)
        bot.send_message(message.chat.id, '<b>Меню</b>, выбирите тип блюда', parse_mode='html', reply_markup=markup_inl)
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
        markup_inl = types.InlineKeyboardMarkup(row_width=1)
        bt_tg_connect_ = types.InlineKeyboardButton("связь в телеграме", url='https://t.me/MUCHO_REST')
        bt_sayt_connect_ = types.InlineKeyboardButton("Наш сайт", url='https://mucho.clients.site/')
        markup_inl.add(bt_tg_connect_, bt_sayt_connect_)
        bot.send_message(message.chat.id, 'Возникли проблемы обращайтесь или звоните нам по телефону: +7(925)562-61-64', reply_markup=markup_inl)

    else:
        bot.send_message(message.chat.id, 'извените, но я вас не понимаю /help')


""" обработчик команд Меню """
@bot.callback_query_handler(func=lambda call:True)
def menu_(call):
    """ Закуски """
    if call.data == 'snacks':
        markup_inl = types.InlineKeyboardMarkup(row_width=1)
        bt_zac_2 = types.InlineKeyboardButton('Начос с соусами', callback_data='zac_2')
        bt_zac_3 = types.InlineKeyboardButton('Брускетта с ростбифом и соусом манго-чили', callback_data='zac_3')
        bt_zac_4 = types.InlineKeyboardButton('Брускетта с тартаром из лосося и авокадо', callback_data='zac_4')
        bt_zac_5 = types.InlineKeyboardButton('Брускетта с тартаром из лосося и клубники', callback_data='zac_5')
        bt_zac_6 = types.InlineKeyboardButton('Кесадилья с мясом', callback_data='zac_6')
        bt_zac_7 = types.InlineKeyboardButton('Пикантные крылья Баффало', callback_data='zac_7')
        bt_zac_8 = types.InlineKeyboardButton('Гренки ржаные', callback_data='zac_8')
        bt_zac_9 = types.InlineKeyboardButton('Кесадилья с грушей и горгонзолой', callback_data='zac_9')
        bt_zac_10 = types.InlineKeyboardButton('Сырные палочки с брусничным соусом', callback_data='zac_10')
        bt_zac_11 = types.InlineKeyboardButton('Хрустящие креветки со Сладким чили', callback_data='zac_11')
        bt_zac_13 = types.InlineKeyboardButton('Тако с ростбифом', callback_data='zac_13')
        bt_zac_14 = types.InlineKeyboardButton('Буррито с говядиной', callback_data='zac_14')
        bt_zac_15 = types.InlineKeyboardButton('Тако с курицей и сладким чили', callback_data='zac_15')
        markup_inl.add( bt_zac_2, bt_zac_3, bt_zac_4, bt_zac_5, bt_zac_6, bt_zac_7,
                        bt_zac_8, bt_zac_9, bt_zac_10, bt_zac_11, bt_zac_13, bt_zac_14, bt_zac_15)
        bot.send_message(call.message.chat.id, 'Выберите блюдо, что бы узнать о нем подробнее', reply_markup=markup_inl)

    """ горячие блюда """
    if call.data == 'hot_dishes':
        markup_inl = types.InlineKeyboardMarkup(row_width=1)
        bt_hot_dishes_1 = types.InlineKeyboardButton('Ребра по-мексикански', callback_data='hot_dishes_1')
        bt_hot_dishes_2 = types.InlineKeyboardButton('Голень индейки с брусничным соусом', callback_data='hot_dishes_2')
        bt_hot_dishes_3 = types.InlineKeyboardButton('Мексиканский сет Карне асада', callback_data='hot_dishes_3')
        bt_hot_dishes_4 = types.InlineKeyboardButton('Фахитос', callback_data='hot_dishes_4')
        bt_hot_dishes_5 = types.InlineKeyboardButton('Бефстроганов с картофельным пюре', callback_data='hot_dishes_5')
        bt_hot_dishes_6 = types.InlineKeyboardButton('Запеченный батат с яйцом пашот и  ростбифом', callback_data='hot_dishes_6')
        bt_hot_dishes_7 = types.InlineKeyboardButton('Стейк из лосося со шпинатом', callback_data='hot_dishes_7')
        bt_hot_dishes_9 = types.InlineKeyboardButton('Дабл бифштекс с картофелем фри', callback_data='hot_dishes_9')
        markup_inl.add(bt_hot_dishes_1, bt_hot_dishes_2, bt_hot_dishes_3, bt_hot_dishes_4, bt_hot_dishes_5,
                        bt_hot_dishes_6, bt_hot_dishes_7, bt_hot_dishes_9)
        bot.send_message(call.message.chat.id, 'Выберите блюдо, что бы узнать о нем подробнее', reply_markup=markup_inl)

    """ соусы """
    if call.data == 'sauces':
        markup_inl = types.InlineKeyboardMarkup(row_width=1)
        bt_sauces_1 = types.InlineKeyboardButton('Соус BBQ', callback_data='sauces_1')
        bt_sauces_2 = types.InlineKeyboardButton('Соус Ягодный', callback_data='sauces_2')
        bt_sauces_3 = types.InlineKeyboardButton('Соус Блю чиз', callback_data='sauces_3')
        bt_sauces_4 = types.InlineKeyboardButton('Соус Чесночный', callback_data='sauces_4')
        bt_sauces_5 = types.InlineKeyboardButton('Соус сладкий чили', callback_data='sauces_5')
        bt_sauces_6 = types.InlineKeyboardButton('Соус Перечный', callback_data='sauces_6')
        bt_sauces_7 = types.InlineKeyboardButton('Фирменный соус Mucho', callback_data='sauces_7')
        bt_sauces_8 = types.InlineKeyboardButton('Соус сырный', callback_data='sauces_8')
        bt_sauces_9 = types.InlineKeyboardButton('Кетчуп', callback_data='sauces_9')
        markup_inl.add(bt_sauces_1, bt_sauces_2, bt_sauces_3, bt_sauces_4, bt_sauces_5,
                        bt_sauces_6, bt_sauces_7, bt_sauces_8, bt_sauces_9)
        bot.send_message(call.message.chat.id, 'Выберите блюдо, что бы узнать о нем подробнее', reply_markup=markup_inl)

    """ гарнир """
    if call.data == 'side_dishes':
        markup_inl = types.InlineKeyboardMarkup(row_width=1)
        bt_side_dishes_1 = types.InlineKeyboardButton('Картофель батат', callback_data='side_dishes_1')
        bt_side_dishes_2 = types.InlineKeyboardButton('Микс-салат', callback_data='side_dishes_2')
        bt_side_dishes_3 = types.InlineKeyboardButton('Картофель айдахо', callback_data='side_dishes_3')
        bt_side_dishes_4 = types.InlineKeyboardButton('Кукуруза на гриле', callback_data='side_dishes_4')
        bt_side_dishes_5 = types.InlineKeyboardButton('Картофель фри', callback_data='side_dishes_5')
        bt_side_dishes_6 = types.InlineKeyboardButton('Овощи гриль', callback_data='side_dishes_6')
        bt_side_dishes_7 = types.InlineKeyboardButton('Зеленая фасоль', callback_data='side_dishes_7')
        bt_side_dishes_8 = types.InlineKeyboardButton('Картофельное пюре с чеддером и крошкой бекона', callback_data='sauces_8')
        markup_inl.add(bt_side_dishes_1, bt_side_dishes_2, bt_side_dishes_3, bt_side_dishes_4, bt_side_dishes_5,
                        bt_side_dishes_6, bt_side_dishes_7, bt_side_dishes_8)
        bot.send_message(call.message.chat.id, 'Выберите блюдо, что бы узнать о нем подробнее', reply_markup=markup_inl)

    """ салаты """
    if call.data == 'salads':
        markup_inl = types.InlineKeyboardMarkup(row_width=1)
        bt_salads_1 = types.InlineKeyboardButton('Зеленый салат с авокадо и гравлаксом', callback_data='salads_1')
        bt_salads_2 = types.InlineKeyboardButton('Салат с печенью и апельсином', callback_data='salads_2')
        bt_salads_3 = types.InlineKeyboardButton('Салат с хрустящими баклажанами и страчателлой', callback_data='salads_3')
        bt_salads_4 = types.InlineKeyboardButton('Салат Фермерский', callback_data='salads_4')
        bt_salads_5 = types.InlineKeyboardButton('Салат Кобб', callback_data='salads_5')
        bt_salads_6 = types.InlineKeyboardButton('Салат Цезарь с креветками', callback_data='salads_6')
        bt_salads_7 = types.InlineKeyboardButton('Салат Цезарь с курицей', callback_data='salads_7')
        bt_salads_8 = types.InlineKeyboardButton('Салат греческий', callback_data='salads_8')
        markup_inl.add(bt_salads_1, bt_salads_2, bt_salads_3, bt_salads_4, bt_salads_5,
                        bt_salads_6, bt_salads_7, bt_salads_8)
        bot.send_message(call.message.chat.id, 'Выберите блюдо, что бы узнать о нем подробнее', reply_markup=markup_inl)

    """ Бургеры """
    if call.data == 'burgers':
        markup_inl = types.InlineKeyboardMarkup(row_width=1)
        bt_burgers_1 = types.InlineKeyboardButton('Бургер чикен карри', callback_data='burgers_1')
        bt_burgers_2 = types.InlineKeyboardButton('Бургер чизбургер', callback_data='burgers_2')
        bt_burgers_3 = types.InlineKeyboardButton('Бургер Mucho с соусом Бурбон', callback_data='burgers_3')
        bt_burgers_4 = types.InlineKeyboardButton('Бургер с ростбифом', callback_data='burgers_4')
        bt_burgers_5 = types.InlineKeyboardButton('Бургер Дочь Монтесумы', callback_data='burgers_5')
        bt_burgers_6 = types.InlineKeyboardButton('Бургер тако', callback_data='burgers_6')
        markup_inl.add(bt_burgers_1, bt_burgers_2, bt_burgers_3, bt_burgers_4, bt_burgers_5, bt_burgers_6)
        bot.send_message(call.message.chat.id, 'Выберите блюдо, что бы узнать о нем подробнее', reply_markup=markup_inl)

    """ Детское меню """
    if call.data == 'childrens_menu':
        markup_inl = types.InlineKeyboardMarkup(row_width=1)
        bt_childrens_menu_1 = types.InlineKeyboardButton('Пицца Маргоша', callback_data='childrens_menu_1')
        bt_childrens_menu_2 = types.InlineKeyboardButton('Ушастый чиз', callback_data='childrens_menu_2')
        bt_childrens_menu_3 = types.InlineKeyboardButton('Куриная котлета с пюре', callback_data='childrens_menu_3')
        bt_childrens_menu_4 = types.InlineKeyboardButton('Молочный коктель', callback_data='childrens_menu_4')
        bt_childrens_menu_5 = types.InlineKeyboardButton('Макарошки с сыром', callback_data='childrens_menu_5')
        bt_childrens_menu_6 = types.InlineKeyboardButton('Курочка в панировке с йогуртовым соусом', callback_data='childrens_menu_6')
        markup_inl.add(bt_childrens_menu_1, bt_childrens_menu_2, bt_childrens_menu_3, bt_childrens_menu_4, bt_childrens_menu_5, bt_childrens_menu_6)
        bot.send_message(call.message.chat.id, 'Выберите блюдо, что бы узнать о нем подробнее', reply_markup=markup_inl)

    """ Супы """
    if call.data == 'soup':
        markup_inl = types.InlineKeyboardMarkup(row_width=1)
        bt_soup_1 = types.InlineKeyboardButton('Кукурузный крем-суп с беконом', callback_data='soup_1')
        bt_soup_2 = types.InlineKeyboardButton('Кукурузный крем-суп с креветкой', callback_data='soup_2')
        bt_soup_3 = types.InlineKeyboardButton('Крем-суп грибной', callback_data='soup_3')
        bt_soup_4 = types.InlineKeyboardButton('Мексиканский суп с креветками', callback_data='soup_4')
        bt_soup_5 = types.InlineKeyboardButton('Легкий куриный суп', callback_data='soup_5')
        bt_soup_6 = types.InlineKeyboardButton('Мексиканский мясной суп с фасолью', callback_data='soup_6')
        markup_inl.add(bt_soup_1, bt_soup_2, bt_soup_3, bt_soup_4, bt_soup_5, bt_soup_6)
        bot.send_message(call.message.chat.id, 'Выберите блюдо, что бы узнать о нем подробнее', reply_markup=markup_inl)

    """ Пицца """
    if call.data == 'pizza':
        markup_inl = types.InlineKeyboardMarkup(row_width=1)
        bt_pizza_1 = types.InlineKeyboardButton('Большая пицца Вилларибо', callback_data='pizza_1')
        bt_pizza_2 = types.InlineKeyboardButton('Большая пицца Маргарита', callback_data='pizza_2')
        bt_pizza_3 = types.InlineKeyboardButton('Большая пицца Mucho Четыре сыра', callback_data='pizza_3')
        bt_pizza_4 = types.InlineKeyboardButton('Большая пицца Дорблю с говядиной', callback_data='pizza_4')
        bt_pizza_5 = types.InlineKeyboardButton('Пицца Дорблю с говядиной и сладкой вишней', callback_data='pizza_5')
        bt_pizza_6 = types.InlineKeyboardButton('Пицца Вилларибо', callback_data='pizza_6')
        bt_pizza_7 = types.InlineKeyboardButton('Пицца Mucho Четыре сыра', callback_data='pizza_7')
        bt_pizza_8 = types.InlineKeyboardButton('Пицца Маргарита', callback_data='pizza_8')
        markup_inl.add(bt_pizza_1, bt_pizza_2, bt_pizza_3, bt_pizza_4, bt_pizza_5, bt_pizza_6, bt_pizza_7, bt_pizza_8)
        bot.send_message(call.message.chat.id, 'Выберите блюдо, что бы узнать о нем подробнее', reply_markup=markup_inl)

    """ Закуски """
    if call.data == 'other':
        markup_inl = types.InlineKeyboardMarkup(row_width=1)
        bt_other_1 = types.InlineKeyboardButton('Лимонад Маракуйя', callback_data='other_1')
        bt_other_2 = types.InlineKeyboardButton('Паста со шпинатом и томленной говядиной', callback_data='other_2')
        bt_other_3 = types.InlineKeyboardButton('Лимонад Мохито клубничный', callback_data='other_3')
        bt_other_4 = types.InlineKeyboardButton('Лимонад Мохито', callback_data='other_4')
        bt_other_5 = types.InlineKeyboardButton('Стейк Мачете', callback_data='other_5')
        bt_other_6 = types.InlineKeyboardButton('Стейк Стриплойн', callback_data='other_6')
        bt_other_7 = types.InlineKeyboardButton('Шоколадный флан', callback_data='other_7')
        bt_other_8 = types.InlineKeyboardButton('Фланк', callback_data='other_8')
        bt_other_9 = types.InlineKeyboardButton('Морс ягодный домашний', callback_data='other_9')
        bt_other_10 = types.InlineKeyboardButton('Стейк филе миньон', callback_data='other_10')
        bt_other_11 = types.InlineKeyboardButton('Свежевыжатый сок', callback_data='other_11')
        bt_other_12 = types.InlineKeyboardButton('Стейк Рибай', callback_data='other_12')
        bt_other_13 = types.InlineKeyboardButton('Паста пенне Арабьята', callback_data='otherother_13')
        bt_other_14 = types.InlineKeyboardButton('Тальятелле Болоньезе', callback_data='other_14')
        markup_inl.add(bt_other_1, bt_other_2, bt_other_3, bt_other_4, bt_other_5, bt_other_6, bt_other_7,
                        bt_other_8, bt_other_9, bt_other_10, bt_other_11, bt_other_12, bt_other_13,
                            bt_other_14)
        bot.send_message(call.message.chat.id, 'Выберите блюдо, что бы узнать о нем подробнее', reply_markup=markup_inl)

    main_zac(call)
    main_hot_dishes(call)
    main_sauces(call)
    main_side_dishes(call)
    main_salads(call)
    main_burger(call)
    main_childrens_menu(call)
    main_pizza(call)
    main_soup(call)
    main_other(call)




if __name__ == "__main__":
    bot.polling(none_stop = True)
