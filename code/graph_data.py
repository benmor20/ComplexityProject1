import matplotlib.pyplot as plt
import numpy as np
from numpy.core.function_base import linspace
import pandas as pd
import csv
import os

wd = os.path.dirname(__file__)
path = os.path.join(wd, "data", "data.csv")

data = pd.read_csv(path)
print(data)
data = data.set_index("radius")
data = data.groupby("preference")["segregation"]

data.plot(x = "radius", y = "segregation", legend = True)
plt.show()