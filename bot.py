import os
import telebot
from telebot import types

TOKEN = os.getenv("TELEGRAM_TOKEN")  # Убедись, что эта переменная задана на Render
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton("📞 Calling phrases"),
        types.KeyboardButton("📄 Documents"),
        types.KeyboardButton("📍 Load status")
    )
    bot.send_message(message.chat.id, "Welcome! Choose a category:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def reply(message):
    if message.text == "📞 Calling phrases":
        bot.send_message(message.chat.id, "Hi, I'm calling about the load from Dallas to Atlanta. Is it still available?")
    elif message.text == "📄 Documents":
        bot.send_message(message.chat.id, "Please send the rate confirmation to our email.")
    elif message.text == "📍 Load status":
        bot.send_message(message.chat.id, "The driver is empty and can pick up today at 3 PM.")
    else:
        bot.send_message(message.chat.id, "I didn't understand that. Please choose a button.")

bot.polling()
