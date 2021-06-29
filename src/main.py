import os
from dotenv import load_dotenv
from webserver import keep_running
from commands import *

# Load bot token from .env file
load_dotenv()
TOKEN = os.environ["TOKEN"]


@bot.event
async def on_ready():
    print(f"Successfully logged in as {bot.user}")

keep_running()
bot.run(TOKEN)
