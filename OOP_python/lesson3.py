#1
a, b, *c = ['a', 'b', 'c', 'd']
print(a)
print(b)
print(c)
# a
# b
# ['c', 'd']

a, *b, c = ['a', 'b', 'c', 'd']
print(a)
print(b)
print(c)
# a
# ['b', 'c']
# d

*a, b, c = ['a', 'b', 'c', 'd']
print(a)
print(b)
print(c)
# ['a', 'b']
# c
# d


#2
nums = [0, 10]
print(list(range(10)))
print(list(range(0, 5)))
print(list(range(*nums)))

#3
print(1, 2, 3)
# 1 2 3
print([1, 2, 3])
# [1, 2, 3]
print(*[1, 2, 3])
# 1 2 3

#4
def ab(a, b):
    print(a, b)
elems = ['a', 'b']
ab('a', 'b')
ab(*elems)
ab(*['a', 'b'])
# a b
# a b
# a b


#5
def super_sum(numbers):
    res = 0
    for number in numbers:
        res += number
        print(f"Sum = {res}")

super_sum([1, 2, 3, 4, 5])
# Sum = 1
# Sum = 3
# Sum = 6
# Sum = 10
# Sum = 15
def super_sum(*numbers):
    res = 0
    for number in numbers:
        res += number
        print(f"Sum = {res}")

super_sum(1, 2, 3, 4, 5)
# Sum = 1
# Sum = 3
# Sum = 6
# Sum = 10
# Sum = 15

#6
print(1, 2, 3, 4, 5)
# 1 2 3 4 5
print(1, 2, 3, 4, 5, sep='\n')
# 1
# 2
# 3
# 4
# 5

#7
def func(*args, **kwrgs):
    print(args)
    print(kwrgs)
func(1, 3, 4, 5, 'a', 'b', key1='123', key2='abc')
# (1, 3, 4, 5, 'a', 'b')
# {'key1': '123', 'key2': 'abc'}