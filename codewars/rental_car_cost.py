def rental_car_cost(d):
    if d < 3:
        a = d * 40
        return a
    elif 3 <= d < 7:
        a = d * 40 - 20
        return a
    elif d >= 7:
        a = d * 40 - 50
        return a


rental_car_cost(7)
