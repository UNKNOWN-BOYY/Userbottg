import os
import threading
from flask import Flask
from pyrogram import Client, filters

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION")

# Start Pyrogram Client
app = Client(
    name="mybot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,
    plugins=dict(root="plugins")
)

# Flask app to keep instance alive for Koyeb
web = Flask(__name__)

@web.route('/')
def home():
    return "Userbot is running!"

# 🔧 This part is critical
def run_flask():
    # Bind to 0.0.0.0 (public) instead of localhost (127.0.0.1)
    web.run(host="0.0.0.0", port=8080)

# Run Flask in a separate thread
threading.Thread(target=run_flask).start()

# Start the userbot
app.run()
