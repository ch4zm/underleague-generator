import random
import unittest
from underleague_generator.splortsleague import SplortsLeagueGenerator


class TestSplortsLeague(unittest.TestCase):
    def test_splorts_league_generator(self):
        random.seed(420)
        slg = SplortsLeagueGenerator()

        random.seed(420)
        res = slg.generate()

        league_names = ["Chaotic", "Lawful"]
        division_names = ["Knowledge", "Revelation"]
        for league_name in league_names:
            self.assertIn(league_name, res.keys())
            for division_name in division_names:
                self.assertIn(division_name, res[league_name])

        self.assertIn("Westport Coattails", res["Chaotic"]["Knowledge"])

    def test_extract_leagues_divisions_teams_sim(self):
        league = {
            "Hot": {
                "Island": ["Aye Ones", "Bye Twos", "Cee Threes", "Dee Fours"],
                "Volcano": ["Eee Fives", "Fff Sixes", "Grr Sevens", "Hey Eights"],
            },
            "Cold": {
                "Island": ["I Nines", "Jay Tens", "Kay Elevens", "El Twelves"],
                "Volcano": [
                    "Em Thirteens",
                    "En Fourteens",
                    "Oh Fifteens",
                    "Pee Sixteens",
                ],
            },
        }
        (
            league_names,
            division_names,
            team_names,
        ) = SplortsLeagueGenerator.extract_leagues_divisions_teams(league)
        self.assertIn("Hot", league_names)
        self.assertIn("Cold", league_names)
        self.assertIn("Island", division_names)
        self.assertIn("Volcano", division_names)
        self.assertIn("Aye Ones", team_names)
        self.assertIn("Eee Fives", team_names)
        self.assertIn("El Twelves", team_names)

    def test_extract_leagues_divisions_teams_real(self):
        random.seed(420)
        slg = SplortsLeagueGenerator()

        random.seed(420)
        res = slg.generate()

        (
            league_names,
            division_names,
            team_names,
        ) = SplortsLeagueGenerator.extract_leagues_divisions_teams(res)
        self.assertIn("Chaotic", league_names)
        self.assertIn("Knowledge", division_names)
        self.assertIn("Cedar City Sweatsocks", team_names)

    def test_league_geo_type(self):
        # -----
        # Default (cities)
        random.seed(420)
        slg = SplortsLeagueGenerator(country_code="rus")

        random.seed(420)
        res = slg.generate()
        (
            league_names,
            division_names,
            team_names,
        ) = SplortsLeagueGenerator.extract_leagues_divisions_teams(res)
        self.assertIn('Chaotic', league_names)
        self.assertIn('Lawful', league_names)
        self.assertIn('Knowledge', division_names)
        self.assertIn('Revelation', division_names)
        self.assertIn('Satis Fighting Asparagus', team_names)
        self.assertIn('Pervoye Maya Gyroscopes', team_names)
        self.assertIn('Olginskaya Stevedores', team_names)

        # -----
        # States
        random.seed(420)
        slg = SplortsLeagueGenerator(country_code="rus", geo="states")

        random.seed(420)
        res2 = slg.generate(nleagues=4, ndivisions=4, teams_per_division=3)
        (
            league_names2,
            division_names2,
            team_names2,
        ) = SplortsLeagueGenerator.extract_leagues_divisions_teams(res2)
        self.assertIn('Peanut', league_names2)
        self.assertIn('Lentil', league_names2)
        self.assertIn('Spring', division_names2)
        self.assertIn('Summer', division_names2)
        self.assertIn('Moscow Parabolas', team_names2)
        self.assertIn('Khabarovsk Eight Tracks', team_names2)
        self.assertIn('Tomsk Frivolities', team_names2)

        # -----
        # Failure
        with self.assertRaises(Exception):
            SplortsLeagueGenerator(country_code="blah-blah-blah")

        with self.assertRaises(Exception):
            SplortsLeagueGenerator(geo="blah-blah-blah")

        gen = SplortsLeagueGenerator()
        with self.assertRaises(Exception):
            gen.generate(nleagues=1000)
            gen.generate(ndivisions=1000)
            gen.generate(nleagues=1000, ndivisions=1000)

