class Dog():

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


dog1 = Dog("Tyzik", 4)
print(dog1.get_name(), dog1.get_age())
dog1.set_name("Tyzik2")
print(dog1.get_name(), dog1.get_age())
dog1.set_age(10)
print(dog1.get_name(), dog1.get_age())
# Tyzik 4
# Tyzik2 4
# Tyzik2 10
print("="*80)
class Dog():
    __MAX_AGE = 40
    __MIN_AGE = 0
    __MIN_LEN_NAME = 3
    __MAX_LEN_NAME = 20

    @classmethod
    def __check_age(cls, age):
        if type(age) != int:
            raise TypeError(f"Возраст может быть только числом, а получено: {age}")
        elif cls.__MIN_AGE <= age >= cls.__MAX_AGE:
            raise TypeError(f"Возраст не может быть таким: {age}")

    @classmethod
    def __check_name(cls, name):
        if type(name) != str:
            raise TypeError(f"Имя может быть только строкой , а получено: {name}")
        elif len(name) < cls.__MIN_LEN_NAME:
            raise TypeError(f"Имя должно находиться в диапазоне {cls.__MIN_LEN_NAME}, {cls.__MAX_LEN_NAME})")
        elif len(name) > cls.__MAX_LEN_NAME:
            raise TypeError(f"Имя выходит за диапазоне {cls.__MIN_LEN_NAME}, {cls.__MAX_LEN_NAME})")



    def __init__(self, name, age):
        self.__check_name(name)
        self.__check_age(age)
        self.__name = name
        self.__age = age


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__check_name(name)
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__check_age()
        self.__age = age




dog1 = Dog(input("ВВедите имя собаки: "), int(input('Ведите возраст собаки:')))
print(dog1.name, dog1.age)
dog1.name = input('Введите другое имя для собаки: ')
print(dog1.name, dog1.age)
dog1.age = input('Введите другой возраст: ')
print(dog1.name, dog1.age)
