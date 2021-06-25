import os
import discord
from sqlitedict import SqliteDict
from dotenv import load_dotenv
from support import *

client = discord.Client()

db = SqliteDict("./bot_settings.sqlite", autocommit=True)


@client.event
async def on_message(message):
    prefix = db["prefix"]

    if message.author == client.user:  # ignore messages from self
        return

    # Admin commands
    if message.content.startswith(f"{prefix}serverip"):
        server_ip = message.content[len(prefix) + 9:]

        await message.channel.send(update_server_ip(server_ip))

    elif message.content.startswith(f"{prefix}setprefix"):
        new_prefix = message.content[len(prefix) + 10:]

        await message.channel.send(update_prefix(new_prefix))

    # User commands
    if message.content.startswith(f"{prefix}online"):
        # List all online players on the server
        await message.channel.send(get_online_players())


@client.event
async def on_ready():
    print(f"Successfully logged in as {client.user}")

client.run(TOKEN)
