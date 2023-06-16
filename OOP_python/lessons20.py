class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.age))

    def __eq__(self, other):
        return self.age ==  other.age and self.name == other.name

dog1 = Dog('Шарик', 6)
dog2 = Dog('Шарик', 5)
dog3 = Dog('Шарик', 5)
print(hash(dog1))
print(hash(dog2))
print(hash(dog3))
print(dog1 == dog3)
print(dog2 == dog3)

date = {}
date[dog1] = '1'
date[dog2] = '2'
date[dog3] = '3'
print(date)

print(hash())

