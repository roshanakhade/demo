
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


obj1 = Dog('Fido')
obj2 = Dog('Buddy')
obj1.add_trick('roll over')
obj2.add_trick('play dead')
obj2.add_trick('jump')


print(obj1.name)
print(obj2.name)
print(obj1.tricks)
print(obj2.tricks)