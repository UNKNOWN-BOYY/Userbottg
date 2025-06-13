from pyrogram import Client
from flask import Flask
import os

app = Flask(__name__)

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION_STRING = os.environ.get("SESSION_STRING")

bot = Client(
    "userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,
    no_updates=True  # Disable update handling
)


# Load plugins
def load_plugins():
    from os import listdir
    from importlib import import_module
    for file in listdir("plugins"):
        if file.endswith(".py"):
            name = file[:-3]
            import_module(f"plugins.{name}")
            print(f"Loaded plugin: {file}")

@app.route('/')
def home():
    return "Userbot is running!"

if __name__ == "__main__":
    load_plugins()
    bot.run()  # ✅ run in main thread — fixes signal() error

