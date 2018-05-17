#Import modules here
import discord
from discord.ext import commands
import asyncio
import os

"""You cannot use the Time module. Instead to await asyncio.sleep(Seconds), aysncio allows the bot to work because it pauses coroutines 
however time.sleep pauses the whole bot, which is not what we want.

Also make sure that there are no repeating loops because python will not run the discord bot code if the previos code
hasn't been executed."""


bot = commands.Bot(command_prefix='~')
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Watching NBA Games'))
    print('------------------\nLogged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------------------')
