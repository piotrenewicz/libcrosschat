#import discord_backend
import FacebookBot

user_function = None

def message_handler(incoming_message: str, author: str):
    response = user_function(incoming_message, author)
    return response


def begin(set_user_function):
    global user_function
    user_function = set_user_function
    #discord_backend.register_text_endpoint(user_function)
    #discord_backend.run()  # for multpile backends we will need threads here
    FacebookBot.register_text_endpoint(message_handler)
    FacebookBot.run()

