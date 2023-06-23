def descending_order(num):
    list = []
    for i in str(num):
        list.append(i)
    list.reverse()
    rez = int(''.join(map(str, list)))
    print(f"Input:{num}, Output:{rez} ")

descending_order(123)
