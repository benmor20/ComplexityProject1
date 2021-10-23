from schelling_base import City
from schelling_expansion import HomoHeteroCity
import numpy as np
from matplotlib import pyplot as plt


city = HomoHeteroCity(50, r=7)
city.loop_until_done(max_steps=-1)
city.draw()
