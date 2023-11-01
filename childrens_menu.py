from main import *
import telebot
from telebot import types

bot = telebot.TeleBot('5322324188:AAGsEpCEQCFR9DtI6bN6fv0f3CNPDCadEMk')


""" обработка гарниры """
def main_childrens_menu(call):
    if call.data == 'childrens_menu_1':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='childrens_menu')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3378693/95f5bc1f969447b5bd11947482302c29/450x300',
                        caption="Пицца Маргоша\n 550 ₽\n\tОписание:\n Тесто, томатный соус, моцарелла (28 см)",
                        reply_markup=markup_inl)
    if call.data == 'childrens_menu_2':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='childrens_menu')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/2050703/24fa2ee642544c02b896a6bd3542a85f/450x300',
                        caption="Ушастый чиз\n 720 ₽\n\tОписание:\n Булочка, айсберг, чили-майонез, котлета куриная, помидор, фри, огурец маринованный, соус кетчуп с горчицей",
                        reply_markup=markup_inl)
    if call.data == 'childrens_menu_3':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='childrens_menu')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3531870/c529c21ac09344ffa36bc8631663ebe4/450x300',
                        caption="Куриная котлетка с пюре\n 450 ₽\n\tОписание:\n Куриная котлета, картофельное пюре, огурец, помидор черри",
                        reply_markup=markup_inl)
    if call.data == 'childrens_menu_4':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='childrens_menu')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3596693/9814bb1276114ff1a24be423cf03c126/450x300',
                        caption="Молочный коктейль\n 400 ₽\n\tОписание:\n Мороженое, сливки, молоко",
                        reply_markup=markup_inl)
    if call.data == 'childrens_menu_5':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='childrens_menu')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3813301/0dfc40ce477f4830a9bcb3079017e893/450x300',
                        caption="Макарошки с сыром\n 390 ₽\n\tОписание:\n Спагетти, масло сливочное, пармезан",
                        reply_markup=markup_inl)
    if call.data == 'childrens_menu_6':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='childrens_menu')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3580810/d8c80fbaea8a4f2abed28e98cc582973/450x300',
                        caption="Курочка в панировке с йогуртовым соусом\n 390 ₽\n\tОписание:\n Маринованное куриное филе (соль, перец, паприка, яйцо)",
                        reply_markup=markup_inl)
