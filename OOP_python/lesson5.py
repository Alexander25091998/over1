class Dog():
    def __new__(cls, *args, **kwargs):
        print(f'__new__ | {cls}')
        return super().__new__(cls)

    def __init__(self):
        print(f"__init__ | {self}")


dog1 = Dog()
print(dog1)
# __new__ | <class '__main__.Dog'>
# __init__ | <__main__.Dog object at 0x000001DAD805CF70>
# <__main__.Dog object at 0x000001DAD805CF70>

print("="* 80)


class DBconnector():
    dbconector = None
    def __new__(cls, *args, **kwargs):
        if DBconnector.dbconector is None:
            DBconnector.dbconector = super().__new__(cls)
        return DBconnector.dbconector

    def __init__(self, lodin, password):
        self.login = lodin
        self.password = password
    def save_date(self):
        print("Save date")

    def delete_date(self):
        print("Date delete")

    def __str__(self):
        return f"{self.login} | {self.password} | {id(self)}"

dbconeector1 = DBconnector('postgres1', 'postgres1')
dbconeector2 = DBconnector('postgres2', 'postgres2')

print(dbconeector1)
print(dbconeector2)\

# postgres1 | postgres1 | 2039438757456 разные id в памяти
# postgres2 | postgres2 | 2039438756928
# после создания __new__ ссылаются на один и тоже id в памяти
# postgres2 | postgres2 | 1793124259296
# postgres2 | postgres2 | 1793124259296
