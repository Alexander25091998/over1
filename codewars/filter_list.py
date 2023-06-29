def filter_list(l):
    a = []
    b = []
    for i in l:
        if type(i) == int:
            a.append(i)
    return a

filter_list([1, 2, 'a', 'b'])