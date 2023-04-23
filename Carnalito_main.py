#Archivo main del bot de discord llamado "Carnalito"
#Este código importa la librería Discord.py y las funciones commands de esa librería.

import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from commands.recreational_commands import setup_recreation_commands
from commands.administrator_commands import setup_administrator_commands

from events.event_vrg import on_message

load_dotenv()
TOKEN = os.getenv('TOKEN')

# Se crean los intents para permitir ciertas funcionalidades del bot en el servidor.
intents = discord.Intents().all()

# Se crea la instancia del bot, definiendo el prefijo que se usará para invocar los comandos y los intents.
bot = commands.Bot(command_prefix='!', intents=intents)

# Se llaman a las funciones que configuran los comandos
setup_recreation_commands(bot)
setup_administrator_commands(bot)

# Se llama a los eventos
bot.add_listener(on_message)
 
# Se inicia la ejecución del bot con el token proporcionado.
bot.run(TOKEN)