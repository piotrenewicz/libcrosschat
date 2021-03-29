import crosschatbotAPI
import time


@crosschatbotAPI.attach_text
def this_is_client_job(message: str, author: str):
    time.sleep(10)
    return "Hello, you've contacted client code function!\nUnfortunately we are still under construction.\nLong story short, you're not getting any other response from us today!" + message + author


crosschatbotAPI.begin_backends()
print("user code complete, now just waiting")
time.sleep(430)