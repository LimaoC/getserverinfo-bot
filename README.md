# GetServerInfo
[![Github issues](https://img.shields.io/github/issues/LimaoC/getserverinfo-bot)](https://github.com/LimaoC/getserverinfo-bot/issues)
[![Github forks](https://img.shields.io/github/forks/LimaoC/getserverinfo-bot)](https://github.com/LimaoC/getserverinfo-bot/network/members)
[![Github stars](https://img.shields.io/github/stars/LimaoC/getserverinfo-bot)](https://github.com/LimaoC/getserverinfo-bot/stargazers)
[![Github license](https://img.shields.io/github/license/LimaoC/getserverinfo-bot)](https://github.com/LimaoC/getserverinfo-bot/)

GetServerInfo is a Discord bot built in Python that fetches information on Minecraft servers.

It is designed to be used in small Discord servers with a dedicated Minecraft server, and allows you to get server statistics without needing to open up the server console or log onto Minecraft.

Thank you to https://api.mcsrvstat.us/ for the Minecraft server API!

# Dependencies
Dependencies that are necessary if you want to run the bot yourself:
- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [discord.ext](https://discordpy.readthedocs.io/en/stable/ext/commands/index.html)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://docs.python-requests.org/en/master/)
- [sqlitedict](https://pypi.org/project/sqlitedict/)
- [Flask](https://pypi.org/project/Flask/) (for running the web server)

# Usage

# License
[MIT](https://choosealicense.com/licenses/mit/)

# Roadmap
- [x] Implement main functionality: fetching information from Minecraft server using ip
- [ ] Implement permission levels for commands
- [x] Make use of Discord message embeds instead of common messages
- [ ] Add graphics
- [ ] Add tests
