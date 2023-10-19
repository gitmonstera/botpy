from main import *
import telebot
from telebot import types

bot = telebot.TeleBot('5322324188:AAGsEpCEQCFR9DtI6bN6fv0f3CNPDCadEMk')

""" обработка закусок """
def main_zac(call):
    if call.data == 'zac_1':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='snacks')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3596693/d7cea9fea0564f7595e904e0ba98e7d1/450x300',
                        caption="Тортилья с томатами и страчателлой\n 590 ₽\n \t Описание: \nТесто для пиццы, томаты, страчателла, песто, манка, базилик свежий",
                        reply_markup=markup_inl)
    if call.data == 'zac_2':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='snacks')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3790679/52bba02d16ad4b0ea776c51101a6d5d3/450x300',
                        caption="Начос с соусами\n 450 ₽ \n \t Описание: \nНачос с соусом сальса и сырным",
                        reply_markup=markup_inl)
    if call.data == 'zac_3':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='snacks')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3454897/760f9de70ef6491a8926b856e5864c64/450x300',
                        caption="Брускетта с ростбифом и соусом манго-чили\n350 ₽ \n \t Описание: \nХлеб зерновой, сыр креметте, соус манго-чили, ростбиф, перец печеный, руккола, масло оливковое",
                        reply_markup=markup_inl)
    if call.data == 'zac_4':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='snacks')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3702558/1a561ba2f7a44e06aaf7ac6c61c48d97/450x300',
                        caption="Брускетта с тартаром из лосося и авокадо\n350 ₽ \n \t Описание: \nХлеб зерновой, масло чесночное, лосось,"
                                "авокадо, огурец, лимон, масло кунжутное, майонез, соевый соус, рукола",
                        reply_markup=markup_inl)
    if call.data == 'zac_5':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='snacks')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3521394/2a978a9c35254bb8b2a6d06199f6248d/450x300',
                        caption="Брускетта с тартаром из лосося и клубники\n350 ₽ \n \t Описание: \nХлеб зерновой, лосось, клубника, масло оливковое, мята, сыр креметте, лимон",
                        reply_markup=markup_inl)
    if call.data == 'zac_6':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='snacks')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3790679/11da7f39536c4a8fbc76e0071d1aad35/450x300',
                        caption="Кесадилья с мясом\n580 ₽ \n \t Описание: \nТоматы, перец болгарский, лук репчатый, говядина, куриное бедро,"
                        "куриная грудка, томатная паста, чеснок, кукуруза, кориандр, сыр моцарелла, тортилья, лолло россо, соус сальса, сметана",
                        reply_markup=markup_inl)
    if call.data == 'zac_7':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='snacks')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3529621/2a75ab07d6ba256ba474cd649886d563/450x300',
                        caption="Пикантные крылья Баффало\n590 ₽ \n \t Описание: \nЖареные во фритюре куриные крылья, соус барбекю, "
                        "соус тобаско, ломтики моркови и сельдерея с соусом блю чиз",
                        reply_markup=markup_inl)
    if call.data == 'zac_8':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='snacks')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/1380157/00812d11dee95d554853d80baf66a87c/450x300',
                        caption="Гренки ржаные\n210 ₽ \n \t Описание: \nПодаются с чесночным соусом",
                        reply_markup=markup_inl)
    if call.data == 'zac_9':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='snacks')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3514991/78ca09402db44fde973e864fb2f338fa/450x300',
                        caption="Кесадилья с грушей и горгонзолой\n580 ₽ \n \t Описание: \nГруша, сыр моцарелла, сыр дор блю, тортилья, мед",
                        reply_markup=markup_inl)
    if call.data == 'zac_10':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='snacks')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3514991/78ca09402db44fde973e864fb2f338fa/450x300',
                        caption="Сырные палочки с брусничным соусом\n390 ₽ \n \t Описание: \nСырные палочки, брусничный соус",
                        reply_markup=markup_inl)
    if call.data == 'zac_11':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='snacks')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/1368744/aa7bdc67711245e31e23ad1b0707a54c/450x300',
                        caption="Хрустящие креветки со Сладким чили\n490 ₽ ",
                        reply_markup=markup_inl)
    if call.data == 'zac_12':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='snacks')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3593277/76b2d6fb0fb846868495a9ea5bc0cfdb/450x300',
                        caption="Бурито с цыпленком\n510 ₽ \n \t Описание: \nТортилья пшеничная, куриное филе, сыр чеддер, "
                        "перец болгарский свежий, кукуруза консервированная, красный лук, соус сальса, соус гуакамоле",
                        reply_markup=markup_inl)
    if call.data == 'zac_13':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='snacks')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3816972/4a14eda3fb50a2a8cc34f0ad7b5549f6/450x300',
                        caption="Тако с ростбифом\n590 ₽ \n \t Описание: \nРостбиф, тортилья пшеничная, соус сальса, руккола",
                        reply_markup=markup_inl)
    if call.data == 'zac_14':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='snacks')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3337779/781f9d787dd64615a2c1efc99384e20c/450x300',
                        caption="Буррито с говядиной\n550 ₽ \n \t Описание: \nПшеничная лепешка, говядина (фарш), гуакамоле, томаты пилати,"
                        " фасоль консервированная, кукуруза консервированная, сыр чеддер, халапеньо, специи",
                        reply_markup=markup_inl)
    if call.data == 'zac_15':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='snacks')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3401132/b1355c65b74b75800e50cdd1abb533d9/450x300',
                        caption="Тако с курицей и сладким чили\n490 ₽ \n \t Описание: \nТортилья пшеничная, курица, сыр чеддер, "
                        "перец болгарский печеный, соус сладкий чили, кукуруза консервированная, кинза ",
                        reply_markup=markup_inl)
