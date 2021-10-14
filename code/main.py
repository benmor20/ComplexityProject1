import multiprocessing
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.function_base import linspace
from schelling_base import City
from schelling_base import decorate_seg
import csv
import os
# from multiprocessing import Process, Queue, Pool, cpu_count
import multiprocessing as mp
import time


# city = City(50, r=3)
# city.draw()
# segs = [city.step() for i in range(10000)]
# plt.plot(segs)
# decorate_seg()
# plt.show()

# plt.figure()
# im = city.draw()

##########################################
# city = City(n=50, r = 7, square = False)

# # draw the initial grid
# plt.figure(figsize=(9,3))
# plt.subplot(1,3,1)
# city.draw(plot_show = False)

# # first update
# plt.subplot(1,3,2)
# for i in range(1000):
#     city.step()
# city.draw(plot_show = False)

# # second update
# plt.subplot(1,3,3)
# for i in range(1000, 2000):
#     city.step()
# city.draw(plot_show = False)

# plt.tight_layout()
# plt.show()

#################################

# city = City(50, r=7, square=False)
# print(city.kernel)
# plt.figure(1)
# city.draw()
# city.loop()
# plt.figure(2)
# city.draw()

##################################
# Test different radii over time

# nSteps = 10000
# radii = 7
# citySize = 50
# segs = np.zeros((nSteps, radii))
# for r in range(1, radii+1):
#     print("                                ", end = "\r")
#     city = City(citySize, r = r)
#     for s in range(nSteps):
#         segs[s, r-1] = city.step()
#         # print("Radius: " + str(r) + ", Steps: " + str(s), end = "\r")

# plt.plot(segs)
# plt.legend(range(1, radii+1))
# plt.show()

###################################

# nSteps = 2000
# radii = range(1, 5)
# # preferences = [0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
# preferences = [0.2, 0.3, 0.4, 0.5]
# citySize = 20
# # p_out = []
# # r_out = []
# # s_out = []
# output = []
# output_rows = []

# for p in preferences:
#     print("                                                                       ", end = "\r")
#     this_x_out = []
#     this_y_out = []
#     for r in radii:
#         city = City(citySize, r = r)
#         for s in range(nSteps):
#             city.step(threshold = p)
#         print("Preference: " + str(p) + ", Radius: " + str(r), end = "\r")
#         # this_p_out.append([r, np.mean(city.compute_percent_same())])
#         s = np.mean(city.compute_percent_same())
#         this_x_out.append(r)
#         this_y_out.append(s)
#         output_rows.append([p, r, s])
#     output.append((p, [this_x_out, this_y_out]))

# print(output)
# for o in output:
#     this_p = o[1]
#     plt.plot(this_p[0], this_p[1])
# plt.legend(preferences)
# plt.show()

###############################
nSteps = 10000
radii = range(1, 8)
preferences = [0.2, 0.25, 0.3, 0.31, 0.32, 0.325, 0.33, 0.34, 0.35, 0.4, 0.45, 0.5]
# preferences = [0.2, 0.3, 0.4, 0.5]
citySize = 100 # paper uses 50
output_rows = []

def calculate_s(r, pref, i):
    # For a given radius and preference, run the simulation
    # i is for troubleshooting, doesn't do anything
    city = City(citySize, r = r)
    s = city.loop_until_done(threshold = pref, max_steps=nSteps)
    # s = np.mean(city.compute_percent_same())
    print("Preference: " + str(pref) + ", Radius: " + str(r) + ", I: " + str(i))
    return [pref, r, s, citySize, nSteps]

#instead of doing 5 identical tasks, just loop within calculate_s

if __name__ == "__main__":
    params = []
    for i in range(1): # Make an array of tuples of all combinations of input arguments
        for r in radii:
            for pr in preferences:
                params.append((r, pr, i))
    
    with mp.Pool() as pool: # have the pool map each tuple onto calculate_s arguments
        # Starmap is just unpacking the tuple into multiple arguments
        # This will complete the operation with an optimal number of pool workers,
        # making use of all CPU cores.
        output_rows = pool.starmap(calculate_s, params)
                
    # Sort and add header to the list
    output_rows.sort()
    headers = ["preference","radius","segregation","city_size","num_steps"]
    output_rows.insert(0, headers)
    print(output_rows)
    
    # Write the output list to CSV
    wd = os.path.dirname(__file__)
    path = os.path.join(wd, "data", "data2.csv")
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(output_rows)
