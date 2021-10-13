import matplotlib.pyplot as plt
import numpy as np
from numpy.core.function_base import linspace
from schelling_base import City
from schelling_base import decorate_seg
import csv
import os
from multiprocessing import Process, Queue
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
# citySize = 100
# segs = np.zeros((nSteps, radii))
# for r in range(1, radii+1):
#     print("                                ", end = "\r")
#     city = City(citySize, r = r)
#     for s in range(nSteps):
#         segs[s, r-1] = city.step()
#         print("Radius: " + str(r) + ", Steps: " + str(s), end = "\r")

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
preferences = [0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
# preferences = [0.2, 0.3, 0.4, 0.5]
citySize = 100

def calculate_s(queue, pref, r):
    city = City(citySize, r = r)
    city.loop(num_steps = nSteps, threshold = pref)
    s = np.mean(city.compute_percent_same())
    # print("                                                                       ", end = "\r")
    print("Preference: " + str(pref) + ", Radius: " + str(r))
    queue.put([pref, r, s])

def sortFunc(x):
    return(str(x[0]) + "," + str(x[1]))

if __name__ == "__main__":
    queue = Queue()

    # processes = [Process(target=calculate_s, args=(queue, p, r)) for p in preferences]
    processes = []
    for p in preferences:
        for r in radii:
            processes.append(Process(target=calculate_s, args=(queue, p, r,)))

    for p in processes:
        p.start()

    for p in processes:
        p.join()
    
    # alive = [p for p in processes if p.is_alive()]

    # while(len(alive) > 0):
    #     alive = [p for p in alive if p.is_alive()]
    #     print("                                                                       ", end = "\r")
    #     print("Alive: " + str(len(alive)))
    #     time.sleep(0.1)

    output_rows = [queue.get() for p in processes]

    output_rows.sort(key = sortFunc)
    print(output_rows)
    wd = os.path.dirname(__file__)
    path = os.path.join(wd, "data", "data.csv")
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(output_rows)
