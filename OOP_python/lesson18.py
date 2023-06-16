class Products:
    def __init__(self, products, bonuses=0):
        self.bonuses = bonuses
        self.products = products

    def get_ptoducts_prise(self):
        return sum(self.products.values()) - self.bonuses

    def del_bonuses(self):
        return sum(self.products.values())

    def __add__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonuses + other)
        elif isinstance(other, Products):
            new_products = {}
            for product, prise in self.products.items():
                if product not in new_products:
                    new_products[product] = prise
            for product, prise in other.products.items():
                if product not in new_products:
                    new_products[product] = prise
            return Products(new_products)

    def __radd__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonuses + other)

    def __sub__(self, other):
        new_products = {}
        if len(self.products) > len(other.products):
            for products, prises in other.products.items():
                for product, prise in self.products.items():
                    if product != products and prises != prise not in new_products:
                        new_products[product] = prise
        else:
            print(f"Вычитается меньшее от большего!!!{self.bonuses}")
        return Products(new_products)

    def __rsub__(self, other):
        if isinstance(other, int):
            return Products(self.products, other)


products1 = Products({'молоко': 3, 'сыр': 5})
print(f'Цена: {products1.get_ptoducts_prise()}: {products1.products}')
products2 = Products({"Кефир": 5})
products3 = products1 + products2
print(f'Цена: {products3.get_ptoducts_prise()}: {products3.products}')
products4 = 6 + products3
print(f'Цена: {products4.get_ptoducts_prise()}: {products4.products}')
print(f'Цена: {products4.del_bonuses()}: {products4.products}')
products5 = Products({"Колбоса": 8})
products6 = products4 + products5
print(f'Цена: {products6.get_ptoducts_prise()}: {products6.products}')
products7 = products6 - products5
print(f'Цена: {products7.get_ptoducts_prise()}: {products7.products}')



