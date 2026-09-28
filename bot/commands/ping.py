import discord
from discord import app_commands


@app_commands.command(
    name="ping",
    description="Comprueba si el bot está funcionando"
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!")