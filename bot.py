import os
import discord
from discord.ext import commands
words = ["хуй", "пизд", "хуе", "хуё", "бля", "еба", "блет","пидор", "хую", "хуя" ] 
bot = commands.Bot(command_prefix= '¥')
@bot.event
async def on_message(message) :
    global words
    msg = message.content.lower()
    for i in words:
        if i in msg:
            await message.channel.purge(limit=1)
            await message.channel.send(f"{message.author.mention}, не матерись :)")
            break
token = os.environ.get('token')
bot.run(token)
