import numpy as np
from schelling_base import City
import utils


class HomoHeteroCity(City):
    def __init__(self, n, r=1, square=False, color_probs=(0.1, 0.45, 0.45), hetero_prob=0.5):
        super().__init__(n, r, square, color_probs)
        self.make_grid(n, color_probs, hetero_prob)

    @property
    def grid(self):
        return self.array[:, :, 0]

    def make_grid(self, n, color_probs=(0.1, 0.45, 0.45), hetero_prob=0.5):
        super().make_grid(n, color_probs)
        grid = self.array.copy()
        hetero = np.random.random((n, n)) < hetero_prob
        self.array = np.zeros((n, n, 2))
        self.array[:, :, 0] = grid
        self.array[:, :, 1] = hetero

    @property
    def hetero(self):
        return self.array[:, :, 1]

    def find_unhappy(self, threshold=0.375):
        percent_same = self.compute_percent_same()
        unhappy_homo = (self.hetero == 0) & (percent_same < threshold)
        unhappy_hetero = (self.hetero == 1) & ((percent_same < threshold / 2) | (percent_same > 1 - threshold / 2))
        return utils.locs_where(unhappy_hetero) + utils.locs_where(unhappy_homo)

