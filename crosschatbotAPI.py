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


# def full_example("Platform", room_id, message, author, send)
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

    print("Backends ready, waiting for interaction")
    if blocking:
        print("press enter to release wait")
        input()
