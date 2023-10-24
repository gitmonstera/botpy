from main import *
import telebot
from telebot import types

bot = telebot.TeleBot('5322324188:AAGsEpCEQCFR9DtI6bN6fv0f3CNPDCadEMk')


""" обработка гарниры """
def main_salads(call):
    if call.data == 'salads_1':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='salads')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_message(call.message.chat.id, "Зеленый салат с авокадо и гравлаксом\n 650 ₽\n \t Описание: "
                                               "\nРуккола, айсберг, лолло россаМикс салата, огурец, фасоль стручковая, чили свежий, авокадо, семга гравлакс, "
                                               "соль, масло оливковое, лен, кунжут, масло кунжутное", reply_markup=markup_inl)
    if call.data == 'salads_2':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='salads')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/2796335/4048caa060494ccfbdbc4210cf800b9b/450x300',
                        caption="Салат с печенью и апельсином\n 690 ₽\n \t Описание: \nПечень куриная, микс-салат, сливки, вино, чеснок, апельсин, мед, оливковое масло",
                        reply_markup=markup_inl)
    if call.data == 'salads_3':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='salads')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/1962206/9dd87cf8304e4dc4976b0e0b6bf6c5a5/450x300',
                        caption="Салат с хрустящими баклажанами и страчателлой\n 550 ₽\n \t Описание: \nБаклажан, помидор, соус чили сладкий, страчателла, кинза, грецкий орех",
                        reply_markup=markup_inl)
    if call.data == 'salads_4':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='salads')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3735503/0d54153820334480b8fd3c3e88f43597/450x300',
                        caption="Салат Фермерский\n 590 ₽\n \t Описание: \nКурица запеченная маринованная, сладкий перец, два вида фасоли (зеленая и красная), лук красный, помидоры черри, чесночный соус, лолло россо, грецкий орех, картофель айдахо, пшеничная тортилья",
                        reply_markup=markup_inl)
    if call.data == 'salads_5':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='salads')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3377781/0e62e90d06d1e8558851de21f6ff68bf/450x300',
                        caption="Салат Кобб\n 550 ₽\n \t Описание: \nКуриное филе жареное, микс салата, яйцо куриное, помидоры, огурцы, редис свежий, заправка мучо ( йогурт, майонез, чеснок, зелень), мусс пармезан, салат корн",
                        reply_markup=markup_inl)
    if call.data == 'salads_6':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='salads')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3490335/773de26259d4437f989986f76cf5aec4/450x300',
                        caption="Салат Цезарь с креветками\n 680 ₽\n \t Описание: \nСалат айсберг, айсберг, креветки, помидоры черри, сыр пармезан, соус цезарь",
                        reply_markup=markup_inl)
    if call.data == 'salads_7':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='salads')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/2370127/1106a5d4e49b44d5a91a449efdceb083/450x300',
                        caption="Салат Цезарь с курицей\n 580 ₽\n \t Описание: \nСалат айсберг, айсберг, курица, помидоры черри, сыр пармезан, соус цезарь",
                        reply_markup=markup_inl)
    if call.data == 'salads_8':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='salads')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3583740/122db261e9748ba982261d1465cab973/450x300',
                        caption="Салат Греческий\n 490 ₽\n \t Описание: \nОгурцы, томаты, сладкий перец, оливки, маслины, красный лук, сербская брынза, оливковое масло, прованские травы",
                        reply_markup=markup_inl)
        