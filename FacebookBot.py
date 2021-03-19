from flask import Flask, request
from pymessenger import Bot
import random
# app = Flask(__name__)

# PAGE_ACCESS_TOKEN = ''

# bot = Bot(PAGE_ACCESS_TOKEN)

# VERIFY_TOKEN = 'alamakota'

# def process_message(text):
#     formatted_message = text.lower()
#     if formatted_message == "test":
#         response = "Test Successful"
#     elif formatted_message == "what are your hours?":
#         response = "We're open on these days at these hours"
#     else:
#         response = "See you soon!"

#     return response

# @app.route('/', methods=["POST", "GET"])
# def webhook():
#     if request.method == "GET":
#         if request.args.get("hub.verify_token") == VERIFY_TOKEN:
#             return request.args.get("hub.challenge")
#         else:
#             return "Hello! Not connected to Facebook!"
#     elif request.method == "POST":
#         payload = request.json
#         event = payload['entry'][0]['messaging']
#         for msg in event:
#             text = msg['message']['text']
#             sender_id = msg['sender']['id']
#             response = process_message(text)
#             bot.send_message(sender_id, response)
#         return "Message received."
#     else:
#         return "200"

app = Flask(__name__)
VERIFY_TOKEN = "alamakota"
ACCESS_TOKEN = ""
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
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)
    return "Message Processed"

def get_message():
    sample_responses = ["We done it!", "Great work! :)"]
    return random.choice(sample_responses)

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"



if __name__ == "__main__":
    app.run(debug=True)
