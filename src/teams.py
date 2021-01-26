from collections.abc import Iterable
import random
import os
from .generics import IterableDataLoader


HERE = os.path.abspath(os.path.dirname(__file__))
DATA = os.path.join(HERE, 'data')


class TeamNameGeneratorBase(IterableDataLoader):

class TeamNameGenerator(TeamNameGeneratorBase, UniformGenerator):
    pass
