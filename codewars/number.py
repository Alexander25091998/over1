def number(bus_stops):
    a = []
    b = []
    for i in bus_stops:
        a.append(i[0])
        b.append(i[1])
    c = sum(a) - sum(b)
    print(c)




number([[10,0], [3,5], [5,8]])