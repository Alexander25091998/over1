import traceback


try:
    numbers = [1, 2, 3]
    print(numbers[10])
except Exception as e:
    print('У нас случилась ошибка')
    traceback.print_exc()
print('Конец програмы')
