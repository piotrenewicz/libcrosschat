from flask import Flask, request
from pymessenger import Bot
from tokens.discord_config import ACCESS_TOKEN, VERIFY_TOKEN
import os

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
                        response_sent_text = get_message(message['message'].get('text'))
                        send_message(recipient_id, response_sent_text)
    return "Message Processed"

def get_message(message):
    if message.lower() == "hello":
        return "Hi!"
    elif message.lower() == "what day is today?":
        return "Today is Wendsday."

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"



if __name__ == "__main__":
    os.system("ngrok.exe http 5000")
    app.run(debug=True)
