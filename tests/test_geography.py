import random
import unittest
from underleague_generator.geography import (
    StatesGeneratorBase,
    StatesGenerator,
    BigStatesGenerator,
    SmallStatesGenerator,
    CitiesGeneratorBase,
    CitiesGenerator,
    BigCitiesGenerator,
    SmallTownsGenerator,
)


class TestGeography(unittest.TestCase):

    def test_states_generator_base(self):
        sg = StatesGeneratorBase(country_code="usa")
        # Calling generate() should fail
        with self.assertRaises(AttributeError):
            sg.generate(size=50)

    def test_states_generator(self):
        random.seed(420)
        sg = StatesGenerator(country_code="usa")
        res = sg.generate(size=10)
        self.assertIn("Texas", res)

    def test_small_states_generator(self):
        random.seed(420)
        ssg = SmallStatesGenerator(country_code="usa")
        res = ssg.generate(size=10)
        self.assertIn("Wyoming", res)

    def test_big_states_generator(self):
        random.seed(420)
        bsg = BigStatesGenerator(country_code="usa")
        res = bsg.generate(size=10)
        self.assertIn("California", res)
    
    def test_cities_generator(self):
        random.seed(420)
        cg = CitiesGenerator(country_code="usa")
        res = cg.generate(size=10)
        self.assertIn("Danbury", res)

    def test_small_towns_generator(self):
        random.seed(420)
        cg = SmallTownsGenerator(country_code="usa")
        res = cg.generate(size=10)
        self.assertIn("Cold Spring Harbor", res)

    def test_big_cities_generator(self):
        random.seed(420)
        cg = BigCitiesGenerator(country_code="usa")
        res = cg.generate(size=10)
        self.assertIn("Anchorage", res)
