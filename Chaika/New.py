import telebot
import Constants
import os
import random

from Files.Attachment import Attachment

bot = telebot.TeleBot(Constants.token)

print(bot.get_me())


def send_audio(message, answer, file):
    bot.send_message(message.from_user.id, answer)
    directory = 'C:\\Users\\Dimas\\PycharmProjects\\Chaika\\Files\\' + file
    all_files_in_directory = os.listdir(directory)
    print(all_files_in_directory)
    random_file = random.choice(all_files_in_directory)
    audio = open(directory + '/' + random_file, 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_audio')
    bot.send_audio(message.from_user.id, audio)
    audio.close()


def log(message, answer):
    print('\n ------')
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст = {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id), message.text))
    print(answer)


def start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('Фото', 'Аудио', 'Стикер')
    user_markup.row('Настройки', 'Помощь')
    user_markup.row('Остановить чайку :с')
    bot.send_message(message.from_user.id, 'Здрасте', reply_markup=user_markup)


def stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'Noooooooo', reply_markup=hide_markup)


def settings(message):
    bot.send_message(message.chat.id, Constants.settings)


def help(message):
    bot.send_message(message.chat.id, Constants.helps)


def text(message):
    text = message.text.lower()

    if message.text == 'Остановить чайку :с':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Noooooooo', reply_markup=hide_markup)


    elif message.text in Constants.cho:
        answer = 'Через плечо'
        bot.send_message(message.from_user.id, answer)
        log(message, answer)


    elif message.text in Constants.ooo:
        answer = 'МОЯ ОБОРОНА'
        file = 'ooo'
        send_audio(message, answer, file)

    elif message.text in Constants.hello:
        answer = 'Забор покрасте'
        bot.send_message(message.from_user.id, answer)
        log(message, answer)


    elif message.text == 'Фото':
        attachment = Attachment(
            directory='C:\\Users\\Dimas\\PycharmProjects\\Chaika\\Files\\Photo',
            action='upload_photo',
            function={
                bot.send_photo(message.from_user.id, img)
            }
        )

        attachment.send(message, bot)

        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, action)
        img.close()


    elif message.text == 'Аудио':
        directory = 'C:\\Users\\Dimas\\PycharmProjects\\Chaika\\Files\\Audio'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        random_file = random.choice(all_files_in_directory)
        audio = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()


    elif message.text == 'Стикер':
        url = 'https://t.me/addstickers/joe_the_seagull_ru'
        bot.send_message(message.from_user.id, url)



    elif message.text == 'Настройки':
        bot.send_message(message.chat.id, Constants.settings)

    elif message.text == 'Помощь':
        bot.send_message(message.chat.id, Constants.helps)

    else:
        answer1 = message.text[::-1]
        answer = answer1.lower()

        log(message, answer)
        bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['stop'])
def handle_test(message):
    stop(message)


@bot.message_handler(commands=['settings'])
def handle_test(message):
    settings(message)


@bot.message_handler(commands=['start'])
def handle_test(message):
    start(message)


@bot.message_handler(commands=['help'])
def handle_test(message):
    help(message)


@bot.message_handler(content_types=['text'])
def handle_test(message):
    text(message)


bot.polling(none_stop=True, interval=0)
