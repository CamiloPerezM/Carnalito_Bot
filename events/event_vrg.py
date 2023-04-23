import discord
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith(bot.command_prefix):
        await bot.process_commands(message)  # procesar comandos
        return

    if not message.content.startswith('!'):
        if "verga" in message.content.lower().split() and len(message.content.lower().split()) == 1:
            await message.channel.send(f"{message.author.mention} Comes ¯\_(ツ)_/¯ ")
        elif "vrg" in message.content.lower().split() and len(message.content.lower().split()) == 1:
            await message.channel.send(f"{message.author.mention} Comes ¯\_(ツ)_/¯ ")
