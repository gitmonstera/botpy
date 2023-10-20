from main import *
import telebot
from telebot import types

bot = telebot.TeleBot('5322324188:AAGsEpCEQCFR9DtI6bN6fv0f3CNPDCadEMk')


""" обработка гарниры """
def main_side_dishes(call):
    if call.data == 'side_dishes_1':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='side_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3401132/a0a3469fa1874f608cddd1c3a9c43525/450x300',
                        caption="Картофель батат\n 340 ₽",
                        reply_markup=markup_inl)
    if call.data == 'side_dishes_2':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='side_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/2794391/91a2b763c63745f4bcb077128ff7b28e/450x300',
                        caption="Микс-салат\n 100 ₽\n \t Описание: \nРуккола, айсберг, лолло росса",
                        reply_markup=markup_inl)
    if call.data == 'side_dishes_3':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='side_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3735503/214373e72dbd00203bace62c1c0c0c0e/450x300',
                        caption="Картофель айдахо\n 250 ₽\n \t Описание: \nЖареные картофельные дольки со специями",
                        reply_markup=markup_inl)
    if call.data == 'side_dishes_4':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='side_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3550919/bb57db881ec9e5f49a9fcf653746924c/450x300',
                        caption="Кукуруза на гриле\n 250 ₽\n \t Описание: \nПочаток кукурузы на гриле",
                        reply_markup=markup_inl)
    if call.data == 'side_dishes_5':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='side_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/1387779/b713e8d39941386b868d4f3925d5cb93/450x300',
                        caption="Картофель фри\n 240 ₽\n \t Описание: \nОбжаренный во фритюрном масле",
                        reply_markup=markup_inl)
    if call.data == 'side_dishes_6':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='side_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3781088/cbaf2838511d4c7e8e7fc5c550a82647/450x300',
                        caption="Овощи гриль\n 390 ₽\n \t Описание: \nБолгарский перец красный и зеленый, лук, помидор, цукини",
                        reply_markup=markup_inl)
    if call.data == 'side_dishes_7':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='side_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3807631/f313960597c864dc1d9b046d5155d004/450x300',
                        caption="Зеленая фасоль\n 250 ₽\n \t Описание: \nС оливковым маслом и чесноком",
                        reply_markup=markup_inl)
    if call.data == 'side_dishes_8':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='side_dishes')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3781088/1e8374f083a561972bdc66df26f434d6/450x300',
                        caption="Картофельное пюре с чеддером и крошкой бекона\n 250 ₽\n \t Описание: \nКартофельное пюре, сыр Чеддер, хрустящая крошка бекона",
                        reply_markup=markup_inl)
                
