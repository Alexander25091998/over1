list1 = list(range(1, 20))
print(list1)

list2 = []
for elem in list1:
    list2.append(elem * elem)
print(list2)
list3 = [elem for elem in list1]
print(list3)
list4 = [elem * elem for elem in list1]
print(list4)
def plus_2(elem):
    return elem + 2
print([plus_2(elem) for elem in list1])
print(list(map(lambda elem: plus_2(elem), list1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
# [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
# [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
print(100*'=')

dict1 = {elem: elem * elem for elem in list1}
print(dict1)

date = [
    'Milk',
    'Fich',
    'Meat'
]
print(date)
# ['Milk', 'Fich', 'Meat']
dict2 = {}
for el in date:
    dict2[el] = len(el)
print(dict2)
# {'Milk': 4, 'Fich': 4, 'Meat': 4}
print({word: len(word) for word in date})
# {'Milk': 4, 'Fich': 4, 'Meat': 4}
print({word: len(word) for word in date if len(word) > 4})
# {}
print(100*'=')
dict2 = {word: len(word) for word in date}
print(dict2)
print({word.upper(): word_len for word, word_len in dict2.items()})
# {'Milk': 4, 'Fich': 4, 'Meat': 4}
# {'MILK': 4, 'FICH': 4, 'MEAT': 4}
