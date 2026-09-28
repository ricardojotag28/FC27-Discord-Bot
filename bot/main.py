import os

import discord
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


if not TOKEN:
    raise RuntimeError("No se encontró DISCORD_TOKEN en el archivo .env")


intents = discord.Intents.default()

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@tree.command(name="ping", description="Comprueba si el bot está funcionando")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!")

@client.event
async def on_ready():
    await tree.sync()
    print(f"Bot conectado como {client.user}")
    print("Comandos sincronizados.")

client.run(TOKEN)   