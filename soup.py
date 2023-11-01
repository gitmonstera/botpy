from main import *
import telebot
from telebot import types

bot = telebot.TeleBot('5322324188:AAGsEpCEQCFR9DtI6bN6fv0f3CNPDCadEMk')


""" обработка гарниры """
def main_soup(call):
    if call.data == 'soup_1':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='soup')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/2050703/a2bbab640ae74878beb4a27da05f437a/450x300',
                        caption="Кукурузный крем-суп с беконом\n 600 ₽\n\tОписание:\n Кукуруза, пюре картофельное, сливки, куркума, кориандр, чеддер, лен, бекон жареный, микрозелень, хлеб для брускетт, масло чесночное",
                        reply_markup=markup_inl)
    if call.data == 'soup_2':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='soup')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3512182/fcdaa094e78b4be881ab142645030d01/450x300',
                        caption="Кукурузный крем-суп с креветкой\n 600 ₽\n\tОписание:\n Кукуруза, пюре картофельное, сливки, куркума, кориандр, чеддер, лен, креветка, микрозелень, хлеб для брускетт, масло чесночное",
                        reply_markup=markup_inl)
    if call.data == 'soup_3':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='soup')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3502490/50b9e3adbc074049a0da6e50d435395e/450x300',
                        caption="Крем-суп грибной\n 390 ₽\n\tОписание:\n Бульон грибной, шампиньоны, лук, сливки, масло трюфельное, молоко, гренки",
                        reply_markup=markup_inl)
    if call.data == 'soup_4':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='soup')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3595156/149a1aa8ad1b4ed981eeb80ca35a7f4b/450x300',
                        caption="Мексиканский суп с креветками\n 600 ₽\n\tОписание:\n Лук репчатый, масло оливковое, бульон куриный, сливки, хлопья чили, зира, кориандр, сметана, кинза, авокадо, вода",
                        reply_markup=markup_inl)
    if call.data == 'soup_5':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='soup')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3490335/6915c784d4a842759f345c541d36104c/450x300',
                        caption="Легкий куриный суп\n 600 ₽\n\tОписание:\n Куриный бульон, куриная грудка, картофель, морковь, зеленый горошек, зелень",
                        reply_markup=markup_inl)
    if call.data == 'soup_6':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='soup')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3507285/5d692fcccc724daab5e6edf1cacd12e6/450x300',
                        caption="Мексиканский мясной суп с фасолью\n 580 ₽\n\tОписание:\n Томатный суп с говядиной, болгарским перцем, луком репчатым, сливками и соком лайма",
                        reply_markup=markup_inl)
