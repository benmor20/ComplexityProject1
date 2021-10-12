import matplotlib.pyplot as plt
import numpy as np
from schelling_base import City


# grid = make_grid(n=10)
# city = City(25)
# city.draw()
# plt.show()
# segs = [city.step() for i in range(1000)]
# # plt.plot(segs)
# # decorate_seg()
# # plt.show()

# plt.figure()
# im = city.draw()
# plt.show()

##########################################
city = City(n=50, r = 7, square = False)

# draw the initial grid
plt.figure(figsize=(9,3))
plt.subplot(1,3,1)
city.draw(plot_show = False)

# first update
plt.subplot(1,3,2)
for i in range(1000):
    city.step()
city.draw(plot_show = False)

# second update
plt.subplot(1,3,3)
for i in range(1000, 2000):
    city.step()
city.draw(plot_show = False)

plt.tight_layout()
plt.show()

#################################

# city = City(50, r=7, square=False)
# print(city.kernel)
# plt.figure(1)
# city.draw()
# city.loop()
# plt.figure(2)
# city.draw()
