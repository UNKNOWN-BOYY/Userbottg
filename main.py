import os
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

# Optional: log all messages from your own account (for debugging)
@app.on_message(filters.me)
async def log_all(client, message):
    print("Received message:", message.text)

app.run()
