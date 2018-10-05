from bs4 import BeautifulSoup, Tag
from typing import List, Dict
import csv
import urllib.request


def generate_players_csv(url: str):
    content = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(content, 'html.parser')
    rows = soup.find_all('table', class_='estadisticasnew')[1].find_all('tr')
    team = ''
    players = []
    ends = 0
    for row in rows:
        if team == '':
            team = get_team(row.find('td', class_='estverdel'))
        elif is_end(list(row.strings)):
            PerformanceCSV.write(team, players)
            team = ''
            players = []
            ends += 1
            if ends == 2:
                break
        elif is_stats(list(row.strings)):
            players.append(get_player_from_tag(row))
    print('Process finished!!')


def get_team(tag: Tag) -> str:
    if tag is None:
        return ''
    raw = tag.string
    return raw[:raw.rindex(' ')].replace(' ', '_').upper()


def is_stats(raw: List[str]) -> bool:
    return len(list(filter(lambda x: x.isdigit(), raw))) > 0


def is_end(raw: List[str]) -> bool:
    return 'Equipo' in raw


def get_stat(stat: str, position: int = 0, separator: str = '/',) -> str:
    if stat.strip() != '':
        return stat.split(separator)[position]
    return stat.strip()


def get_percent(data: Dict[str,str], keyc: str, keyt: str) -> str:
    if data[keyc] == '':
        return ''
    return data[keyc] + '/' + data[keyt]


def get_player_from_tag(tag: Tag) -> {}:
    columns = tag.find_all('td')
    data = {
        '#': columns[0].string.strip(),
        'minutos': get_stat(columns[2].string, 0, ':'),
        'jugador': ' '.join(columns[1].find('a').string.split(', ')[::-1]),
        'pts': columns[3].string.strip(),
        'ast': columns[12].string.strip(),
        'rec': columns[13].string.strip(),
        'tap': columns[16].string.strip(),
        'twopc': get_stat(columns[4].string),
        'twopt': get_stat(columns[4].string, 1),
        'threepc': get_stat(columns[6].string),
        'threept': get_stat(columns[6].string, 1),
        'tlc': get_stat(columns[8].string),
        'tlt': get_stat(columns[8].string, 1),
        'reb': columns[10].string.strip(),
        'def': get_stat(columns[11].string, 0, '+'),
        'of': get_stat(columns[11].string, 1, '+'),
        'per': columns[14].string.strip(),
        'fpr': columns[19].string.strip(),
        'fpc': columns[20].string.strip(),
    }

    data['twoppercent'] = get_percent(data, 'twopc', 'twopt')
    data['threeppercent'] = get_percent(data, 'threepc', 'threept')
    data['tlpercent'] = get_percent(data, 'tlc', 'tlt')
    return data


def get_player_from_str(data: str):
    return get_player_from_tag(BeautifulSoup(data, 'html.parser').find('tr'))


class PerformanceCSV(object):
    properties = ['jugador', 'minutos', 'pts', 'reb', 'ast', 'rec', 'tap', 'twopc', 'twopt', 'twoppercent',
                  'threepc', 'threept', 'threeppercent', 'tlc', 'tlt', 'tlpercent', 'of', 'def', 'per', 'fpr', 'fpc']

    @staticmethod
    def write(team: str, players: []):
        with open(team + '.csv', 'w') as csv_file:
            writer = csv.writer(csv_file, dialect='unix')
            writer.writerow(PerformanceCSV.properties)
            for player in players:
                writer.writerow(map(lambda key: player[key], PerformanceCSV.properties))
