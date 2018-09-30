from acb2csv.acb2csv import generate_players_csv, get_player_from_str


def get_players_csv(url: str):
    generate_players_csv(url)


def parse_player(data: str) -> {}:
    return get_player_from_str(data)
