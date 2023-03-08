from bot import bot
import telebot
from telebot import types

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('С чего начать проект?')
    btn2 = types.KeyboardButton('Банк идей проектов')
    btn3 = types.KeyboardButton('Банк тем проектов')
    btn4 = types.KeyboardButton('Проблема')
    btn5 = types.KeyboardButton('Продукт')
    btn6 = types.KeyboardButton('Исследование')
    btn7 = types.KeyboardButton('План проекта')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    bot.send_message(message.from_user.id, 'Привет, я бот, который может помочь вам создать собственный Индивидуальный Проект!')
    bot.send_message(message.from_user.id, 'Пожалуйста, выберите интересующий вас вопрос', reply_markup= markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'С чего начать проект?':
        bot.send_message(message.from_user.id, 'С чего начать проект? (*testing button*)')
    elif message.text == 'Банк идей проектов':
        bot.send_message(message.from_user.id, 'Банк идей проектов (*testing button*)')
    elif message.text == 'Банк тем проектов':
        bot.send_message(message.from_user.id, 'Банк тем проектов (*testing button*)')
    elif message.text == 'Проблема':
        bot.send_message(message.from_user.id, 'Проблема (*testing button*)')
    elif message.text == 'Продукт':
        bot.send_message(message.from_user.id, 'Продукт (*testing button*)')
    elif message.text == 'Исследование':
        bot.send_message(message.from_user.id, 'Исследование (*testing button*)')
    elif message.text == 'План проекта':
        bot.send_message(message.from_user.id, 'План проекта (*testing button*)')
    elif message.text == 'С чего начать проект?':
        bot.send_message(message.from_user.id, 'С чего начать проект? (*testing button*)')
        
bot.polling(none_stop=True, interval=0)