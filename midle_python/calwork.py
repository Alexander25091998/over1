menu = {
    1: 'Использовать калькулятор',
    2: 'Показать все операции',
    10: 'Выход'
}
operation_log = []
FILE_NAME = '../primer.txt'


def calculate():
    numbers1 = int(input('Введите первое число: '))
    znak = input('Введите знак: ')
    numbers2 = int(input('Введите второе число: '))
    res = "Что-то пошло не поплану"
    if znak == '+':
        res = f"{numbers1} {znak} {numbers2} = {numbers1 + numbers2}"
    elif znak == '-':
        res = f"{numbers1} {znak} {numbers2} = {numbers1 - numbers2}"
    elif znak == '*':
        res = f"{numbers1} {znak} {numbers2} = {numbers1 * numbers2}"
    elif znak == '/':
        res = f"{numbers1} {znak} {numbers2} = {numbers1 / numbers2}"
    print(res)
    operation_log.append(res)


def show_operation():
    print("=" * 80)
    for counter, operation in enumerate(operation_log):
        print(f"{counter + 1}. {operation}".replace('\n', ''))
    print("=" * 80)


def run():
    with open(FILE_NAME, 'r') as file:
        operation_log.extend(file.readlines())
    while True:
        print("Меню: ", menu)
        choose_menu_item = int(input('Выберите пункт из списка: '))
        if choose_menu_item == 1:
            calculate()
        elif choose_menu_item == 2:
            show_operation()
        elif choose_menu_item == 10:
            with open(FILE_NAME, "w") as file:
                for operation in operation_log:
                    file.write(operation.replace('\n', '') + '\n')
            return
        else:
            print('Такого пункта в меню не существует')


run()