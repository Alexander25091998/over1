
class MainSever:
    def __init__(self, login, password):
        print('MainSever.__init__')
        super().__init__()
        self.login = login
        self.password = password

    def main_save(self):
        print(f"[{self.login} - {self.password}]Основное сохранение: {self}")


class XlsxServer:
    def __init__(self):
        super().__init__()
        print('XlsxServer.__init__')
        # self.arg1 = arg1
        pass

    def save_to_exel(self):
        print(f"Сохранено в exel: {self}")


class DbServer:
    def __init__(self):
        super().__init__()
        print('DbServer.__init__')

        # pass

    def save_to_db(self):
        print(f"Сохранено в базу данных: {self}")


class Car(MainSever, XlsxServer, DbServer):
    def __init__(self, model, year):
        print('Car.__init__')
        parent = super()
        parent.__init__('login1', 'password1')
        self.model = model
        self.year = year

    def __repr__(self):
        return f'{self.model} {self.year}'


class Student(MainSever, DbServer, XlsxServer):
    def __init__(self, name, last_name):
        print('Student.__init__')
        parent = super()
        parent.__init__('login2', 'password2')
        self.name = name
        self.last_name = last_name

    def __repr__(self):
        return f'{self.name} {self.last_name}'


car = Car('Ferreri SF 900', 2018)
student = Student('Petrov', "Oleg")
to_save_elems = [car, student]

for elem in to_save_elems:
    elem.main_save()
    elem.save_to_db()
    elem.save_to_exel()

# print(Car.__mro__)
# print(Student.__mro__)
