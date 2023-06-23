from itertools import groupby

def unique_in_order(string):
    list = []
    if string == str:
        for i in string:
            list.append(i)
    elif string == ['']:
        for i in string:
            print(i)
    rez = [el for el, _ in groupby(list)]
    return print(rez)

unique_in_order(['1122112223c22333'])
unique_in_order('1122112223c22333')
unique_in_order(('1122112223c22333'))
print(type('1122112223c22333'))
print(type(['1122112223c22333']))
print(type(('1122112223c22333')))
