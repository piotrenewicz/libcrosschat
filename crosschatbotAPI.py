import threading

import DiscordBackend
import FacebookBackend
import TelegramBackend

all_backends = [DiscordBackend, FacebookBackend, TelegramBackend]
all_threads = []


def attach_text(function_being_decorated):
    for backend in all_backends:
        backend.register_text_endpoint(function_being_decorated)

    return function_being_decorated


# def full_example(("Platform", room_id), message, author, send)
def attach_full(function_being_decorated):
    for backend in all_backends:
        backend.register_full_endpoint(function_being_decorated)

    return function_being_decorated


def begin_backends(blocking=True):
    for backend in all_backends:
        if backend.enable:
            all_threads.append(threading.Thread(
                target=backend.run, daemon=True))

    for thread in all_threads:
        thread.start()

    if len(all_threads) == 0:
        print("No backends are configured to start!\n"
              "Example configurations are located in crosschatbotAPI/tokens_template/\n"
              "copy them to crosschatbotAPI/tokens/ and edit with your tokens and preferences\n"
              "When you're done remember to set enable=True for the backends you wish to start!")
        return None

    print("Starting " + str(len(all_threads)) + " backends")
    if blocking:
        print("Blocking the MainThread, to prevent program close. \n"
              "Press enter to release the MainThread")
        input()
