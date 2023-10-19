from main import *
import telebot
from telebot import types

bot = telebot.TeleBot('5322324188:AAGsEpCEQCFR9DtI6bN6fv0f3CNPDCadEMk')


""" обработка горячих блюд """
def main_hot_dishes(call):
    if call.data == 'hot_dishes_1':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='hot_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3580810/42c04e52a70fe3a8dcef403ba5dbc58e/450x300',
                        caption="Ребра по-мексикански\n 890 ₽\n \t Описание: \nСвиные ребра в азиатском соусе",
                        reply_markup=markup_inl)
    if call.data == 'hot_dishes_2':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='hot_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3512826/16611f9d98263bca34ede6dd43147563/450x300',
                        caption="Голень индейки с брусничным соусом\n 940 ₽\n \t Описание: \nС мини-картофелем и брусничным соусом",
                        reply_markup=markup_inl)
    if call.data == 'hot_dishes_3':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='hot_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3531870/4e993cabcffa443e822007f5ee0f8800/450x300',
                        caption="Мексиканский сет Карне асада\n 3 900 ₽\n \t Описание: \nСтейк фланк (400 г), "
                                    "тортилья (100 г), гуакамоле (80 г), халапеньо (40 г), соус сальса (20 г), перец гриль (40 г)",
                        reply_markup=markup_inl)
    if call.data == 'hot_dishes_4':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='hot_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3724421/be26c9244db34a3e9a197c615867f257/450x300',
                        caption="Фахитос\n 750 ₽\n \t Описание: \nГовяжья вырезка, перец болгарский, лук репчатый, помидоры, острый перец чили, кинза",
                        reply_markup=markup_inl)
    if call.data == 'hot_dishes_5':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='hot_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/1380157/ac07df3943ede0f4cd971d50ee3afa6e/450x300',
                        caption="Бефстроганов с картофельным пюре\n 790 ₽\n \t Описание: \nЛук, говяжья вырезка, шампиньоны, сметана, сливки, картофельное пюре",
                        reply_markup=markup_inl)
    if call.data == 'hot_dishes_6':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='hot_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3507285/a1db984e912141b3b4ff969c677ff9ae/450x300',
                        caption="Запеченный батат с яйцом пашот и ростбифом\n 890 ₽",
                        reply_markup=markup_inl)
    if call.data == 'hot_dishes_7':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='hot_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3525402/aae44dd62bf6417a80e7c8439c0ef0f7/450x300',
                        caption="Стейк из лосося со шпинатом\n 1 150 ₽\n \t Описание: \nЛосось, припущенный шпинат, оливковое масло, лимон",
                        reply_markup=markup_inl)
    if call.data == 'hot_dishes_8':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='hot_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3528150/e02c0482303e482094949c7c45fbcb4d/450x300',
                        caption="Чили кон Карне\n 690 ₽\n \t Описание: \nОстрое мексиканское блюдо из говядины с овощами, фасолью,"
                        " на томатной основе с перцем халапеньо. Подается с сыром чеддер и сырной тортильей",
                        reply_markup=markup_inl)
    if call.data == 'hot_dishes_9':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='hot_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/2353725/30c7d4bf9ed3b4c0bfcf5be168ffbbf5/450x300',
                        caption="Дабл бифштекс с картофелем фри\n 800 ₽\n \t Описание: \nКотлеты бифштекс (2 шт.) с глазуньей и картофелем фри",
                        reply_markup=markup_inl)

