from Dog import DogDemo


obj1 = DogDemo.Dog('Fido')
obj2 = DogDemo.Dog('Buddy')
obj1.add_trick('roll over')
obj2.add_trick('play dead')
obj2.add_trick('jump')


print(obj1.name)
print(obj2.name)
print(obj1.tricks)
print(obj2.tricks)
