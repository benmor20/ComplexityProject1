from schelling_base import City
import matplotlib.pyplot as plt

# For the draw function in schelling_base:
# plt.imshow(a, cmap = "gray", **options)

ax = plt.subplot(2,4,1)
city = City(n=15,r=1,square=True)
city.array = 1- city.kernel
city.draw(plot_show = False)
ax.set_title("Moore Kernel")

ax = plt.subplot(2,4,2)
city = City(n=15,r=1)
city.array = 1- city.kernel
city.draw(plot_show = False)
ax.set_title("R=1")

ax = plt.subplot(2,4,3)
city = City(n=15,r=2)
city.array = 1- city.kernel
city.draw(plot_show = False)
ax.set_title("R=2")

ax = plt.subplot(2,4,4)
city = City(n=15,r=3)
city.array = 1- city.kernel
city.draw(plot_show = False)
ax.set_title("R=3")

ax = plt.subplot(2,4,5)
city = City(n=15,r=4)
city.array = 1- city.kernel
city.draw(plot_show = False)
ax.set_title("R=4")

ax = plt.subplot(2,4,6)
city = City(n=15,r=5)
city.array = 1- city.kernel
city.draw(plot_show = False)
ax.set_title("R=5")

ax = plt.subplot(2,4,7)
city = City(n=15,r=6)
city.array = 1- city.kernel
city.draw(plot_show = False)
ax.set_title("R=6")

ax = plt.subplot(2,4,8)
city = City(n=15,r=7)
city.array = 1- city.kernel
city.draw(plot_show = False)
ax.set_title("R=7")

plt.show()