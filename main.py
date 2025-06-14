import os
import threading
from flask import Flask
from pyrogram import Client, filters

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION")

app = Client(
    name="mybot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,
    plugins=dict(root="plugins")
)

web = Flask(__name__)

@web.route('/')
def home():
    return "OK", 200

@web.route('/health')
def health():
    return "Healthy", 200

def run_flask():
    web.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_flask).start()

app.run()