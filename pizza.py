from main import *
import telebot
from telebot import types

bot = telebot.TeleBot('5322324188:AAGsEpCEQCFR9DtI6bN6fv0f3CNPDCadEMk')


""" обработка гарниры """
def main_pizza(call):
    if call.data == 'pizza_1':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='pizza')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/1962206/7c65241075444f9aaff915eee3636edf/450x300',
                        caption="Большая пицца Вилларибо\n 1 150 ₽\n\tОписание:\n Говядина, бекон, томатный соус, моцарелла, лук красный, перец болгарский, соус барбекю, лук фри (36 см)",
                        reply_markup=markup_inl)
    if call.data == 'pizza_2':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='pizza')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3504598/a8c825da391b49cebacd8a82794dd271/450x300',
                        caption="Большая пицца Маргарита\n 890 ₽\n\tОписание:\n Тесто, томатный соус, моцарелла (36 см)",
                        reply_markup=markup_inl)
    if call.data == 'pizza_3':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='pizza')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3512826/21b5957095ca4796b66d409d213af9af/450x300',
                        caption="Большая пицца Mucho Четыре сыра\n 990 ₽\n\tОписание:\n Соус сливочный, сыр маскарпоне, сыр камамбер, сыр дорблю, сыр пармезан (36 см)",
                        reply_markup=markup_inl)
    if call.data == 'pizza_4':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='pizza')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3595156/1948a3b4d2d8407981d30124cb281b10/450x300',
                        caption="Большая пицца Дорблю с говядиной\n 1 450 ₽\n\tОписание:\n Соус блю чиз, рубленая говядина, моцарелла, соус вишневый, лук фри (36 см)",
                        reply_markup=markup_inl)
    if call.data == 'pizza_5':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='pizza')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3772784/fd030daba3584aaa9e863af445e21101/450x300',
                        caption="Пицца Дор Блю с говядиной и сладкой вишней\n 990 ₽\n\tОписание:\n Соус блю чиз, рубленая говядина, моцарелла, соус вишневый, лук фри",
                        reply_markup=markup_inl)
    if call.data == 'pizza_6':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='pizza')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3490902/939a4453b6024070b128fa3b75d4465d/450x300',
                        caption="Пицца Вилларибо\n 750 ₽\n\tОписание:\n Говядина, бекон, томатный соус, моцарелла, лук красный, перец болгарский, соус барбекю, лук фри (28 см)",
                        reply_markup=markup_inl)
    if call.data == 'pizza_7':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='pizza')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3798638/198d51ee8d474e039cea1c38c0868f67/450x300',
                        caption="Пицца Mucho Четыре сыра\n 690 ₽\n\tОписание:\n Соус сливочный, сыр маскарпоне, сыр камамбер, сыр дорблю, сыр пармезан (28 см)",
                        reply_markup=markup_inl)
    if call.data == 'pizza_8':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='pizza')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3502490/0cdb5d0990d6ac7d7c86725acc573676/450x300',
                        caption="Пицца Маргарита\n 550 ₽\n\tОписание:\n Тесто, томатный соус, моцарелла (28 см)",
                        reply_markup=markup_inl)
        