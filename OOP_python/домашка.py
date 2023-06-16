# product = {
#     1: {'Meat': 5},
#     2: {"Bananna": 8},
#     3: {"Cheese": 9},
#     4: {"Baget": 5},
#     5: {"Brad": 8}
# # , "Bananna": 8, "Cheese": 9,"Chicken": 10, "Baget": 5, "Brad": 8
# }
# counter = 0
# for products in product:
#     product[counter] = products
# # print(product)
# # product = product + dict(6, {"Fiche": 10})
# # print(product)
# class Product:
#     def __init__(self, products, prise):
#         self.products = products
#         self.prise = prise
#
#     def save_date(self, products, prise):
#         products = product
#         for product in products:
#             products[product] = prise
#             return product
#
#
# a = Product('Meat', 8)
# print(a.save_date)
#
#
#
#
#         \

class Product:
    def __init__(self, name):
        self.name = name
        # self.prise = prise

    def __add__(self, other):
        # if isinstance(other, int):
        #     return Product(self.name)
        # elif isinstance(other, Product):
            product = {}
            new_products = {}
            counter = 1
            for product, prise in self.name.items():
                if product not in new_products:
                    new_products[product] = prise

            for product, prise in other.name.items():
                if product not in new_products:
                    new_products[product] = prise
                    return Product(new_products)
#             product[counter] = new_products
#             counter += 1
#             return product
#
#     def __radd__(self, other):
#         if isinstance(other, int):
#             return Product(self.name)
#
#     # def __str__(self):
#     #     return f"{self.name_fryct}"
#
fruct1 = Product({'Meat': 5})
print(fruct1.name)
fruct1 += Product({"Fich": 15})
print(fruct1.name)
class People:
    def check_ptoduct(self):
        return fruct1.name

    def save_product(self):
        people_product = {}

    def vibor(product):
        while True:
            if product in fruct1.name:






print(People.check_ptoduct())
# # , "Bananna": 8, "Cheese": 9,"Chicken": 10, "Baget": 5, "Braed": 8