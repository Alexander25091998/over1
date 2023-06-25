from itertools import groupby

def longest(a1, a2):
    a = []
    for i in a1:
        a.append(i)
    for c in a2:
        a.append(c)
    a.sort()
    new = [el for el, _ in groupby(a)]
    s = ''.join(new)
    return s
    # "aehrsty"


longest("aretheyhere", "yestheyarehere")