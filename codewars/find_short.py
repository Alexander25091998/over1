def find_short(s):
    ls = s.split()
    a = []
    for i in ls:
        a.append(len(i))
    ls = min(a)
    return ls


find_short("bitcoin take over the world maybe who knows perhaps")