import os

import discord
from discord import app_commands

from services.player_service import get_player


@app_commands.command(
    name="player",
    description="Muestra las estadísticas de un jugador"
)
@app_commands.describe(name="Gamertag del jugador")
async def player(interaction: discord.Interaction, name: str):

    club_id = int(os.getenv("FC27_CLUB_ID", "143739"))

    player_data = get_player(club_id, name)

    if player_data is None:
        await interaction.response.send_message(
            f"❌ No encontré al jugador **{name}** en el club."
        )
        return

    await interaction.response.send_message(
        f"**{player_data.name}**\n"
        f"Posición: {player_data.position}\n"
        f"Overall: {player_data.overall}\n"
        f"Partidos: {player_data.games_played}\n"
        f"Victorias: {player_data.win_rate}%\n"
        f"Goles: {player_data.goals}\n"
        f"Asistencias: {player_data.assists}\n"
        f"Valoración media: {player_data.average_rating}\n"
        f"MVP: {player_data.man_of_the_match}\n"
        f"Tiros: {player_data.shot_success_rate}%\n"
        f"Pases: {player_data.passes_made} ({player_data.pass_success_rate}%)\n"
        f"Tackles: {player_data.tackles_made} ({player_data.tackle_success_rate}%)\n"
        f"Clean sheets (DEF): {player_data.clean_sheets_def}\n"
        f"Clean sheets (GK): {player_data.clean_sheets_gk}\n"
        f"Tarjetas rojas: {player_data.red_cards}"
    )