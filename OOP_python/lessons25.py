from dataclasses import dataclass, field


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"name: {self.name}, age: {self.age}"
#
#     # def __str__(self):
#     #     return f"name: {self.name}, age: {self.age}"
@dataclass(frozen=True)
class Person:
    name: str
    age: int = 28
#     значение по умолчанию
    child = []


person = Person('Андрей', 25)
print(person)
print(person.age)
person2 = Person(person.name,26)
print(person2)
# Person(name='Андрей', age=23)
# 23
# Person(name='Андрей', age=27)
print('='*80)


class Person:
    def __init__(self, name, age, childs=[]):
        self.name = name
        self.age = age
        self.childs = childs

    def __repr__(self):
        return f"name: {self.name}, age: {self.age}"

#     # def __str__(self):
#     #     return f"name: {self.name}, age: {self.age}"
@dataclass(frozen=True)
class Person:
    name: str
    age: int = 28
#     значение по умолчанию
    child: list = field(default_factory=list)


person = Person('Андрей', 25)
person.child.append("Mixa")
print(person)
print(person.age)
person2 = Person("Василий", 26)
person2.child.append("Nikita")
print(person2)
# Person(name='Андрей', age=25, child=['Mixa'])
# 25
# Person(name='Василий', age=26, child=['Nikita'])