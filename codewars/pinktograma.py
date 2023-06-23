import string
import re


def is_pangram(text):
    abc = list(string.ascii_lowercase)
    litr = []
    text = text.lower().replace(' ', '').replace('!', '').replace(',', '').replace('.', '').replace('?', '').replace('int', '')
    text = re.sub(r'\d', '', text)
    for i in abc:
        if i in text:
            litr.append(i)
    if litr == abc:
        print(True)
        return True
    else:
        print(False)
        return False








    # for elem in s:
    #     list_items.append(elem)
    # for el in list_items:
    #     if el != el:
    #         print('Является')
    #         return True
    #     else:
    #         print('Не Является')
    #         return False


is_program("1abcdefghijklmnopqrstuvwxyz")
#
# str = "The quick, brown fox jumps over the lazy dog!"
# s = str.lower() and str.replace(' ', '')
#
# print(len(s))
