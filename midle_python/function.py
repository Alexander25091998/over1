# 1. Написать функцию которая принимает 2 параметра:
# число часов и число минут и выводит число секунд на экран
def get_seconds(hours, minutes):
    hours = hours*3600
    minutes = minutes*60
    seconds = hours + minutes
    return seconds
print(get_seconds(1, 1))

# 2. Написать функцию которая принимает 2 параметра
# и возвращает список чисел от первого до второго
def get_range(from_number, to_number):
    number_range = range(from_number, to_number+1)
    numbers = list(number_range)
    return numbers

print(get_range(1, 9))

# 3. Написать функцию которая принимает список чисел и
# возвращает наибольшее из чисел, встроенные функции
# использовать нельзя
def get_max(numbers):
    max_number = numbers[0]
    for ele in numbers:
        if ele > max_number:
            max_number = ele
    return max_number
print(get_max([1, 20, 30, 500]))

