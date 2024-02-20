import time

# x = [1, 2, 3, 4, 3, 6, 7]

# for element in x:
#     print(element)

# for i in range(1, 11):
#     print(i)

i = 0
while True:
    print(i)
    i = i + 1
    if i == 10:
        break
    if i == 5:
        continue
    time.sleep(1)
    print("I am {}".format(i))
