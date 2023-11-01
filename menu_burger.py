from main import *
import telebot
from telebot import types

bot = telebot.TeleBot('5322324188:AAGsEpCEQCFR9DtI6bN6fv0f3CNPDCadEMk')


""" обработка гарниры """
def main_burger(call):
    if call.data == 'burgers_1':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='burgers')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3506707/b179ae525b8a45fa973e6b8dbe2fb64b/450x300',
                                            caption="Бургер Чикен карри\n 550 ₽\n \t Описание: \nБулочка, куриный шницель, помидор, огурец маринованный, салат айсберг, соус карри", 
                                                reply_markup=markup_inl)
    if call.data == 'burgers_2':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='burgers')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3550919/20c3883c418ca60b80f8f98a8b620a40/450x300',
                                            caption="Бургер Чизбургер\n 530 ₽\n \t Описание: "
                                               "\nБулочка белая, котлета говяжья, сыр чеддер, помидоры свежие, огурцы маринованные, лук красный, кетчуп, соус горчичный. Добавки по желанию", 
                                                reply_markup=markup_inl)
    if call.data == 'burgers_3':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='burgers')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3798638/946cf92156564d67b55d65eaea5b0cc5/450x300',
                                            caption="Бургер Mucho с соусом Бурбон\n 750 ₽\n \t Описание: \nБулочка белая, котлета говяжья, сыр чеддер, бекон, корн-салат, соус бурбон, кетчуп, горчица дижонская", 
                                                reply_markup=markup_inl)
    if call.data == 'burgers_4':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='burgers')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3805363/01b5cdf5462f56eef700bbd46241a5fe/450x300',
                                            caption="Бургер с ростбифом\n 700 ₽\n \t Описание: \nБулочка белая, ростбиф, сыр моцарелла, перец болгарский, лук красный, соус сливочный гриль, соус барбекю", 
                                                reply_markup=markup_inl)
    if call.data == 'burgers_5':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='burgers')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3401132/edd5cd9c80536afe4516e923d1efb03e/450x300',
                                            caption="Бургер Дочь Монтесумы\n 630 ₽\n \t Описание: \nБулочка белая, котлета говяжья, сыр дорблю, соус брусничный, соус горчичный, лук-фри", 
                                                reply_markup=markup_inl)
    if call.data == 'burgers_6':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='burgers')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3208959/e7512cbad95645d598bc9c4bb7db8132/450x300',
                                            caption="Тако бургер\n 610 ₽\n \t Описание: \nГовяжья котлета, сыр чеддер, соус гуакамоле, соус сальса, помидоры, лук красный, сырная тортилья, халапеньо", 
                                                reply_markup=markup_inl)
    