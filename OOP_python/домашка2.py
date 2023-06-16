import time


product_people = {}
money = 100


class Product:
    def __init__(self, product):
        self.product = product

    def __add__(self, other):
        if isinstance(other, int):
            return Product(self.product)
        elif isinstance(other, Product):
            new_products = {}
            for products, prise in self.product.items():
                if products not in new_products:
                    new_products[products] = prise

            for products, prise in other.product.items():
                if products not in new_products:
                    new_products[products] = prise
                    return Product(new_products)


product = Product({'Мясо': 5, 'Огурец': 3, 'Икра': 10, 'Помидор': 7, 'Хлеб': 4, 'Рыба': 8})
a = input('Введите название продукта: ')
b = int(input('Введите цену: '))
while True:
    product1 = Product({a: b})
    break
product += product1
print(product.product)


Menu = {
    1: "Онлан ветрина",
    2: "Общая сумма покупок",
    3: "Произвести оплату",
    4: "Проверить остаток на счету",
    5: "Выход"
}
PodMenu = {
    1: 'Выйти из прайс-листа'
}


def print_kass_bon():
    print(f"Сейчас выдаст чек за ваши продукты")
    time.sleep(1.5)
    print(f"""Общая стоимость продуктов]\n{product_people} ---> {sum(product_people.values())}""")


def to_pay_off():
    print(f"Ваша оплата прошла с вашего счёта спишут {sum(product_people.values())}")
    time.sleep(1.5)
    print(f"Оплата произошла успешно, на вашем счету осталось {money - sum(product_people.values())}")


def check_money():
    print(f"На вашем счету {money - sum(product_people.values())}")


def stop():
    print('Спасибо за покупкe, приходите к нам ещё')


def pr():
    print(Menu)
    ch = int(input('Выбери пукт который хотите: '))
    while True:
        if ch == 1:
            print(f"{product.product}||{PodMenu}")
            b = str.title(input('Выберите продукты которые хотите выбрать: '))
            if b == '1':
                return start()
            elif str(b):
                for a, prise in product.product.items():
                    if a == b:
                        product_people[a] = prise
                        print(f"Ваши продукты: {product_people}--->{sum(product_people.values())}")
        elif ch == 2:
            print_kass_bon()
            return pr()
        elif ch == 3:
            to_pay_off()
            return pr()
        elif ch == 4:
            check_money()
            return pr()
        elif ch == 5:
            stop()
            break


def start():
    pr()


start()
