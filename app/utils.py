from telebot import types

from app import config


def get_default_markup():
    default_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Помощь")
    item2 = types.KeyboardButton("Загрузить новый документ в базу знаний")
    default_markup.add(item2, item1)
    return default_markup


def get_yes_no_markup():
    default_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Да, этот")
    item2 = types.KeyboardButton("Нет, загружу другой")
    default_markup.add(item1, item2)
    return default_markup


def return_to_menu_markup():
    default_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Хочу вернуться в главное меню🥺")
    default_markup.add(item1)
    return default_markup


def help_markup():
    default_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Помощь")
    default_markup.add(item1)
    return default_markup




def send_default_message(message, bot):
    bot.send_message(message.chat.id,
                     config.WHAT_DO_YOU_WANT_STR,
                     reply_markup=get_default_markup())


