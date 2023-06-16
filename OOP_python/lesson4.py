class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog('Tyzik', 4)
print(dog1.name)
print(dog1.age)
# Tyzik
# 4
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Dog {self.name}, emy {self.age} yaer"

dog1 = Dog('Tyzik', 4)
dog2 = Dog('Pyzik', 5)
print(dog1)
print(dog2)
# Dog Tyzik, emy 4 yaer
# Dog Pyzik, emy 5 yaer

class Dog():
    animal_type = "Dog"
    legs_num = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{Dog.animal_type} {self.name}, emy {self.age} yaer"

dog1 = Dog('Tyzik', 4)
dog2 = Dog('Pyzik', 5)
print(dog1)
print(dog2)
# Dog Tyzik, emy 4 yaer
# Dog Pyzik, emy 5 yaer
print(Dog.animal_type)
print(Dog.legs_num)
# Dog
# 4