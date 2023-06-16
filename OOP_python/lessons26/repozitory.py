from abc import ABC, abstractmethod
import os
import pandas
import datetime
import json
from entities import Student
import xlsxwriter


class StudentsRepo(ABC):
    @abstractmethod
    def load_students(self):
        pass

    @abstractmethod
    def get_config(self):
        pass

    @abstractmethod
    def save_date(self, students):
        pass


class StudentsRepoXlsx(StudentsRepo):
    STUDENT_FILE = 'marks.xlsx'
    CONFIG_FILE_NAME = 'initial_config.json'

    def save_date(self, students):
        workbook = xlsxwriter.Workbook(self.STUDENT_FILE)
        bold = workbook.add_format({'bold': True})
        for student, data in students.items():
            worksheet = workbook.add_worksheet(student)
            worksheet.write('A1', 'Дата', bold)
            worksheet.write('B1', 'Отметка', bold)
            counter = 2
            for mark in data.marks:
                worksheet.write(f"A{counter}", str(mark[0])[:16])
                worksheet.write(f"B{counter}", mark[1])
                counter += 1
        workbook.close()

    def get_config(self):
        with open(self.CONFIG_FILE_NAME, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            return data

    def uppdate_wit_initiial_studets(self, students):
        new_students = {}
        initial_students = self.get_config()['users']

        for login, data in initial_students.items():
            if login in students:
                marks = students[login]
                student = Student(
                    name=login,
                    password=data['password'],
                    role=data['role'],
                    marks=marks
                )
            else:
                student = Student(
                    name=login,
                    password=data['password'],
                    role=data['role']
                )
            new_students[login] = student

        return new_students

    def load_students(self):
        students = {}
        if os.path.exists(self.STUDENT_FILE):
            xls_date = pandas.ExcelFile(self.STUDENT_FILE)
            for sheet in xls_date.sheet_names:
                df1 = pandas.read_excel(xls_date, sheet)
                marks = df1.values.tolist()
                students[sheet] = list(
                    map(
                        lambda el: (
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

        return self.uppdate_wit_initiial_studets(students)