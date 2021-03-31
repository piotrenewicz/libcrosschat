from flask import Flask, request
from pymessenger import Bot
from tokens.facebook_config import ACCESS_TOKEN, VERIFY_TOKEN
import os

text_function = None
def register_text_endpoint(_message_function):
    global text_function
    text_function = _message_function

app = Flask(__name__)
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
                        response_sent_text = get_message(message['message'].get('text'), recipient_id)
                        send_message(recipient_id, response_sent_text)
    return "Message Processed"

def get_message(message, recipient_id):
    print(type)
    return text_function(message, recipient_id)

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"

def run():
    app.run(debug=True)
