

def hands_washer(func):
    def inner(*args, **kwargs):
        print('Моем руки')
        res = func(*args, **kwargs)
        print('Моем руки')
        return res

    return inner


def not_hands_washer(func):
    def inner(*args, **kwargs):
        print('Мы не будем кушать')
        res = func(*args, **kwargs)
        print('Мы же не куашли')
        return res

    return inner


def clear_eat2(func, meal1, meal2):
    print('Моем руки')
    res = func(meal1, meal2)
    print('Моем руки')
    return res


@hands_washer
def eat(meal1, meal2):
    print(f'Кушаю: {meal1}, {meal2}')
    return 'Приём пиши закончен'

@not_hands_washer
def eat1(m1, m2):
    print(f"Я не хочу кушать: {m1}, {m2}")
    return 'Приём пиши закончен'

# clear_eat = hands_washer(eat)
# print(clear_eat('Мясо', 'Пюре'))
print(eat('Мясо', 'Пюре'))
print(eat1('Fich', 'Meat'))
# print(clear_eat2(eat, 'Мясо', 'Пюре'))


# Моем руки
# Кушаю: Мясо, Пюре
# Моем руки
# Приём пиши закончен
# Мы не будем кушать
# Я не хочу кушать: Fich, Meat
# Мы же не куашли
# Приём пиши закончен

