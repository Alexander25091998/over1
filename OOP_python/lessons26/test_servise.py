import traceback
from utils import Utils
import datetime

class TestServise:
    RETURN_STATYS = "STOP"
    def __init__(self, repo):
        self.repo = repo

    @staticmethod
    def start_test(student):
        right_answer = 0
        for i in range(1, 6):
            try:
                question, answer = Utils.random_test()
                print(f'Реши пример: {question} ')
                user_answer = int(input('Ваш ответ: '))
                if answer == user_answer:
                    right_answer += 1
            except Exception as e:
                print('Вы ввели не число')
        mark = right_answer * 2
        student.marks.append((datetime.datetime.now(), mark))
        print(f'Твоя отметка: {mark}')

    @staticmethod
    def look_answer_student(student, students):
            to_print = f'Все оценки ученика: {student.name}\n'
            data = students[student.name]
            for counter, mark in enumerate(data.marks):
                to_print += f'{counter}. {mark[1]} -> {mark[0]}\n'
            print(f"{'=' * 80}\n{to_print}\n{'=' * 80}")

    @staticmethod
    def look_answer_admin(students_name, students):
        if students_name in students.keys():
            to_print = f'Все оценки ученика: {students_name}\n'
            data = students[students_name]
            for counter, mark in enumerate(data.marks):
                to_print += f'{counter}. {mark[1]} -> {mark[ 0]}\n'
            print(f"{'='*80}\n{to_print}\n{'='*80}")
        else:
            print(f"{'=' * 80}\nСтудента с именем {students_name} не существует\n{'=' * 80}")

    @staticmethod
    def show_average_info(students):
        to_print = 'Средний бал всех учеников:\n'
        counter = 1
        by_school_marks_sum = 0
        by_school_marks_count = 0
        for name, data in students.items():
            int_marks = list(map(lambda el: el[1], data.marks))
            to_print += f"{counter}. {name}: {sum(int_marks) / len(int_marks) if len(int_marks) != 0 else 'Нет отметок'}\n"
            counter += 1
            for mark in data.marks:
                by_school_marks_count += 1
                by_school_marks_sum += mark[1]
        to_print += f'Средний по школе {round(by_school_marks_sum / by_school_marks_count, 2)}, всего {by_school_marks_count} отметок'
        to_print = f"{'='*80}\n{to_print}\n{'='*80}"
        print(to_print)

    def students_menu(self, student, students):
        chosen_item = input('Выберите пункт меню: ')
        if chosen_item == "1":
            TestServise.start_test(student)
        elif chosen_item == "2":
            self.look_answer_student(student, students)
        elif chosen_item == "10":
            print('Все данные сохранены')
            self.repo.save_date(students)
            return self.RETURN_STATYS


    def admins_menu(self, students):
        chosen_item = input('Выберите пункт меню: ')
        if  chosen_item == "1":
            self.show_average_info(students)
        elif chosen_item == "2":
            student_name = input('Введиет имя ученика: ').lower()
            self.look_answer_admin(student_name, students)
        elif chosen_item == "10":
            print('Программа завершила работу')
            return self.RETURN_STATYS

    def show_menu(self, students, student, config):
        while True:
            current_role = student.role
            current_menu = config[current_role]
            print(current_menu)
            try:
                if current_role == Utils.SRUDENT_ACCES:
                    rez = self.students_menu(student, students)
                elif current_role == Utils.ADMIN_ACCES:
                    rez = self.admins_menu(student, students)
                else:
                    rez == self.RETURN_STATYS
                if rez == self.RETURN_STATYS:
                    return
            except Exception as e:
                traceback.print_exc()
                print('Вы ввели не правильный пункт')

    def try_to_show_menu(self, students, student, config):
        self.show_menu(students, student, config) if student is not None else print('Ты не смог залогиниться в программе')


