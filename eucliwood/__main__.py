import discord 
from discord.ext import commands

eucliwood = commands.Bot (
    command_prefix = 'eu ',
    activity = discord.Game(name="Commands: euhelp"),
    case_insensitive = True,
    max_messages = 10_000,
)
# On startup
print(" Bot starting! ")

# Commands
eucliwood.load_extension("cogs.misc")

token = open("eucliwood/token", "r")
eucliwood.run(token.readline())    


# On shutdown
print(" Bot turning off ")