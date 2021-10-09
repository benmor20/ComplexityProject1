import numpy as np


def locs_where(condition):
    """Find cells where a boolean array is True.

    condition: NumPy array

    return: list of coordinate pairs
    """
    ii, jj = np.nonzero(condition)
    return list(zip(ii, jj))


def random_loc(locs):
    """Choose a random element from a list of tuples.

    locs: list of tuples

    return: tuple
    """
    index = np.random.choice(len(locs))
    return locs[index]