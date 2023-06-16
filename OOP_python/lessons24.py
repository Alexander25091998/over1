from abc import ABC, abstractmethod

class BirthDay(ABC):
    @abstractmethod
    def get_nama(self):
        pass

    def print(self):
        print(f"Happe New Yer {self.get_nama()}")


class Car(BirthDay):
    def get_nama(self):
        return 'Машина'

class Cat(BirthDay):
    def get_nama(self):
        return 'Шарик'


class Dog(BirthDay):
    def get_nama(self):
        return 'Кица'

car = Car()
dog = Dog()
cat = Cat()
pritables = [car, dog, cat]
for obj in pritables:
    obj.print()