import discord
from discord.ext import commands

@commands.command()
async def hola(ctx):
    await ctx.send(f'Hola {ctx.author.mention}, como te encuentras el dia de hoy? (❁´◡`❁)')
    
@commands.command()
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    if member.avatar:
        avatar_url = member.avatar.url
    else:
        avatar_url = member.default_avatar_url

    await ctx.send(avatar_url)

def setup_recreation_commands(bot):
    bot.add_command(hola)
    bot.add_command(avatar)
