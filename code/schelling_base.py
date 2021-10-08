import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from scipy.signal import correlate2d

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
    def __init__(self, n, probs = [0.1, 0.45, 0.45]):
        self.make_grid(n, probs)
        self.kernel = np.array([[1, 1, 1],
                                [1, 0, 1],
                                [1, 1, 1]], dtype=np.int8)

    def make_grid(self, n, probs):
        """Make an array with two types of agents.
        
        n: width and height of the array
        
        return: NumPy array
        """
        choices = np.array([0, 1, 2], dtype=np.int8)
        self.grid = np.random.choice(choices, (n, n), p=probs)

    def draw(self):
        """Draws the grid.
        
        grid: NumPy array
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
        return plt.imshow(a, cmap, **options)

    def compute_num_same(self):
        """For each cell, the number of same-color neighbors.
        
        grip: NumPy array
        
        return: new NumPy array
        """
        kernel = self.kernel
        red = self.grid==1
        blue = self.grid==2

        # count red neighbors, blue neighbors, and total
        options = dict(mode='same', boundary='fill')
        num_red = correlate2d(red, kernel, **options)
        num_blue = correlate2d(blue, kernel, **options)

        # Note: This is slightly different than Allen's original implementation
        # This uses the number of non-opposite people, so cells are comfortable
        # with no neighbors. Also uses a second np.where for reds, so that
        # red, blue, and empty are all distinguishable. There may be a better 
        # way to do this. 
        num_same = np.where(blue, 8-num_red, np.where(red, 8-num_blue, 8))
        
        return num_same

    def locs_where(self, condition):
        """Find cells where a boolean array is True.
        
        condition: NumPy array
        
        return: list of coordinate pairs
        """
        ii, jj = np.nonzero(condition)
        return list(zip(ii, jj))

    def random_loc(self, locs):
        """Choose a random element from a list of tuples.
        
        locs: list of tuples
        
        return: tuple
        """
        index = np.random.choice(len(locs))
        return locs[index]

    def move(self, source, dest):
        """Swap the agents at source and dest.
        
        grip: NumPy array
        source: location tuple
        dest: location tuple
        """
        
        self.grid[dest], self.grid[source] = self.grid[source], self.grid[dest]

    def step(self, threshold=3):
        """Simulate one time step.
        
        grid: NumPy array
        threshold: number of same-color neighbors needed to be happy

        return: average number of same-color neighbors
        """
        # grid = self.grid
        num_same = self.compute_num_same()

        unhappy_locs = self.locs_where(num_same < threshold)
        print(len(unhappy_locs))
        if(len(unhappy_locs) == 0):
            return num_same.mean()

        empty = (self.grid==0)
        empty_locs = self.locs_where(empty)

        source = self.random_loc(unhappy_locs)
        dest = self.random_loc(empty_locs)

        self.move(source, dest)

        # FILL THIS IN!
        num_same = self.compute_num_same()
        return num_same.mean()

# grid = make_grid(n=10)
# city = City(25)
# city.draw()
# plt.show()
# segs = [city.step() for i in range(1000)]
# # plt.plot(segs)
# # decorate_seg()
# # plt.show()

# plt.figure()
# im = city.draw()
# plt.show()

city = City(n=50)

# draw the initial grid
plt.figure(figsize=(9,3))
plt.subplot(1,3,1)
city.draw()

# first update
plt.subplot(1,3,2)
for i in range(1000):
    city.step()
city.draw()

# second update
plt.subplot(1,3,3)
for i in range(1000):
    city.step()
city.draw()

plt.tight_layout()
plt.show()
