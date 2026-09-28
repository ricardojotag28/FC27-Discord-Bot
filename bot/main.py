import os

import discord
from dotenv import load_dotenv
from commands.ping import ping
from commands.player import player


load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


if not TOKEN:
    raise RuntimeError("No se encontró DISCORD_TOKEN en el archivo .env")


intents = discord.Intents.default()

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
GUILD_ID = 1334972415071092738
GUILD = discord.Object(id=GUILD_ID)
tree.add_command(ping)
tree.add_command(player)



@client.event
async def on_ready():
    await tree.sync()
    print(f"Bot conectado como {client.user}")
    print("Comandos sincronizados.")

client.run(TOKEN)   