import telebot
from time import sleep
from telegram_config import *

# Initialize bot with given token
bot = telebot.TeleBot(TOKEN)


# Handle /start command
@bot.message_handler(commands=['start'])
def start(message):
    sleep(0.5)
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.send_message(message.chat.id, 'Text after start command')


# Handle /help command
@bot.message_handler(commands=['help'])
def help_(message):
    sleep(0.5)
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.send_message(message.chat.id, 'Text after help command')


# Handle simple text messages
@bot.message_handler(content_types=['text'])
def text_message(message):
    sleep(0.5)
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.send_message(message.chat.id, 'Text after simple text message')


# Start bot's polling
if __name__ == '__main__':
    print('=====STARTING BOT=====')
    bot.polling(none_stop=True)
