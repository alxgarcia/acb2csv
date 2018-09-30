import sys
from acb2csv import get_players_csv


def main():
    if len(sys.argv) < 2:
        print('Usage: acb2csv <url>')
        sys.exit(1)
    get_players_csv(sys.argv[1])
