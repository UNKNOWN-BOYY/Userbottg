
from pyrogram import Client, filters

@Client.on_message(filters.command("ping", prefixes=".") & filters.me)
async def ping_handler(client, message):
    await message.reply_text("Pong!")
