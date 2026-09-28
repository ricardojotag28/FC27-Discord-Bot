from dataclasses import dataclass


@dataclass
class Player:
    name: str
    position: str
    overall: int = 0
    games_played: int = 0
    win_rate: float = 0.0
    goals: int = 0
    assists: int = 0
    average_rating: float = 0.0
    man_of_the_match: int = 0
    shot_success_rate: float = 0.0
    passes_made: int = 0
    pass_success_rate: float = 0.0
    tackles_made: int = 0
    tackle_success_rate: float = 0.0
    clean_sheets_def: int = 0
    clean_sheets_gk: int = 0
    red_cards: int = 0