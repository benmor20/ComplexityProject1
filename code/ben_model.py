# -*- coding: utf-8 -*-
"""Project 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i4O1vY2kFWk7GIRSuuoJQUETyMi2BT2v

http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.1027.3357&rep=rep1&type=pdf
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from scipy.signal import correlate2d
import numba as nb

def decorate(**options):
    plt.gca().set(**options)
    plt.tight_layout()

# make a custom color map
brg = cm.get_cmap('brg', 512)
br_array = brg(np.linspace(0, 0.5, 256))
cmap_no_empty = ListedColormap(br_array)
cmap = ListedColormap(np.concatenate((np.ones((256, 4)), br_array)))

def draw(grid):
    """Draws the grid.
    
    grid: NumPy array
    """
    # Make a copy because some implementations
    # of step perform updates in place.
    a = grid.copy()
    n, m = a.shape
    plt.axis([0, m, 0, n])
    plt.xticks([])
    plt.yticks([])

    options = dict(interpolation='none', alpha=0.8)
    options['extent'] = [0, m, 0, n]
    return plt.imshow(a, cmap if (grid == -1).sum() > 0 else cmap_no_empty, **options)



"""# New Section"""

def make_city(n, p_empty=0.1):
  choices = np.array([0, 1], dtype=np.int8)
  probs = [p_empty, 1 - p_empty]
  empty_city = np.random.choice(choices, (n, n), p=probs)
  full_city = np.random.rand(n, n)
  return (empty_city - 1) + full_city * empty_city

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

city = np.arange(1,10).reshape(3,3)
print(city)
draw(city)
plt.show()

kernel = np.array([[0.125, 0.125, 0.125],
                   [0.125, -1.00, 0.125],
                   [0.125, 0.125, 0.125]])
corr = correlate2d(city, kernel, boundary='wrap', mode='same')
corr

@nb.njit
def get_avg_abs_diff(arr):
    n,m = arr.shape
    out = np.empty((n,m))
    for i in range(n):
        for j in range(m):
            a = max(0,i-1)
            b = i+2
            c = max(0,j-1)
            d = j+2
            neighbors = arr[a:b,c:d]
            empty = neighbors == -1
            out[i,j] = np.sum(np.abs(neighbors-arr[i,j]) * (1 - empty))/(neighbors.shape[0]*neighbors.shape[1] - 1 - np.sum(empty))
    return out

# Commented out IPython magic to ensure Python compatibility.
# %timeit correlate2d(make_city(10000), kernel)

# Commented out IPython magic to ensure Python compatibility.
# %timeit get_avg_abs_diff(make_city(10000))

city[0, 0] = -1
city[2, 2] = -1
get_avg_abs_diff(city)