from collections.abc import Iterable
import random


class IterableDataLoader(object):
    def __init__(self, data):
        if isinstance(data, Iterable):
            self.data = data
        else:
            raise Exception(
                "Error: data provided to {self.__class__.__name__} was not iterable!"
            )


class UniformGenerator(object):
    def generate(self, size=1):
        """
        Sample data using uniform bias.
        Returns a list of the specified size.
        """
        if size > len(self.data) or size < 0:
            raise Exception(
                f"Error: generate method got size parameter {size}, must be between 0 and {len(self.data)}"
            )
        return random.choices(self.data, k=size)


class BaseLinearBiasedGenerator(object):
    """
    Returns a generator that will be linearly biased to return items from the top of the list.

    Example: a five-item list would have the following probabilities:

    blue    5 / (5+4+3+2+1) = 25%
    red     4 / ( ...     ) = 20%
    green   3 / ( ...     ) = 15%
    yellow  2 / ( ...     ) = 10%
    purle   1 / ( ...     ) = 5%
    """

    def generate(self, size=1, reverse=False):
        """
        Sample data using linear bias.
        Returns a list of the specified size.
        """
        if size > len(self.data) or size < 0:
            raise Exception(
                f"Error: generate method got size parameter {size}, must be between 0 and {len(self.data)}"
            )
        weights = list(range(1, len(self.data) + 1))
        if reverse:
            weights = reversed(weights)
        return random.choices(self.data, weights=weights, k=size)


class LinearBiasedGenerator(BaseLinearBiasedGenerator):
    """
    Generator that is linearly biased toward items at the front of the list
    """
    def generate(self, size=1):
        return super().generate(size, reverse=True)


class ReversedLinearBiasedGenerator(BaseLinearBiasedGenerator):
    """
    Generator that is linearly biased toward items at the back of the list
    """
    def generate(self, size=1):
        return super().generate(size, reverse=False)


class BaseLogBiasedGenerator(object):
    """
    Returns a generator that will be logarithmically biased to return items from top of list.
    Basically, each item has double the probability of occurring as the next item.

    Example: a five-item list would have the following probabilities:

    blue    2^5 / (2^1 + ... + 2^5) = 51%
    red     2^4 / (2^1 + ... + 2^5) = 25%
    green   2^3 / (2^1 + ... + 2^5) = 12%
    yellow  2^2 / (2^1 + ... + 2^5) = 6%
    purple  2^1 / (2^1 + ... + 2^5) = 3%
    """

    def generate(self, size=1, reverse=False):
        """
        Sample data using log bias.
        Returns a list of the specified size.
        """
        if size > len(self.data) or size < 0:
            raise Exception(
                f"Error: generate method got size parameter {size}, must be between 0 and {len(self.data)}"
            )
        weights = [2 ** j for j in range(1, len(self.data) + 1)]
        if reverse:
            weights = reversed(weights)
        return random.choices(self.data, weights=weights, k=size)


class LogBiasedGenerator(BaseLogBiasedGenerator):
    """
    Generator that is log biased toward items at the front of the list
    """
    def generate(self, size=1):
        return super().generate(size, reverse=True)


class ReversedLogBiasedGenerator(BaseLogBiasedGenerator):
    """
    Generator that is log biased toward items at the back of the list
    """
    def generate(self, size=1):
        return super().generate(size, reverse=False)
