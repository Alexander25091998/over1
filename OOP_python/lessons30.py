class Person:
    MAx_AGE = 0
    Min_AGE = 99
    data = []

    def __init__(self, name2, age):
        self.name = name2
        self.age = age

    def __repr__(self):
        return f"{self.name} {self.age}"


person1 = Person('Andrei', 27)
print(person1)
person2 = Person('Alex', 57)
print(person2)
print(person1.__dict__)
print(Person.__dict__)
print("="*80)
person1.data.append('1')
person1.data.append('2')
person1.data.append('3')
print(person1.data)
print(person2.data)