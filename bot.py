#!/usr/bin/env python
import types
import telebot
import os

TOKEN = '709201343:AAGiXyNFHmExukOiE6vGYlsdQDLLiLWw2NI'

bot = telebot.TeleBot(TOKEN)

def log(message, answer):
    print('\n')
    from datetime import datetime
    print(datetime.now())
    print('Сообщение от {0} {1} , (id = {2}) \n Текст - {3}'.format(message.from_user.first_name,
                                                                    message.from_user.last_name,
                                                                    str(message.from_user.id),
                                                                    message.text))
    print(answer)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Наши контакты и адресс','Заказать товар')
    user_markup.row('Куртки','Платья' ,'Джинсы')
    user_markup.row('Рубашки','Обувь','Кардиганы','Другое',)
    answer = 'FashionWorldBot:' \
             '\nДобро пожаловать дорогой пользователь моего бота !'
    log(message, answer)
    bot.send_message(message.from_user.id, answer , reply_markup=user_markup)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    answer = 'Бот создан новичком в этой сфере, не судите строго'
    log(message, answer)
    bot.reply_to(message, answer)

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    if message.text == 'Свитера':
        directory = "smth/photo"
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file,'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id,'upload_photo')
            bot.send_photo(message.from_user.id, answer)
            answer.close()
    elif message.text == 'Куртки':
        directory = 'smth/photo'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
            answer.close()
    elif message.text == 'Рубашки':
        directory = 'smth/photo'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file,'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id,'upload_photo')
            bot.send_photo(message.from_user.id, answer)
            answer.close()
    elif message.text == 'Платья':
        directory = 'smth/photo'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
            answer.close()
    elif message.text == 'Джинсы':
        directory = 'smth/photo'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
            answer.close()
    elif message.text == 'Обувь':
        directory = 'smth/photo'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file,'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id,'upload_photo')
            bot.send_photo(message.from_user.id, answer)
            answer.close()
    elif message.text == 'Кардиганы':
        directory = 'smth/photo'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
            answer.close()
    elif message.text == 'Другое':
        directory = 'smth/photo'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
            answer.close()
    elif message.text == 'Заказать товар':
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = telebot.types.KeyboardButton(text='Отправить номер телефона', request_contact=True)
        button_geo = telebot.types.KeyboardButton(text='Отправить местоположение', request_location=True)
        button_hub = telebot.types.KeyboardButton(text='Назад')
        keyboard.add(button_phone,button_geo,button_hub)
        answer = '--------------------------------------------------------------------------------'\
                 '\nДля того чтобы заказать товар ,' \
                 '\nвы должны нам отправить ваши данные ,' \
                 '\nтоесть ваш номер телефона и желательно адресс.' \
                 '\nВ скором времени вам отвят.' \
                 '\nЗатем человеку , который вам ответит' \
                 '\nвы должны отправить фотографию и размер товара,' \
                 '\nкоторый вы хотите преобрести.' \
                 '\nЕсли товар отсутствует или нет вашего размера,' \
                 '\nвам предложат другой вариант.' \
                 '\nПо поводу доставки , также уточняете.' \
                 '\n--------------------------------------------------------------------------------' \


        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=keyboard)
    elif message.text == 'Назад':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Наши контакты и адресс', 'Заказать товар')
        user_markup.row('Свитера', 'Куртки', 'Платья', 'Джинсы')
        user_markup.row('Рубашки', 'Обувь', 'Кардиганы', 'Другое', )
        answer = 'Вы перешли в главное меню .'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == 'Наши контакты и адресс':
        bot.send_message(message.from_user.id , 'Контактная информация'
                                                '\n---------------------------------------'
                                                '\nНаш номер телефона :\n+998 94 6119619'
                                                '\n---------------------------------------'
                                                '\nНаш адресс :\n15-й квартал, 50 массив Юнусабад,\nЮнусабадский район, Ташкент, Узбекистан'
                                                '\n---------------------------------------------------------------------------------------'
                                                '\nhttps://yandex.ru/maps?whatshere%5Bpoint%5D=69.304746%2C41.375958&whatshere%5Bzoom%5D=17.0&ll=69.304746%2C41.37479140025151&z=17.0'
                                                '\n---------------------------------------------------------------------------------------')

    else:
        bot.send_message(message.from_user.id , 'Я вас не понимаю.')

@bot.message_handler(content_types=['location'])
def user_location(message):
    lat = message.location.latitude
    lon = message.location.longitude
    answer = 'Заказ пришел от покупателя :{0} ,\nАдресс : {1},{2}'.format(message.from_user.first_name,
                                                                          lat,lon)

    bot.send_message(662273735, answer)


@bot.message_handler(content_types=['contact'])
def user_contact(message):
    answer = 'Заказ пришел от покупателя :{0} ,\nНомер телефона : {1}'.format(message.from_user.first_name,
                                                                              message.contact.phone_number)
    bot.send_message(662273735, answer)


bot.polling(none_stop=True)