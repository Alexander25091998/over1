def sum_array(a):
    for i in a:
        if i not in a:
            return 0
    b = sum(a)
    return b



sum_array([])