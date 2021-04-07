import telebot
from time import sleep

try:
    from tokens.telegram_config import *
except ModuleNotFoundError:
    enable = False

if enable:
    # Initialize bot with given token
    bot = telebot.TeleBot(TOKEN)


def run():
    bot.polling(none_stop=True)


def unconfigured(*args, **kwargs):
    return None


text_function = unconfigured
full_function = unconfigured

def register_text_endpoint(_message_function):
    global text_function
    text_function = _message_function


def register_full_endpoint(_full_function):
    global full_function
    full_function = _full_function


if enable:
    # Handle simple text messages
    @bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact', 'new_chat_members', 'left_chat_member', 'new_chat_title',
                         'new_chat_photo', 'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message'])
    def respond(message: telebot.types.Message):
        if text_function is not unconfigured:
            bot.send_chat_action(message.chat.id, 'typing')
            bot.send_message(message.chat.id, text_function(
                message.text, message.chat.first_name))

        if full_function is not unconfigured:
            def responder(response):
                bot.send_message(message.chat.id, response)
            full_function(("TG", message.chat.id), message.text, message.chat.first_name, responder)


# Start bot's polling
if __name__ == '__main__':
    print('=====STARTING BOT=====')
    bot.polling(none_stop=True)
