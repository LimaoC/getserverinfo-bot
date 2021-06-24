import os
import discord
from dotenv import load_dotenv
from support import *

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:  # ignore messages from self
        return

    if message.content.startswith("!online"):
        # If no server ip is specified, use default IP
        if message.content == "!online":
            players_online = get_online_players()
        else:
            server_ip = message.content[8:]
            players_online = get_online_players(server_ip)
        await message.channel.send(players_online)


@client.event
async def on_ready():
    print(f"Successfully logged in as {client.user}")

client.run(TOKEN)
