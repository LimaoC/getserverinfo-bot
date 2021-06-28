import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from commands import *

# Load bot token from .env file
load_dotenv()
TOKEN = os.environ["TOKEN"]


@bot.event
async def on_ready():
    print(f"Successfully logged in as {bot.user}")

bot.run(TOKEN)
