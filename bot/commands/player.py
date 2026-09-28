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

    embed = discord.Embed(
        title=f"⚽ {player_data.name}",
        description=(
            f"**{player_data.position.upper()}** · "
            f"Overall **{player_data.overall}**"
        )
    )

    embed.add_field(
        name="📊 Rendimiento",
        value=(
            f"Partidos: **{player_data.games_played}**\n"
            f"Victorias: **{player_data.win_rate}%**\n"
            f"Valoración: **{player_data.average_rating}**\n"
            f"MVP: **{player_data.man_of_the_match}**"
        ),
        inline=False
    )

    embed.add_field(
        name="⚽ Ataque",
        value=(
            f"Goles: **{player_data.goals}**\n"
            f"Asistencias: **{player_data.assists}**\n"
            f"Éxito de tiro: **{player_data.shot_success_rate}%**"
        ),
        inline=True
    )

    embed.add_field(
        name="🎯 Pases",
        value=(
            f"Completados: **{player_data.passes_made}**\n"
            f"Precisión: **{player_data.pass_success_rate}%**"
        ),
        inline=True
    )

    embed.add_field(
        name="🛡️ Defensa",
        value=(
            f"Tackles: **{player_data.tackles_made}**\n"
            f"Éxito: **{player_data.tackle_success_rate}%**\n"
            f"Clean sheets DEF: **{player_data.clean_sheets_def}**\n"
            f"Clean sheets GK: **{player_data.clean_sheets_gk}**"
        ),
        inline=False
    )

    embed.add_field(
        name="🟥 Disciplina",
        value=f"Tarjetas rojas: **{player_data.red_cards}**",
        inline=False
    )

    embed.set_footer(text="FC27 Clubs Pro · NEO CF")

    await interaction.response.send_message(embed=embed)