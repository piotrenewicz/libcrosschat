import threading

import DiscordBackend
import FacebookBackend
# import TelegramBackend

all_backends = [DiscordBackend, FacebookBackend]  # , TelegramBackend]
# waiting on mykhailo to implement TelegramBackend.register_text_endpoint() and TelegramBackend.run()
all_threads = []


user_text_function = NotImplementedError


def text_handler(incoming_message: str, author: str):
    response = user_text_function(incoming_message, author)
    return response


def attach_text(function_being_decorated):
    global user_text_function
    user_text_function = function_being_decorated

    for backend in all_backends:
        backend.register_text_endpoint(text_handler)

    return function_being_decorated


def begin_backends():
    for backend in all_backends:
        if backend.enable:
            all_threads.append(threading.Thread(target=backend.run, daemon=True))

    for thread in all_threads:
        thread.start()

