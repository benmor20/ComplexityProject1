from schelling_base import City
from schelling_expansion import HomoHeteroCity
import numpy as np
from matplotlib import pyplot as plt


radii = [1, 4, 7]
steps = (0, 500, 1000)
ts = [0.2, 0.3, 0.4]

for t in ts:
    for ri, r in enumerate(radii):
        city = City(50, r=r)
        current_steps = 0
        for si, step in enumerate(steps):
            while current_steps < step:
                city.step(threshold=t)
                current_steps += 1
            index = ri * len(steps) + si + 1
            plt.subplot(len(radii), len(steps), index)
            if index == ri * len(steps) + 1:
                plt.ylabel(f'Radius = {r}')
            if index > (len(radii) - 1) * len(steps):
                plt.xlabel(f'Steps = {step}')
            if index == len(steps) // 2 + 1:
                plt.title(f'Segregation of Cities with Differing Vision, threshold={t}')
            city.draw(plot_show=False)
        print(f'Finished {t}, {r}')
    plt.show()
