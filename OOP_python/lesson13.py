import time


def validate_age(min_age, max_age):
    def decoration(func):
        def inner(*args, **kwargs):
            new_args = []
            for arg in args:
                new_arg = None
                if type(arg) == int and arg >= min_age and arg <= max_age:
                    new_arg = arg
                new_args.append(new_arg)
            rez = func(*new_args, **kwargs)
            return rez
        return inner
    return decoration



@validate_age(min_age=1, max_age=90)
def regicter_age(age1, age2):
    print('Загружаем информацию')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('..')
    time.sleep(0.5)
    print('...')
    time.sleep(0.5)
    print('....')
    time.sleep(0.5)
    print(f'Возраст {age1}, {age2} сохранён в базу данных')


regicter_age(10, 10, 10)
