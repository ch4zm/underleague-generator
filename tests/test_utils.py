import os
import random
import unittest
from underleague_generator.constants import GEO
from underleague_generator.utils import (
    get_city_country_codes,
    get_state_country_codes,
    get_cities_data_file_from_country_code,
    get_states_data_file_from_country_code,
    get_team_names_data_file,
    get_leagues_divisions_data_file,
    get_cities_count,
    get_states_count,
)

class TestUtils(unittest.TestCase):
    cc = ['usa', 'rus', 'fra', 'ger', 'can', 'mex', 'chi', 'chi', 'jpn', 'phi', 'ind', 'idn']

    def test_get_city_country_codes(self):
        all_ccc = get_city_country_codes()
        ccc = self.cc
        for cc in ccc:
            self.assertIn(cc, all_ccc)

    def test_get_state_country_codes(self):
        all_scc = get_state_country_codes()
        scc = self.cc
        for cc in scc:
            self.assertIn(cc, all_scc)

    def test_get_states_data_file_from_country_code(self):
        for cc in self.cc:
            our_path = os.path.join(GEO, f'{cc}_states.txt')
            their_path = get_states_data_file_from_country_code(cc)
            self.assertEqual(our_path, their_path)

    def test_get_cities_data_file_from_country_code(self):
        for cc in self.cc:
            our_path = os.path.join(GEO, f'{cc}.txt')
            their_path = get_cities_data_file_from_country_code(cc)
            self.assertEqual(our_path, their_path)
