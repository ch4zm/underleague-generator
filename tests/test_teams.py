import random
import unittest
from underleague_generator.teams import (
    TeamNameGeneratorBase,
    TeamNameGenerator,
    LeagueDivisionNameGeneratorBase,
    LeagueNameGenerator,
    DivisionNameGenerator,
)


class TestTeams(unittest.TestCase):
    def test_team_name_generator_base(self):
        tg = TeamNameGeneratorBase()
        with self.assertRaises(Exception):
            tg.generate()

    def test_team_name_generator(self):
        tg = TeamNameGenerator()
        random.seed(420)
        res = tg.generate(size=4)
        self.assertIn("Nightmares", res)


class LeagueDivisionTest(unittest.TestCase):
    def test_league_division_name_generator_base(self):
        ldg = LeagueDivisionNameGeneratorBase()

    def test_league_name_generator(self):
        lg = LeagueNameGenerator()
        random.seed(420)
        res = lg.generate(size=4)
        self.assertIn('Peanut', res)
        res2 = lg.generate(size=16)
        self.assertIn('Whiskey', res2)

    def test_division_name_generator(self):
        dg = DivisionNameGenerator()
        random.seed(420)
        res = dg.generate(size=4)
        self.assertIn('Peanut', res)
        res2 = dg.generate(size=16)
        self.assertIn('Whiskey', res2)
