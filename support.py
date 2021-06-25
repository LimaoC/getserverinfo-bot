import os
import requests
import json
from dotenv import load_dotenv
from sqlitedict import SqliteDict

# Load bot token from .env file
load_dotenv()
TOKEN = os.environ["TOKEN"]

db = SqliteDict("./bot_settings.sqlite", autocommit=True)


def get_online_players() -> str:
    """
    Returns a string with the number of players currently connected to the
    given server ip (up to 10 max).
    """
    MAX_PLAYERS = 10
    server_ip = db["server_ip"]

    # Get json data from API for given server ip
    response = requests.get(f"https://api.mcsrvstat.us/2/{server_ip}")
    json_data = json.loads(response.text)

    if json_data["online"]:
        num_players = json_data["players"]["online"]
        message = (f"There are {num_players} player(s) currently online "
                   f"on {server_ip}.")

        # If there are > 0 players online, list the player names (up to 10 max)
        if num_players > MAX_PLAYERS:
            try:
                for player in json_data["players"]["list"][:MAX_PLAYERS]:
                    message += "\n- " + player
                message += f"\n... and {num_players - MAX_PLAYERS} more"
            except KeyError as e:
                pass
        elif num_players > 0:
            for player in json_data["players"]["list"]:
                message += "\n- " + player
    else:
        message = f"{server_ip} is currently offline."

    return message


def update_server_ip(server_ip: str) -> str:
    """
    Updates the server ip in the bot settings to the given server ip.
    """
    if "." in server_ip and " " not in server_ip:
        db["server_ip"] = server_ip
        return f"Server IP has successfully been set to {server_ip}."
    else:
        return "Invalid IP."


def update_prefix(prefix: str) -> str:
    """
    Updates the prefix in the bot settings to the given prefix.
    """
    db["prefix"] = prefix
    return f"Bot prefix has successfully been set to {prefix}."


if __name__ == "__main__":
    print("This file is not intended to be run on its own. Run main.py "
          "instead.")
