import os
import random
import tempfile
import unittest
from underleague_generator.players import (
    FirstNameGeneratorBase,
    FirstNameGenerator,
    LastNameGeneratorBase,
    LastNameGenerator,
    NameGenerator,
)


class TestPlayers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmpdir = tempfile.TemporaryDirectory()
        cls.tmp = cls.tmpdir.name
        if not os.path.exists(cls.tmp):
            os.mkdir(cls.tmp)

    def test_first_name_generator_base(self):
        fng = FirstNameGeneratorBase()
        with self.assertRaises(Exception):
            fng.generate()

    def test_last_name_generator_base(self):
        fng = LastNameGeneratorBase()
        with self.assertRaises(Exception):
            fng.generate()

    def test_first_name_generator(self):
        fng = FirstNameGenerator()
        random.seed(420)
        res = fng.generate(size=4)
        print(res)
        #self.assertIn("Nightmares", res)

    @classmethod
    def tearDownClass(cls):
        del cls.tmpdir
