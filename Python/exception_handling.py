
x = {"a": 1, "b": 2}

print(x)

try:
    print(x['c'])
except KeyError as e:
    print("Caught an exception.")

