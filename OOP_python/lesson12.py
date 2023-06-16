import  time
import requests


def check_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        finish_time =time.time()
        print(f"Функция выполинлась за {finish_time - start_time} сек")
        return res

    return  inner

@check_time
def f1():
    print('12345')
    time.sleep(1)
    print('23434')



f1()
print('=' * 80)


@check_time
def fibonachi(num):
    if num in [1, 2]:
        return num
    return fibonachi(num - 1) + fibonachi(num - 2)


print(fibonachi(10))


@check_time
def f3():
    rez = requests.get('https://mvd.gov.by/ru/login')
    print()
f3()
