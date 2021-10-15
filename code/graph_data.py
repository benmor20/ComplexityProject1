import matplotlib.pyplot as plt
import pandas as pd
import os

wd = os.path.dirname(__file__)
path = os.path.join(wd, "data", "data2.csv")

data = pd.read_csv(path) # load csv
data = data.groupby(by = ["preference", "radius"]).mean() # take mean by preference and radius
data = data.reset_index() # can't figure out how to unset only 1 index
data = data.set_index("radius") # set index to radius
print(data)

# group data by preference, take segregation column, and plot
data.groupby("preference")["segregation"].plot(x = "radius", y = "segregation", legend = True)
plt.show()