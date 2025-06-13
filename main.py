
from flask import Flask
from threading import Thread
from pyrogram import Client, filters
import os
import importlib.util
import pathlib

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

bot = Client(name="userbot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

def load_plugins():
    plugins_path = pathlib.Path("./plugins")
    for plugin in plugins_path.glob("*.py"):
        spec = importlib.util.spec_from_file_location(plugin.stem, plugin)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        print(f"Loaded plugin: {plugin.name}")

def start_bot():
    load_plugins()
    bot.run()

if __name__ == "__main__":
    Thread(target=start_bot).start()
    app.run(host="0.0.0.0", port=8080)
