import os
import discord
from discord.ext import commands
token = 'токен' 
words = ["маты", "маты", "маты"] 
bot = commands.Bot(command_prefix= 'префикс')
@bot.event
async def on_message(message) :
    global words
    msg = message.content.lower()
    for i in words:
        if i in msg:
            await msg.channel.purge(limit=1)
            break
        return
token = os.environ.get('token')
bot.run (token)
