from flask import Flask, request
from pymessenger import Bot
try:
    from tokens.facebook_config import ACCESS_TOKEN, VERIFY_TOKEN, enable
except ModuleNotFoundError:
    enable = False


def unconfigured(*args, **kwargs):
    return


text_function = unconfigured
full_function = unconfigured


def register_text_endpoint(_message_function):
    global text_function
    text_function = _message_function


def register_full_endpoint(_full_function):
    global full_function
    full_function = _full_function


app = Flask(__name__)
if enable:
    bot = Bot(ACCESS_TOKEN)


@app.route('/conversion_layer', methods=['POST', 'GET'])
def verify_token():
    if request.method == 'GET':
        token = request.args.get("hub.verify_token")
        if token == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Invalid verification token"
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        process_message(message['message'].get('text'), recipient_id)

    return "Message Processed"


def process_message(message, recipient_id):
    if full_function is not unconfigured:
        def responder(response):
            send_message(recipient_id, response)
        full_function(("FB", recipient_id), message, recipient_id, responder)

    if text_function is not unconfigured:
        quick_response = text_function(message, recipient_id)
        send_message(recipient_id, quick_response)


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"


def run():
    app.run(debug=True, use_reloader=False)
