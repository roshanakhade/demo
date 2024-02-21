
def func(**kwargs):
    for key, value in kwargs.items():
        print("{} = {}".format(key, value))


func(a=1, b=2, c=3, d=4)
