"""
This file contains a class which stores information about the default Minecraft
server used by the bot
"""
from lib import *
from support import *

# Accesses bot_settings database
try:
    os.mkdir("./db")  # creates the db folder if one does not exist
except FileExistsError:
    pass

DB_PATH = "./db/bot_settings.sqlite"
bot_settings = SqliteDict(DB_PATH, autocommit=True)


class Server:
    def __init__(self):
        """
        Constructs a Server object with the latest IP stored in the
        bot_settings database.
        """
        self._ip = bot_settings.get("server_ip")

    @property
    def server_ip(self) -> str:
        """
        Returns the current server ip.
        """
        return self._ip

    @server_ip.setter
    def server_ip(self, new_ip: str) -> None:
        """
        Sets the current server ip to the given ip.
        """
        bot_settings["server_ip"] = new_ip
        self._ip = new_ip


def has_server_icon(ip: str) -> bool:
    """
    Checks whether the given server ip has a dedicated icon, and converts the
    icon to a jpg.

    Returns:
        (bool): True if server has an icon, and False otherwise.
    """
    response = requests.get(f"https://api.mcsrvstat.us/2/{ip}", )
    json_data = json.loads(response.text)

    try:
        # Convert data URI from API to image
        icon = urllib.request.urlopen(json_data["icon"])

        with open(ICON_PATH, "wb") as image:
            image.write(icon.file.read())
        return True
    except KeyError:  # server does not have an icon
        return False


def get_online_players(ip: str) -> str:
    """
    Returns a message indicating the number of players that are online, and
    a list (up to 10 max) of players that are online.
    """
    MAX_PLAYERS = 10

    response = requests.get(f"https://api.mcsrvstat.us/2/{ip}")
    json_data = json.loads(response.text)

    if json_data["online"]:  # server is online
        num_players = json_data["players"]["online"]
        message = (f"There are {num_players} player(s) currently online "
                   f"on {ip}.")

        if num_players > MAX_PLAYERS:  # list player names if there are > 0
            try:  # API doesn't contain the player list if it is too large
                for player in json_data["players"]["list"][:MAX_PLAYERS]:
                    message += "\n- " + player
                message += f"\n... and {num_players - MAX_PLAYERS} more"
            except KeyError:
                pass
        elif num_players > 0:
            for player in json_data["players"]["list"]:
                message += "\n- " + player
    else:
        message = f"{ip} is currently offline."

    return message


def attach_icon_embed(embed: discord.Embed, ip: str) -> None:
    """
    Attaches the given server ip's icon (if any) to the given embed.
    """
    if has_server_icon(ip):
        image_path = ICON_PATH
        filename = "servericon.jpg"
    else:  # use the default server icon
        image_path = DEFAULT_ICON_PATH
        filename = "defaultservericon.jpg"

    # Attach the server icon to the embedded message
    file = discord.File(image_path, filename=filename)
    embed.set_author(name=ip, icon_url=f"attachment://{filename}")


def get_server_icon(ip: str) -> discord.File:
    """
    Returns the server icon for the given IP as a file object.
    """
    if has_server_icon(ip):
        return discord.File(ICON_PATH, filename="servericon.jpg")
    else:  # use the default server icon
        return discord.File(DEFAULT_ICON_PATH,
                            filename="defaultservericon.jpg")


if __name__ == "__main__":
    print("This file is not intended to be run on its own. Run main.py "
          "instead.")
