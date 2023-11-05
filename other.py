from main import *
import telebot
from telebot import types

bot = telebot.TeleBot('5322324188:AAGsEpCEQCFR9DtI6bN6fv0f3CNPDCadEMk')


""" обработка гарниры """
def main_other(call):
    if call.data == 'other_1':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='other')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/2794391/b303fe11bb804669a134e57510d68935/450x300',
                        caption="Лимонад Маракуйя\n 800 ₽\n\tОписание:\nСобственного приготовления",
                        reply_markup=markup_inl)
    if call.data == 'other_2':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='other')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_message(call.message.chat.id, "Паста со шпинатом и томленой говядиной\n 620 ₽\n\tОписание:\nТальятелле, говядина отварная, шпинат, сливки, демиглас, масло растительное, пармезан",
                        reply_markup=markup_inl)    
    if call.data == 'other_3':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='other')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/2783965/c7459bd0b1704ded9e298a1b362cd790/450x300',
                        caption="Лимонад Мохито клубничный\n 800 ₽\n\tОписание:\nЛимонад собственного приготовления",
                        reply_markup=markup_inl)
    if call.data == 'other_4':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='other')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3506707/568d0aa5d2b04217aeed9e595ea7bd93/450x3000',
                        caption="Лимонад Мохито\n 800 ₽\n\tОписание:\nЛимонад собственного приготовления",
                        reply_markup=markup_inl)
    if call.data == 'other_5':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='other')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3504598/c33c6b503201485eac266dee3faf066e/450x300',
                        caption="Стейк Мачете (скерт)\n 1 350 ₽\n\tОписание:\nСтейк из тонкой диафрагмы",
                        reply_markup=markup_inl)
    if call.data == 'other_6':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='other')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3595513/981fe7f0a9b048d19bbad704effd5e02/450x300',
                        caption="Стейк Стриплойн\n 3 600 ₽",
                        reply_markup=markup_inl)
    if call.data == 'other_7':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='other')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3377781/f3956ff21b2341f797042b4ce477b828/450x300',
                        caption="Шоколадный флан\n 490 ₽\n\tОписание:\nШоколад, яйцо, масло сливочное, мука, сахар",
                        reply_markup=markup_inl)
    if call.data == 'other_8':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='other')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3595156/fc6f9062458d474db53e37c7cb9784ff/450x300',
                        caption="Фланк\n 1 550 ₽\n\tОписание:\nСтейк фланк постная часть говядины, вырезаемая из пашины",
                        reply_markup=markup_inl)
    if call.data == 'other_9':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='other')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/2050703/ab088e031fd54ec0a239f1f7321383ca/450x300',
                        caption="Паста фарфалле с лососем\n 850 ₽\n\tОписание:\nКабачок, вино белое, пармезан, черри, масло оливковое, специи",
                        reply_markup=markup_inl)
    if call.data == 'other_10':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='other')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3798638/ad0e2f2bd2134bc0a8ae8c2de2c38f73/450x300',
                        caption="Морс ягодный домашний\n 800 ₽\n\tОписание:\nМорс из ягод. Собственного приготовления",
                        reply_markup=markup_inl)
    if call.data == 'other_11':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='other')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3528150/75488706a0d249bc812d8434b0a76220/450x300',
                        caption="Стейк филе миньон\n 3 150 ₽\n\tОписание:\nСтейк из говяжьей вырезки",
                        reply_markup=markup_inl)
    if call.data == 'other_12':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='other')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/3106738/e9dba2800d0e490cbee68c4286d77204/450x300',
                        caption="Свежевыжатый сок\n 350 ₽\n\tОписание:\nФреш собственного приготовления на выбор",
                        reply_markup=markup_inl)
    if call.data == 'other_13':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='other')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/1370147/222cc4149cac2146f8cccd3c0e13a10b/450x300',
                        caption="Стейк рибай\n 3 750 ₽\n\tОписание:\nГовяжий стейк из толстого края мраморной говядины",
                        reply_markup=markup_inl)
    if call.data == 'other_14':
        markup_inl = types.InlineKeyboardMarkup()
        bt_app_ = types.InlineKeyboardButton("Скачать приложение", url='https://apps.apple.com/ua/app/mucho/id1633201246?l=ru')
        bt_back_ = types.InlineKeyboardButton("Назад", callback_data='other')
        markup_inl.add(bt_app_, bt_back_)
        bot.send_photo(call.message.chat.id, photo='https://avatars.mds.yandex.net/get-eda/1387779/1442a888d1b3e8cc9b465be38748e44c/450x300',
                        caption="Паста Пенне Арабьята\n 490 ₽\n\tОписание:\nОстрая паста в томатном соусе, помидоры черри, сыр пармезан, базилик",
                        reply_markup=markup_inl)
