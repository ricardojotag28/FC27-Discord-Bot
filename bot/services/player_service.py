from models.player import Player
from services.fc27_api import FC27API


api = FC27API()


def get_player(club_id: int, player_name: str) -> Player | None:
    stats = api.get_member_stats(club_id)

    player = stats[
        stats["name"].str.lower() == player_name.lower()
    ]

    if player.empty:
        return None

    data = player.iloc[0]

    return Player(
        name=data["playerName"],
        position=data["position"],
        overall=int(data["overall"]),
        games_played=int(data["gamesPlayed"]),
        win_rate=float(data["winRate"]),
        goals=int(data["goals"]),
        assists=int(data["assists"]),
        average_rating=float(data["averageRating"]),
        man_of_the_match=int(data["manOfTheMatch"]),
        shot_success_rate=float(data["shotSuccessRate"]),
        passes_made=int(data["passesMade"]),
        pass_success_rate=float(data["passSuccessRate"]),
        tackles_made=int(data["tacklesMade"]),
        tackle_success_rate=float(data["tackleSuccessRate"]),
        clean_sheets_def=int(data["cleanSheetsDef"]),
        clean_sheets_gk=int(data["cleanSheetsGK"]),
        red_cards=int(data["redCards"]),
    )