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
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


@app.route("/", methods=["GET"])
def home():
    return "Telegram Workout Bot is running."


@app.route(f"/webhook/{BOT_TOKEN}", methods=["POST"])
def telegram_webhook():
    data = request.get_json(silent=True)

    if not data:
        return {"ok": False, "error": "No data received"}, 400

    message = data.get("message", {})
    chat = message.get("chat", {})
    chat_id = chat.get("id")
    user_text = message.get("text", "")

    if not chat_id:
        return {"ok": True}

    if not user_text:
        send_message(
            chat_id,
            "Please send a text message for now. Voice support can be added later."
        )
        return {"ok": True}

    response = process_message(chat_id, user_text)
    send_message(chat_id, response)

    return {"ok": True}


def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text
    }

    requests.post(url, json=payload)


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
