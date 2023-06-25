def binary_array_to_number(arr):
    acc = 0
    for b in arr:
        acc = acc * 2 + b
    print(acc)

binary_array_to_number([0, 0, 0, 1])