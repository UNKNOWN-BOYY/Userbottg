from pyrogram import Client, filters

@Client.on_message(filters.command("ping"))
async def ping_handler(client, message):
    await message.reply("Pong!")