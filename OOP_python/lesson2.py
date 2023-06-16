class Cat():
    def __init__(self, name, age):
        self.age = age
        self.name = name
        print(f'Hello world, I cat {name}')

    def __del__(self):
        print(f"Кот {self.name} закончился")


cat1 = Cat('Вася', 3)
cat2 = Cat('Муся', 3)

print(cat1.name)
print(cat2.name)

print(cat1.__dict__)