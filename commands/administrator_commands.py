import discord
from discord.ext import commands

advertencias = []

@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None, *, reason=None):
    if not member:
        await ctx.send('Debes mencionar a un miembro para expulsar Ejemplo: `!kick @usuario razón`')
        return
    if not reason:
        await ctx.send(f'{ctx.author.mention}, debes proporcionar una razón para expulsar a {member.mention}')
        return
    if not ctx.guild.me.guild_permissions.kick_members:
        await ctx.send('No tengo permisos para expulsar miembros')
        return
    if ctx.author.top_role <= member.top_role:
        await ctx.send(f'{ctx.author.mention}, no puedes expulsar a {member.mention} porque tienen un rol igual o superior al tuyo.')
        return
    try:
        await member.kick(reason=reason)
        await ctx.send(f'Expulsado {member.mention} por {ctx.author.mention} debido a {reason}')
    except discord.Forbidden:
        await ctx.send('No puedo expulsar a ese miembro debido a mi configuración de permisos')
    except discord.HTTPException:
        await ctx.send('Hubo un error al intentar expulsar a ese miembro. Por favor intenta de nuevo.')
        
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, no tienes permisos para usar este comando.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("No se encontró el usuario mencionado.")
        
@commands.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None, *, reason=None):
    if not member:
        await ctx.send("Debes mencionar al miembro que quieres banear. Ejemplo: `!ban @usuario razón`")
        return

    if not reason:
        await ctx.send(f"{ctx.author.mention}, debes proporcionar una razón para banear a {member.mention}.")
        return

    if ctx.author.top_role <= member.top_role:
        await ctx.send(f"No puedes banear a {member.mention} porque tiene un rol igual o superior al tuyo.")
        return

    try:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} ha sido baneado por {ctx.author.mention}. Razón: {reason}")
    except discord.Forbidden:
        await ctx.send("No tengo permisos para banear a ese miembro.")
    except discord.HTTPException:
        await ctx.send("Ha ocurrido un error al intentar banear al miembro.")
        
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, no tienes permisos para usar este comando.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("No se encontró el usuario mencionado.")
        
@commands.command()
@commands.has_permissions(administrator=True)
async def md(ctx, member: discord.Member=None, *, message=None):
    
    if not member:
        await ctx.send("Debes mencionar al miembro que quieres mandar un md. Ejemplo: `!md @usuario mensaje`")
        return
    
    if message is None:
        await ctx.send(f"{ctx.author.mention} debes escribir un mensaje para enviar.")
    else:
        try:
            await member.send(f"{message}")
            await ctx.send(f"El mensaje ha sido enviado a {member.mention}")
            
            # Esperar la respuesta del usuario en el chat donde se ejecutó el comando
            def check(m):
                return m.author == member and m.channel == ctx.channel

            response = await ctx.bot.wait_for("message", check=check)

            # Enviar la respuesta del usuario al mismo chat donde se ejecutó el comando
            await ctx.send(f"{member.mention} respondió: {response.content}")
        except:
            await ctx.send(f"No se pudo enviar el mensaje a {member.mention}")

@md.error
async def md_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, no tienes permisos para usar este comando.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("No se encontró el usuario mencionado.")

@commands.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member: discord.Member=None, *, razon=None):
    
    if not member:
        await ctx.send("Debes mencionar al miembro que quieres advertir. Ejemplo: `!warn @usuario razón`")
        return
    
    if not razon:
        await ctx.send(f"{ctx.author.mention}, debes proporcionar una razón para advertir a {member.mention}.")
        return
    
    if ctx.author.top_role <= member.top_role:
        await ctx.send(f"No puedes advertir a {member.mention} porque tiene un rol igual o superior al tuyo.")
        
    try:    
        # Agregamos la advertencia a la lista
        advertencias.append({
            "member": member,
            "razon": razon
            })
        # Enviamos el mensaje de advertencia
        await ctx.send(f"El usuario {member.mention} ha sido advertido por la siguiente razón: {razon}")
    except discord.Forbidden:
        await ctx.send("No tengo permisos para banear a ese miembro.")
    except discord.HTTPException:
        await ctx.send("Ha ocurrido un error al intentar banear al miembro.")

@warn.error
async def warn_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, no tienes permisos para usar este comando.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("No se encontró el usuario mencionado.")
        
def setup_administrator_commands(bot):
    bot.add_command(kick)
    bot.add_command(ban)
    bot.add_command(md)
    bot.add_command(warn)
