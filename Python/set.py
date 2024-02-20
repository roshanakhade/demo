
x = set()

x = {2, 1, 3, 5, 6, 6, 4}

print(x)

x = {"Mumbai", "Delhi", "Sambhajinagar", "Nagpur", 1.2}
#
# print(x)

x.add(7)

print(x)

x.add(6)

print(x)

# x.pop()
#
# print(x)
#
# x.pop()
#
# print(x)
#
# x.pop()
#
# print(x)

x.update({1, 2})

print(x)

y = {"Mumbai", 1.2, "Noida"}

print(x.union(y))

print(x.intersection(y))

print(y.issubset(x))

print(x.issuperset(y))