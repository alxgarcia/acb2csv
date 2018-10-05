from unittest import TestCase
from acb2csv import parse_player


class Parsing(TestCase):
    def test_parsing_player(self):
        data = """<tr>
                <td class="gris" width="15">3</td>
                <td class="naranjaclaro" width="103"><a href="/jugador.php?id=FOO">Pangos, Kevin</a></td>
                <td class="blanco" width="31">23:4</td>
                <td class="grisclaro" width="25">10</td>
                <td class="blanco" width="31">2/2</td>
                <td class="blanco" width="30">100%</td>
                <td class="grisclaro" width="31">2/2</td>
                <td class="grisclaro" width="30">100%</td>
                <td class="blanco" width="31">0/0</td>
                <td class="blanco" width="30">0%</td>
                <td class="grisclaro" width="20">1</td>
                <td class="grisclaro" width="31">0+1</td>
                <td class="blanco" width="20">8</td>
                <td class="grisclaro" width="20">0</td>
                <td class="blanco" width="20">1</td>
                <td class="grisclaro" width="20">0</td>
                <td class="blanco" width="20">0</td>
                <td class="blanco" width="20">0</td>
                <td class="grisclaro" width="20">0</td>
                <td class="blanco" width="20">1</td>
                <td class="grisclaro" width="20">3</td>
            </tr>""".replace("\n", "")
        player = parse_player(data)
        self.assertEqual('3', player['#'])
        self.assertEqual('23', player['minutos'])
        self.assertEqual('Kevin Pangos', player['jugador'])
        self.assertEqual('10', player['pts'])
        self.assertEqual('8', player['ast'])
        self.assertEqual('0', player['rec'])
        self.assertEqual('0', player['tap'])
        self.assertEqual('2', player['twopc'])
        self.assertEqual('2', player['twopt'])
        self.assertEqual('2', player['threepc'])
        self.assertEqual('2', player['threept'])
        self.assertEqual('0', player['tlc'])
        self.assertEqual('0', player['tlt'])
        self.assertEqual('1', player['of'])
        self.assertEqual('0', player['def'])
        self.assertEqual('1', player['per'])
        self.assertEqual('1', player['fpr'])
        self.assertEqual('3', player['fpc'])
