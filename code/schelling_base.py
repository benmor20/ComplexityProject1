import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from scipy.signal import correlate2d

import utils


palette = sns.color_palette('muted')
colors = 'white', palette[1], palette[0]
cmap = LinearSegmentedColormap.from_list('cmap', colors)

def decorate(**options):
    plt.gca().set(**options)
    plt.tight_layout()


def decorate_seg():
    decorate(xlabel='Number of steps',
             ylabel='Average number of same-color neighbors',
             title='Schelling model')


class City:
    def __init__(self, n, r=1, square=False, probs=(0.1, 0.45, 0.45)):
        self.grid = np.zeros((n, n))
        self.kernel = np.zeros((2*r+1, 2*r+1))
        self.make_grid(n, probs)
        self.make_kernel(r, square)

    def make_kernel(self, r, square=False):
        size = 2 * r + 1
        shape = (size, size)
        if square:  # Original kernel
            self.kernel = np.ones(shape, dtype=np.int8)
            self.kernel[r, r] = 0
        else: 
            # Variable radius kernel. I don't know how to do this with 2d list
            # comprehension stuff so I just for looped it. It also is only 
            # run once and kernel isn't very large.
            self.kernel = np.zeros(shape, dtype=np.int8)
            for i in range(0, 2*r+1):
                for j in range(0, 2*r+1):
                    # print(i, j)
                    manhattan_dist = abs(i-r) + abs(j-r)
                    self.kernel[i, j] = (manhattan_dist <= r) and (manhattan_dist != 0)

    def make_grid(self, n, probs):
        """Make an array with two types of agents.
        
        n: width and height of the array
        probs: probability of generating a 0, 1, or 2
        
        return: NumPy array
        """
        choices = np.array([0, 1, 2], dtype=np.int8)
        self.grid = np.random.choice(choices, (n, n), p=probs)

    def draw(self, plot_show = True):
        """
        Draws the grid.
        """
        # Make a copy because some implementations
        # of step perform updates in place.
        a = self.grid.copy()
        n, m = a.shape
        plt.axis([0, m, 0, n])
        plt.xticks([])
        plt.yticks([])

        options = dict(interpolation='none', alpha=0.8)
        options['extent'] = [0, m, 0, n]
        plt.imshow(a, cmap, **options)
        if(plot_show):
            plt.show()

    def compute_percent_same(self):
        """For each cell, the number of same-color neighbors as a
        percentage of the number of non-empty neighbors.
        
        return: new NumPy array
        """
        kernel = self.kernel
        non_empty = self.grid != 0
        red = self.grid == 1
        blue = self.grid == 2

        # count red neighbors, blue neighbors, and total
        options = dict(mode='same', boundary='wrap')
        num_not_empty = correlate2d(non_empty, kernel, **options)
        num_red = correlate2d(red, kernel, **options)
        num_blue = correlate2d(blue, kernel, **options)

        # Note: This is slightly different than Allen's original implementation
        # This uses the percent of neighbors that are the same - empty neighbors are essentially not counted
        # On the off chance of only empty neighbors, the cell is assumed to be completely happy
        total_neighbors = sum(self.kernel)
        np.seterr(divide='ignore', invalid='ignore')
        percent_same = np.where(num_not_empty == 0, 1,
                                np.where(blue, num_blue, np.where(red, num_red, num_not_empty)) / num_not_empty)
        return percent_same

    def move(self, source, dest):
        """Swap the agents at source and dest.

        source: location tuple
        dest: location tuple
        """
        
        self.grid[dest], self.grid[source] = self.grid[source], self.grid[dest]

    def step(self, threshold=0.375):
        """Simulate one time step.

        threshold: percent of same-color neighbors needed to be happy

        return: average percentage of non-opposite neighbors
        """
        percent_same = self.compute_percent_same()
        unhappy_locs = utils.locs_where(percent_same < threshold)
        if len(unhappy_locs) == 0:
            return percent_same.mean()

        empty_locs = utils.locs_where(self.grid == 0)
        source = utils.random_loc(unhappy_locs)
        dest = utils.random_loc(empty_locs)
        self.move(source, dest)

        percent_same = self.compute_percent_same()
        return percent_same.mean()

    def loop(self, num_steps=1000, threshold=0.375):
        for _ in range(num_steps):
            self.step(threshold)

    def loop_until_done(self, threshold = 0.375, max_steps = 10000):
        for i in range(max_steps):
            percent_same = self.compute_percent_same()
            unhappy_locs = utils.locs_where(percent_same < threshold)
            if len(unhappy_locs) == 0:
                return percent_same.mean()

            empty_locs = utils.locs_where(self.grid == 0)
            source = utils.random_loc(unhappy_locs)
            dest = utils.random_loc(empty_locs)
            self.move(source, dest)

        return percent_same.mean()

