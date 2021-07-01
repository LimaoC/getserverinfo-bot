"""
This file contains the bot commands that users can use
"""
from lib import *
from server import *
from support import *

bot = commands.Bot(command_prefix=bot_settings.get("bot_prefix", "!"))
server = Server()


@bot.command(name="setprefix")
async def set_prefix(ctx, prefix):
    """
    Sets the bot prefix to the given prefix. Default prefix is !.
    """
    bot_settings["bot_prefix"] = prefix
    bot.command_prefix = prefix

    embed = discord.Embed(
        title=SUCCESS_MESSAGE,
        description=f"Bot prefix successfully changed to {prefix}.",
        colour=discord.Color.green())

    await ctx.send(embed=embed)


@bot.command(name="setserverip")
async def set_default_ip(ctx, ip):
    """
    Sets the default server IP the bot will use.
    """
    if "." in ip and server.server_ip != ip:  # valid IP change
        server.server_ip = ip
        embed = discord.Embed(
            title=SUCCESS_MESSAGE,
            description=f"Default server IP successfully changed to {ip}.",
            colour=discord.Color.green())
    elif server.server_ip == ip:
        embed = discord.Embed(
            title=FAIL_MESSAGE,
            description=f"Default server IP is already {ip}.",
            colour=discord.Color.red())
    else:
        embed = discord.Embed(
            title=FAIL_MESSAGE,
            description="Invalid server IP.",
            colour=discord.Color.red())

    await ctx.send(embed=embed)


@bot.command(name="serverip")
async def get_server_ip(ctx):
    """
    Gets the default server IP.
    """
    if server.server_ip:
        if has_server_icon(server.server_ip):
            image_path = ICON_PATH
            filename = "servericon.jpg"
        else:  # use the default server icon
            image_path = DEFAULT_ICON_PATH
            filename = "defaultservericon.jpg"

        # Attach the server icon to the embedded message
        file = discord.File(image_path, filename=filename)

        embed = discord.Embed(
            description=f"The default server IP is {server.server_ip}.",
            colour=discord.Color.green())
        embed.set_author(name=server.server_ip,
                         icon_url=f"attachment://{filename}")

        await ctx.send(file=file, embed=embed)
    else:
        embed = discord.Embed(
            title=FAIL_MESSAGE,
            description="There is no default server IP. You can set one using "
                        f"{bot.command_prefix}setserverip <server ip>.",
            colour=discord.Color.red())

        await ctx.send(embed=embed)


@bot.command(name="resetserverip")
async def get_server_ip(ctx):
    """
    Resets the default server IP.
    """
    server.server_ip = None
    await ctx.send(embed=discord.Embed(
        title=SUCCESS_MESSAGE,
        description="The default server IP has been reset.",
        colour=discord.Color.green()))


@bot.command(name="online")
async def list_online_players(ctx, ip=None):
    """
    Gets a list of the players that are online, up to 10 max (uses the server
    IP stored by default).
    """
    if server.server_ip and ip is None:  # use the default IP
        ip = server.server_ip
    if ip:
        if has_server_icon(server.server_ip):
            image_path = ICON_PATH
            filename = "servericon.jpg"
        else:  # use the default server icon
            image_path = DEFAULT_ICON_PATH
            filename = "defaultservericon.jpg"

        # Attach the server icon to the embedded message
        file = discord.File(image_path, filename=filename)

        embed = discord.Embed(description=get_online_players(ip),
                              colour=discord.Color.green())
        embed.set_author(name=ip,
                         icon_url=f"attachment://{filename.jpg}")

        await ctx.send(file=file, embed=embed)
    else:
        embed = discord.Embed(
            title=FAIL_MESSAGE,
            description="There is no default server IP. You can set one using "
                        f"{bot.command_prefix}setserverip <server ip>.",
            colour=discord.Color.red())

        await ctx.send(embed=embed)


if __name__ == "__main__":
    print("This file is not intended to be run on its own. Run main.py "
          "instead.")
