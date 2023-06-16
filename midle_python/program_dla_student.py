import datetime
import random
import xlsxwriter
import pandas

import os
# import openpyxl
# from openpyxl import load_workbook
# from openpyxl.worksheet.formula import ArrayFormula

STUDENT_FILE = 'marks.xlsx'
ADMIN_ACCES = 'ADMIN_ACCES'
SRUDENT_ACCES = 'SRUDENT_ACCES'
INVALID_CREDENTION = 'INVALID_CREDENTION'

logins = {
    'admin': ('12345', ADMIN_ACCES),
    'мария': ('12345', SRUDENT_ACCES),
    'иван': ('12345', SRUDENT_ACCES),
    'александр': ('12345', SRUDENT_ACCES)
}

MENU = {
    ADMIN_ACCES: {
        1: 'Посмотреть оценки ученика',
        2: 'Посмотреть статистику 2',
        10: 'Выйти'
    },
    SRUDENT_ACCES: {
        1: 'Пройти тест',
        2: 'Посмотреть отметки',
        10: 'Выйти и сохраниться'

    }
}
students = {}


def check_is_regist():
    login = input("Введите логин: ")
    passwod = input("Введите пароль: ")
    if login.lower() in logins.keys():
        valid_passwod = logins[login.lower()][0]
        if passwod == valid_passwod:
            return logins[login.lower()][1], login
        else:
            return INVALID_CREDENTION, login
    else:
        return INVALID_CREDENTION, login


def random_test():
    number1 = random.randint(1, 100)
    znak = ['+', '-', '*'][random.randint(0, 2)]
    number2 = random.randint(1, 100)
    quest = f'{number1} {znak} {number2}'
    return quest, eval(quest)


def start_test(login):
    right_answer = 0
    for i in range(1, 6):
        try:
            question, answer = random_test()
            print(f'Реши пример: {question} ')
            user_answer = int(input('Ваш ответ: '))
            if answer == user_answer:
                right_answer += 1
        except Exception as e:
            print('Вы ввели не число')
            return start_test(login)

    mark = right_answer * 2
    if login in students:
        students[login].append((datetime.datetime.now(), mark))
    else:
        students[login] = [(datetime.datetime.now(), mark)]
    print(f'Твоя отметка: {mark}')


def save_date():
    workbook = xlsxwriter.Workbook(STUDENT_FILE)
    bold = workbook.add_format({'bold': True})

   workbook.close()


def look_answer_student():
    students_name = input('Введите имя ученика: ')
    if students_name in students.keys():
        to_print = f'Все оценки ученика: {students_name}\n'
        marks = students[students_name]
        for counter, mark in enumerate(marks):
            to_print += f'({counter}) {mark[1]} -> {mark[0]}\n'
        print("=" * 60)
        print(to_print)
        print("=" * 60)
    else:
        print(f"Студента с именем {students_name} не существует")


def look_answer_admin():
    students_name = input('Введите имя ученика: ')
    if students_name in students.keys():
        to_print = f'Все оценки ученика: {students_name}\n'
        marks = students[students_name]
        for counter, mark in enumerate(marks):
            to_print += f'({counter}) {mark[1]} -> {mark[0]}\n'
        print("=" * 60)
        print(to_print)
        print("=" * 60)
    else:
        print(f"Студента с именем {students_name} не существует")

# def statistic_admin():
#     students_name = input('Введите имя ученика: ')
#     if students_name in students:
#         wb = load_workbook(filename=STUDENT_FILE)
#         sheet_ranges = wb[f"{students_name}"]
#         sheet_ranges["C2"] = ArrayFormula("B2:B16", '=AVERAGE(B2:B16)')
#         print(sheet_ranges['C2'].value)
#     else:
#         print('Такого ученика нет')




def show_average_info():
    to_print = 'Средний бал всех учеников:\n'
    counter = 1
    by_school_marks_sum = 0
    by_school_marks_count = 0
    for name, marks in students.items():
        int_marks = list(map(lambda el: el[1], marks))
        to_print += f'{counter}. {name}: {sum(int_marks) / len(int_marks)}\n'
        counter += 1
        for mark in marks:
            by_school_marks_count += 1
            by_school_marks_sum += mark[1]
    to_print += f'Средний по школе {round(by_school_marks_sum / by_school_marks_count, 2)}, всего {by_school_marks_count} отметок'
    print(to_print)




def show_menu(access_role, login):
    while True:
        current_menu = MENU[access_role]
        print(current_menu)
        try:
            chosen_item = int(input('Выберите пункт меню: '))
            if access_role == SRUDENT_ACCES and chosen_item == 1:
                start_test(login)

            elif access_role == ADMIN_ACCES and chosen_item == 10:
                print('Программа завершила работу')
                return
            elif access_role == SRUDENT_ACCES and chosen_item == 10:
                print('Все данные сохранены')
                save_date()
                return
            elif access_role == SRUDENT_ACCES and chosen_item == 2:
                look_answer_student()
            elif access_role == ADMIN_ACCES and chosen_item == 1:
                look_answer_admin()
            elif access_role == ADMIN_ACCES and chosen_item == 2:
                show_average_info()
                # statistic_admin()
        except Exception as e:
            print('Вы ввели не правильный пункт')




def load_studets():
    if os.path.exists(STUDENT_FILE):
        xls_date = pandas.ExcelFile(STUDENT_FILE)
        for sheet in xls_date.sheet_names:
            df1 = pandas.read_excel(xls_date, sheet)
            marks = df1.values.tolist()
            students[sheet] = list(
                    map(
                        lambda el:
                        (
                           datetime.datetime(
                               year=int(el[0][:4]),
                               month=int(el[0][5:7]),
                               day=int(el[0][8:10]),
                               hour=int(el[0][11:13]),
                               minute=int(el[0][14:16]),
                               second=0
                           ),
                           el[1]),
                        marks
                    )
                )


def run_prog():
    load_studets()
    access_role, login = check_is_regist()
    if access_role != INVALID_CREDENTION:
        show_menu(access_role, login)
    else:
        print('Вы ввели не правильный пароль либо логин')
        return run_prog()

run_prog()
