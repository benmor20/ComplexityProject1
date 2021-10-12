import matplotlib.pyplot as plt
import numpy as np
from schelling_base import City
from schelling_base import decorate_seg


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
nSteps = 10000
radii = 7
citySize = 100
segs = np.zeros((nSteps, radii))
for r in range(1, radii+1):
    print("                                ", end = "\r")
    city = City(citySize, r = r)
    for s in range(nSteps):
        segs[s, r-1] = city.step()
        print("Radius: " + str(r) + ", Steps: " + str(s), end = "\r")

plt.plot(segs)
plt.legend(range(1, radii+1))
plt.show()
