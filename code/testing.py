from schelling_expansion import HomoHeteroCity


city = HomoHeteroCity(50)
print(city.loop_until_done())
city.draw()
