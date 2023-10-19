from main import *
from telebot import types


""" обработка горячих блюд """
def main_sauces(call):
    if call.data == 'sauces_1':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='sauces')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3208959/a781c2dec5024a989b60e2dfb00c67a1/450x300',
                        caption="Соус BBQ\n 90 ₽",
                        reply_markup=markup_inl)
    if call.data == 'sauces_2':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='sauces')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3559865/d8609e05bccd83d004b3bd795f3d6963/450x300',
                        caption="Соус Ягодный\n 90 ₽\n \t Описание: \nСоус на основе ягод и красного вина",
                        reply_markup=markup_inl)
    if call.data == 'sauces_3':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='sauces')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3784951/b733abf3d587570107ab8927dcdf4662/450x300',
                        caption="Соус Блю чиз\n 90 ₽\n \t Описание: \nСливки, сыр дорблю",
                        reply_markup=markup_inl)
    if call.data == 'sauces_4':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='sauces')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/2806911/60e52e2bb3a15a960f0116cf06e25554/450x300',
                        caption="Соус Чесночный\n 90 ₽\n \t Описание: \nМайонез, чеснок, зелень",
                        reply_markup=markup_inl)
    if call.data == 'sauces_5':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='sauces')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3502728/ee607e5a17217e3d5d7125f2f2d9b3f5/450x300',
                        caption="Соус сладкий чили\n 90 ₽",
                        reply_markup=markup_inl)

