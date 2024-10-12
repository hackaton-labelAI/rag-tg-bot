import re

import telebot
from telebot import types

import config
from api_stubs import proccess_pdf, proccess_question
from utils import send_default_message, get_default_markup, return_to_menu_markup

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(content_types=['document'])
def handle_docs(message):
    try:
        if re.match(r"^.*\.pdf$", message.document.file_name):
            bot.send_message(message.chat.id,
                             'Супер, сохраняю☺️')

            # тут пост-запрос
            # src = 'C:/Python/Project/tg_bot/files/received/' + ;
            # with open(src, 'wb') as new_file:
            #     new_file.write(downloaded_file)
            is_file_proccessed_successfully = proccess_pdf()

            if is_file_proccessed_successfully:
                bot.reply_to(message, 'Все прошло успешно☺️')
                send_default_message(message, bot)
            else:
                bot.reply_to(message, 'Что-то пошло не так😰')
        else:
            bot.send_message(message.chat.id,
                             'Ты мне прислал не pdf-документ🤔Попробуй еще раз или вернись в главное меню',
                                    reply_markup=return_to_menu_markup())
    except Exception as e:
        bot.reply_to(message, e)
        send_default_message(message, bot)



@bot.message_handler(commands=['start'])
def button_message(message):
    bot.send_message(message.chat.id,
                     f'Привет! ☺️ \nЯ бот, который отвечает на вопросы по нормативным документам ржд. {config.WHAT_DO_YOU_WANT_STR}',
                     reply_markup=get_default_markup())


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Задать вопрос":
        #markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        question = message.text
        response = proccess_question()
        bot.send_message(message.chat.id, response)
        bot.send_message(message.chat.id, f'{config.WHAT_DO_YOU_WANT_STR}', reply_markup=get_default_markup())
    elif message.text == "Загрузить новый документ в базу знаний":
        bot.send_message(message.chat.id, 'Отправь мне документ с расширением pdf 👇')
    elif message.text == "Хочу вернуться в главное меню🥺":
        bot.send_message(message.chat.id, f'{config.WHAT_DO_YOU_WANT_STR}', reply_markup=get_default_markup())


bot.infinity_polling()
