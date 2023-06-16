class Animal:
    def __init__(self, name):
        self.name = name

    def do_sound(self):
        print("Звук животного")

    def get_name(self):
        print(f"Меня звоут: {self.name}")



class Dog(Animal):
   def play_game(self):
        print('Я собака, я несу плаку')


class Ovcharka(Dog):
    def ovcharka_metod(self):
        print('Метод только для овчарок')


animal = Ovcharka('Неопознаное животное')
dog = Dog('Собака Фёдор')

dog.do_sound()
dog.get_name()

dog.ovcharkq_metod()
