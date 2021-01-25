import uuid
import os
import unittest
import tempfile
import underleague_generator
from underleague_generator.generics import (
    IterableDataLoader,
    UniformGenerator,
    BaseLinearBiasedGenerator,
    LinearBiasedGenerator,
    ReversedLinearBiasedGenerator,
)


class GenericsTests(unittest.TestCase):
    """
    Test generic data types and generators.
    """

    def random_data(self, size):
        return [str(uuid.uuid4()) for j in range(size)]

    def test_iterable_data_loader(self):
        data = self.random_data(100)
        i = IterableDataLoader(data)
        self.assertEqual(data, i.data)

    def check_generator(self, GenClass):
        nsamples = 100

        data = self.random_data(nsamples)
        g = GenClass(data=data)

        sample = g.generate()[0]
        self.assertIn(sample, data)

        sample = g.generate()[0]
        self.assertIn(sample, data)

        samples = g.generate(size=nsamples // 2)
        for sample in samples:
            self.assertIn(sample, data)

        with self.assertRaises(Exception):
            g.generate(size=nsamples + 1)

    def test_uniform_generator(self):
        class SampleUniformGenerator(IterableDataLoader, UniformGenerator):
            pass

        self.check_generator(SampleUniformGenerator)

    def test_base_linear_biased_generator(self):
        class SampleBaseLinearBiasedGenerator(
            IterableDataLoader, BaseLinearBiasedGenerator
        ):
            pass

        self.check_generator(SampleBaseLinearBiasedGenerator)

    def test_linear_biased_generator(self):
        class SampleLinearBiasedGenerator(IterableDataLoader, LinearBiasedGenerator):
            pass

        self.check_generator(SampleLinearBiasedGenerator)

    def test_reversed_linear_biased_generator(self):
        class SampleReversedLinearBiasedGenerator(
            IterableDataLoader, ReversedLinearBiasedGenerator
        ):
            pass

        self.check_generator(SampleReversedLinearBiasedGenerator)
