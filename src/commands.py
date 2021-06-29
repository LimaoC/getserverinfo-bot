"""
This file contains the bot commands that users can use
"""
from discord.ext import commands
from server import *

bot = commands.Bot(command_prefix="!")
server = Server()


@bot.command(name="setprefix")
async def set_prefix(ctx, prefix):
    """
    Sets the bot prefix to the given prefix.
    """
    bot.command_prefix = prefix
    await ctx.send(f"Bot prefix successfully changed to {prefix}.")


@bot.command(name="setserverip")
async def set_default_ip(ctx, ip):
    """
    Sets the default server IP to use for the bot.
    """
    if "." in ip and server.server_ip != ip:
        server.server_ip = ip
        message = f"Default server IP successfully changed to {ip}."
    elif server.server_ip == ip:
        message = f"Default server IP is already {ip}."
    else:
        message = f"Invalid server IP."
    await ctx.send(message)


@bot.command(name="serverip")
async def get_server_ip(ctx):
    """
    Gets the current default server IP.
    """
    if server.server_ip:
        await ctx.send(f"The current default server IP is {server.server_ip}.")
    else:
        await ctx.send("There is no current default server IP. You can set one"
                       f" using {bot.command_prefix}setserverip <server ip>.")


@bot.command(name="resetserverip")
async def get_server_ip(ctx):
    """
    Resets the default server IP.
    """
    server.server_ip = None
    await ctx.send("The default server IP has been reset.")


@bot.command(name="online")
async def get_online_players(ctx, ip=None):
    """
    Gets a list of the players that are online (up to 10 max). A different
    server ip can be used, if specified.
    """
    if server.server_ip:
        await ctx.send(server.get_online_players(ip))
    else:
        await ctx.send("There is no current default server IP. You can set one"
                       f" using {bot.command_prefix}setserverip <server ip>.")


if __name__ == "__main__":
    print("This file is not intended to be run on its own. Run main.py "
          "instead.")
