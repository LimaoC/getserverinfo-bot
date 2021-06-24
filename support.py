import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ["TOKEN"]
DEFAULT_IP = os.environ["DEFAULT_IP"]


def get_online_players(server_ip: str = DEFAULT_IP) -> str:
    """
    Returns a string with the number of players currently connected to the
    given server ip (up to 10 max).
    """
    MAX_PLAYERS = 10

    # Get json data from API for given server ip
    response = requests.get(f"https://api.mcsrvstat.us/2/{server_ip}")
    json_data = json.loads(response.text)

    if json_data["online"]:
        num_players = json_data["players"]["online"]
        message = (f"There are {str(num_players)} player(s) currently online "
                   f"on {server_ip}.")

        # If there are > 0 players online, list the player names (up to 10 max)
        if num_players > MAX_PLAYERS:
            try:
                for player in json_data["players"]["list"][:MAX_PLAYERS]:
                    message += "\n- " + player
                message += f"\n... and {num_players - MAX_PLAYERS}"
            except KeyError as e:
                pass
        elif num_players > 0:
            for player in json_data["players"]["list"]:
                message += "\n- " + player
    else:
        message = f"{server_ip} is currently offline."

    return message
