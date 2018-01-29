import telebot
import Constants
import os
import random


bot = telebot.TeleBot(Constants.token)

print(bot.get_me())


def log(message, answer):
    print('\n ------')
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст = {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id), message.text))
    print(answer)


@bot.message_handler(commands=['stop'])
def handle_test(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'Бот остановлен', reply_markup=hide_markup)


@bot.message_handler(commands=['settings'])
def handle_test(message):
    bot.send_message(message.chat.id, Constants.settings)


@bot.message_handler(commands=['start'])
def handle_test(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('МГТУ', 'МГРИ')
    user_markup.row('/stop')
    bot.send_message(message.from_user.id, 'Здрасте', reply_markup=user_markup)


@bot.message_handler(commands=['help'])
def handle_test(message):
    bot.send_message(message.chat.id, Constants.helps)


@bot.message_handler(content_types=['text'])
def handle_test(message):
    if message.text == 'МГТУ':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Вы студент МГТУ? Поздравляю!', reply_markup=hide_markup)
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row('ИУ', 'ИБМ')
        bot.send_message(message.from_user.id, 'Укажите свой факультет', reply_markup=user_markup)
    if message.text == 'ИУ':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        bot.send_message(message.from_user.id, 'Информатика и системы управления', reply_markup=hide_markup)
        user_markup.row('ИУ-1', 'ИУ-2', 'ИУ-3' , 'ИУ-4')
        user_markup.row('ИУ-5', 'ИУ-6', 'ИУ-7', 'ИУ-8')
        user_markup.row('ИУ-9', 'ИУ-10', 'ИУ-11')
        user_markup.row('Назад')
        bot.send_message(message.from_user.id, 'Укажите номер кафедры', reply_markup=user_markup)
    if message.text == 'ИУ-1':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, Constants.table, reply_markup=hide_markup)
    if message.text == 'ИУ-2':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, Constants.table, reply_markup=hide_markup)
    if message.text == 'ИУ-3':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, Constants.table, reply_markup=hide_markup)
    if message.text == 'ИУ-4':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, Constants.table, reply_markup=hide_markup)
    if message.text == 'ИУ-5':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, Constants.table, reply_markup=hide_markup)
    if message.text == 'ИУ-6':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, Constants.table, reply_markup=hide_markup)
    if message.text == 'ИУ-7':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, Constants.table, reply_markup=hide_markup)
    if message.text == 'ИУ-8':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, Constants.table, reply_markup=hide_markup)
    if message.text == 'ИУ-9':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, Constants.table, reply_markup=hide_markup)
    if message.text == 'ИУ-10':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, Constants.table, reply_markup=hide_markup)
    if message.text == 'ИУ-11':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, Constants.table, reply_markup=hide_markup)

    elif message.text == 'Здрасте':
        bot.send_message(message.from_user.id, 'Забор покрасте')



    elif message.text == 'Фото':
        directory = 'C:\\Users\\Dimas\\PycharmProjects\\Chaika\\Files\\Photo'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
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


bot.polling(none_stop=True, interval=0)
