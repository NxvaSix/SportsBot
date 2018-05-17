import discord
from discord.ext import commands
import asyncio
import time
import os

bot = commands.Bot(command_prefix='~')
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Watching NBA Games'))
    print('------------------\nLogged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------------------')
