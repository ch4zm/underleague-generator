import random
import unittest
from underleague_generator.splortsleague import SplortsLeagueGenerator


class TestSplortsLeague(unittest.TestCase):
    def test_splorts_league_generator(self):
        random.seed(420)
        slg = SplortsLeagueGenerator()

        random.seed(420)
        res = slg.generate()

        league_names = ['Chaotic', 'Lawful']
        division_names = ['Knowledge', 'Revelation']
        for league_name in league_names:
            self.assertIn(league_name, res.keys())
            for division_name in division_names:
                self.assertIn(division_name, res[league_name])

        self.assertIn('Westport Coattails', res['Chaotic']['Knowledge'])

    def test_extract_leagues_divisions_teams(self):
        random.seed(420)
        slg = SplortsLeagueGenerator()

        random.seed(420)
        res = slg.generate()

        league_names, division_names, team_names = SplortsLeagueGenerator.extract_leagues_divisions_teams(res)
        self.assertIn('Chaotic', league_names)
        self.assertIn('Knowledge', division_names)
        self.assertIn('Cedar City Sweatsocks', team_names)
