class Animal:
    def __init__(self):
        print("Animal - __init__")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog - __init__")



class Ovcharka(Dog):
    def __init__(self):
        super().__init__()
        print("Ovcharka - __init__")



ovcharka = Ovcharka()

# Animal - __init__
# Dog - __init__
# Ovcharka - __init__