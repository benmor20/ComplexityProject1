from schelling_base import City
from schelling_expansion import HomoHeteroCity
import numpy as np
from matplotlib import pyplot as plt


radii = [1, 4, 7]
steps = (0, 500, 1000)
ts = [0.2, 0.3, 0.4]

for ri, r in enumerate(radii):
    for ti, t in enumerate(ts):
        city = City(50, r=r)
        city.loop_until_done(threshold=t)
        index = ri * len(radii) + ti + 1
        plt.subplot(len(radii), len(ts), index)
        city.draw(plot_show=False)
        if index == ri * len(radii) + 1:
            plt.ylabel(f'Radius = {r}')
        if index > len(radii) * (len(radii) - 1):
            plt.xlabel(f'Threshold = {t}')
        if index == len(ts) // 2 + 1:
            plt.title(f'Equilibrium States for Varying Cities')
        print(f'Finished {t}, {r}')
plt.show()
