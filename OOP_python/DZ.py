def decorator_paswood(func):
    def date_paswood(*args, **kwargs):  # аргументы прибывают отсюда
        new_passwod = []
        for arg in args:
            passwod = None
            if len(arg) <= 8:
                print(f"{passwod} слишком короткий")
            else:
                print('Ok')
                passwod = arg
            new_passwod.append(passwod)
            rez = func(*new_passwod, **kwargs)
            return rez
    return date_paswood


@decorator_paswood
def print_passwod(passwod):
    if passwod == None:
        print('Пароль не правильный')
    else:
        print(f'Принимаю этот пароль {passwod} он нормальной длины')


print_passwod('NotPAs')
print('='* 80)
print_passwod('NotPAsswod')

# Вывод:
# None слишком короткий
# Пароль не правильный
# =================================================================
# Ok
# Принимаю этот пароль NotPAsswod он нормальной длины