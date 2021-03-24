import crosschatbotAPI


def this_is_client_job(message: str, author: str):
    return "Hello, you've contacted client code function!\nUnfortunately we are still under construction.\nLong story short, you're not getting any other response from us today!"


crosschatbotAPI.begin(this_is_client_job)
