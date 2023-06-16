import random


class Utils:
    ADMIN_ACCES = 'ADMIN_ACCES'
    SRUDENT_ACCES = 'SRUDENT_ACCES'



    @staticmethod
    def input_login_pass():
        login = input("Введите логин: ")
        passwod = input("Введите пароль: ")
        return login, passwod

    @staticmethod
    def check_is_regist(students, login, passsword):
        rez = None
        if login.lower() in students.keys():
            student = students[login.lower()]
            valid_passwod = student.password
            if passsword == valid_passwod:
                return student
        return rez

    @staticmethod
    def random_test():
        number1 = random.randint(1, 100)
        znak = ['+', '-', '*'][random.randint(0, 2)]
        number2 = random.randint(1, 100)
        quest = f'{number1} {znak} {number2}'
        return quest, eval(quest)