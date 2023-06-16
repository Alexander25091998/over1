class Animal:
    def __init__(self, name):
        self.name = name

    def do_sound(self):
        print("Звук животного")

    def get_name(self):
        print(f"Меня звоут: {self.name}")



class Dog(Animal):
    def do_sound(self):
        print('Собака лает Гав-Гав')

    def play_game(self):
        print('Я собака, я несу палку')


class Ovcharka(Dog):
    def ovcharka_metod(self):
        print('Метод только для овчарок')


# print(issubclass(Ovcharka, Dog))
# print(issubclass(Dog, Ovcharka))
#
# dog1 = Dog('Тузик')
# print(isinstance(dog1, Dog))
# print(isinstance(dog1, Ovcharka))


class superint(int):
    def __str__(self):
        return f"[{self.real}]"

print(superint(22) + superint(4))