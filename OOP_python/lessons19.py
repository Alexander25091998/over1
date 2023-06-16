class Products:
    def __init__(self, products, bonuses=0):
        self.bonuses = bonuses
        self.products = products

    def get_ptoducts_prise(self):
        return sum(self.products.values()) - self.bonuses

    def __str__(self):
        return f"Цена: {self.get_ptoducts_prise()}. {self.products}"

    def __eq__(self, other):
        return self.get_ptoducts_prise() == other.get_ptoducts_prise()

    def __gt__(self, other):
        return self.get_ptoducts_prise() > other.get_ptoducts_prise()

    def __ge__(self, other):
        return self.get_ptoducts_prise() >= other.get_ptoducts_prise()




products1 = Products({'Молоко': 3, 'Cыр': 5})
products2 = Products({"Кефир": 5})
products3 = Products({"Молоко": 3, "Сыр": 5})

print(products1 == products3)
print(products1 > products2)
print(products1 >= products3)
print(products1 != products3)
# True
# True
# True
# False
