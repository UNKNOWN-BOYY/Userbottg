
from flask import Flask
from threading import Thread
from pyrogram import Client
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION_STRING = os.environ.get("SESSION_STRING")

app = Flask(__name__)

@app.route('/')
def home():
    return "Userbot is running!"

@app.route('/ping')
def ping():
    return "Pong!", 200

def start_bot():
    with Client(name="userbot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING) as app:
        print("Userbot started.")
        app.run()

if __name__ == "__main__":
    Thread(target=start_bot).start()
    app.run(host="0.0.0.0", port=8080)
