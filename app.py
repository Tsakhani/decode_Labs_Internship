"""
app.py

This file connects the Flask app to Telegram.

Responsibilities:
1. Receive webhook updates from Telegram.
2. Extract the chat_id and message text.
3. Send the message to chatbot_logic.py.
4. Send the chatbot's response back to Telegram.

This file should stay small. It should not contain workout logic.
"""

import os
import requests

from flask import Flask, request
from dotenv import load_dotenv

from chatbot_logic import process_message


load_dotenv()

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

if BOT_TOKEN is None:
    raise ValueError(
        "BOT_TOKEN is missing. Please add it to your .env file or Railway environment variables."
    )

TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_telegram_message(chat_id, text):
    """
    Sends a message back to the Telegram user.
    """

    url = f"{TELEGRAM_API_URL}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text
    }

    response = requests.post(
        url,
        json=payload,
        timeout=10
    )

    return response.json()


@app.route("/", methods=["GET"])
def home():
    """
    Simple health check route.
    Useful for checking whether the Flask app is running.
    """

    return {
        "status": "running",
        "message": "Telegram Workout Bot is live."
    }


@app.route("/webhook", methods=["POST"])
def webhook():
    """
    Receives incoming Telegram updates.
    """

    data = request.get_json()

    if not data:
        return {
            "ok": False,
            "error": "No JSON data received."
        }, 400

    if "message" not in data:
        return {
            "ok": True,
            "message": "No message found in update."
        }, 200

    message_data = data["message"]

    if "chat" not in message_data:
        return {
            "ok": False,
            "error": "No chat found in message."
        }, 400

    chat_id = message_data["chat"]["id"]

    if "text" not in message_data:
        send_telegram_message(
            chat_id,
            "At the moment, I can only understand text messages. Please type your workout request."
        )

        return {
            "ok": True,
            "message": "Non-text message handled."
        }, 200

    user_message = message_data["text"]

    bot_response = process_message(
        chat_id,
        user_message
    )

    send_telegram_message(
        chat_id,
        bot_response
    )

    return {
        "ok": True
    }, 200


if __name__ == "__main__":
    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port
    )