def nb_year(p0, percent, aug, p):
    count = 1
    while True:
        abc = round(p0 + (p0 * (percent/100)) + aug)
        if abc >= p:
            break
        p0 = abc
        count += 1
    return count



nb_year(1500, 5, 100, 5000)
