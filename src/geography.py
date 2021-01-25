from collections.abc import Iterable
import random
import os
from .utils import (
    get_city_country_codes,
    get_state_country_codes,
    get_cities_data_file_from_country_code,
    get_states_data_file_from_country_code,
    get_cities_count,
    get_states_count,
)
from .generics import (
    IterableDataLoader,
    UniformGenerator,
    LinearBiasedGenerator,
    ReversedLinearBiasedGenerator,
    LogBiasedGenerator,
    ReversedLogBiasedGenerator,
)


class CitiesGeneratorBase(IterableDataLoader):
    """
    Base class that loads cities for a given country code
    """

    def __init__(self, **kwargs):
        if 'country_code' not in kwargs:
            raise Exception("Error: country_code is a required keyword argument")
        else:
            country_code = kwargs['country_code']
        if country_code not in get_city_country_codes():
            raise Exception(
                "Error: invalid country code {country_code} passed to {cls.__name__}"
            )
        cities_file = get_cities_data_file_from_country_code(country_code)
        with open(cities_file, "r") as f:
            data = f.readlines()
        data = [j.strip() for j in data if len(j.strip()) > 0]
        super().__init__(data)


class CitiesGenerator(CitiesGeneratorBase, UniformGenerator):
    """
    Generate random states uniformly
    """

    pass


class BigCitiesGenerator(CitiesGeneratorBase, LogBiasedGenerator):
    """
    Generate random cities with a log bias for big cities
    """

    pass


class SmallTownsGenerator(CitiesGeneratorBase, ReversedLinearBiasedGenerator):
    """
    Generate random cities with a linear bias for small towns
    """

    pass


class StatesGeneratorBase(IterableDataLoader):
    """
    Base class that loads states for a given country code
    """

    def __init__(self, **kwargs):
        if 'country_code' not in kwargs:
            raise Exception("Error: country_code is a required keyword argument")
        else:
            country_code = kwargs['country_code']
        if country_code not in get_state_country_codes():
            raise Exception(
                "Error: invalid country code {country_code} passed to {cls.__name__}"
            )
        states_file = get_states_data_file_from_country_code(country_code)
        with open(states_file, "r") as f:
            data = f.readlines()
        data = [j.strip() for j in data if len(j.strip()) > 0]
        super().__init__(data)


class StatesGenerator(StatesGeneratorBase, UniformGenerator):
    """
    Generate random states uniformly
    """

    pass


class BigStatesGenerator(StatesGeneratorBase, LinearBiasedGenerator):
    """
    Generate random states with a linear bias for big states
    """

    pass


class SmallStatesGenerator(StatesGeneratorBase, ReversedLinearBiasedGenerator):
    """
    Generate random states with a linear bias for small states
    """

    pass


