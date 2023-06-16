import traceback

data = ['a', 'b', 'Andrei']
print(data[0])
print('-'*120)

# 1. Проверка количества элементов
if len(data) >= 6:
    print(data[6])
else:
    print('List not have object')
print('-'*120)
# 2. a. С обработкой исключений
try:
    print(data[6])
except:
    print('В списке меньше 6 элементов')
print('-'*120)

# b. С обработкой исключений
try:
    print(data[6])
except IndexError:
    print('В списке меньше 6 элементов')
print('-'*120)

# c. С обработкой исключений
try:
    print(data[6])
except:
    print('В списке меньше 6 элементов')
print('-'*120)

# c. С обработкой исключений
try:
    print(data[1])
except (ArithmeticError, IndexError):
    print('error')
except Exception as e:
    # Exception  в этом методе должен бывть указан последним, потому что он находиться выше в иррархии
    # traceback.print_exc()
    # этот метод позволяет не останавливать программу если есть в каком-то месте ошибка
    print('В списке меньше 6 элементов')
else:
    print('Error not have')
#     в этом случае будет выполняться когда нет ошибки
finally:
    print('Blok finally')
    # это оператор позволяет вывести значение в конце обработки
print('-'*120)

def f1(n1, n2):
    try:
        print('try')
        return n1 / n2
    except:
        print('exept')
        return 0
    finally:
        print('finally')

print(f1(2, 4))
