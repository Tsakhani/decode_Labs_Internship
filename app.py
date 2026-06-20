"""
This script is responsible for receiving Telegram messages
Identifying the user
Passing the message to chatbot_logic.py, and
sending a response back to telegram
"""

from flask import Flask, request
from chatbot_logic import process_message

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.get_json()

    chat_id = data["message"]["chat"]["id"]
    message = data["message"]["text"]

    response = process_message(
        chat_id,
        message
    )

    # send responses to telegram here

    return {"ok":True}