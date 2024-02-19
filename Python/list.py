cities = list()

cities = ["Mumbai", "Pune", "Kolkata", "Nagpur", "Mumbai"]

mini_cities = ['Gaziabad', 'Noida']

print(cities, type(cities))

print(cities[2:4])

cities.append('Delhi')

print(cities)

print(len(cities))

print(cities.count('Mumbai'))

cities.insert(2, "Nagar")

print(cities)

element = cities.pop(2)

print(element, cities)

element = cities.remove("Nagpur")

print(element, cities)

print(cities.index("Mumbai"))

cities.reverse()

print(cities)

# cities.clear()

# print(cities)

cities.extend(mini_cities)

print(cities)
