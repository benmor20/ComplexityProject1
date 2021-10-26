from schelling_base import City
from schelling_expansion import HomoHeteroCity
import numpy as np
from matplotlib import pyplot as plt


phs = [0, 0.4, 0.8]
steps = (0, 500, 1000)
ts = [0.2, 0.3, 0.4]

for phi, ph in enumerate(phs):
    for ti, t in enumerate(ts):
        city = HomoHeteroCity(50, r=4, hetero_prob=ph)
        city.loop_until_done(threshold=t)
        index = phi * len(phs) + ti + 1
        plt.subplot(len(phs), len(ts), index)
        city.draw(plot_show=False)
        if index == phi * len(phs) + 1:
            plt.ylabel(f'% Hetero = {ph}')
        if index > len(phs) * (len(phs) - 1):
            plt.xlabel(f'Threshold = {t}')
        if index == len(ts) // 2 + 1:
            plt.title(f'Equilibrium States for Varying Cities')
        print(f'Finished {t}, {ph}')
plt.show()
