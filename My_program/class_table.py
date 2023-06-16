import datetime
import xlsxwriter

km = []
table = {}
km1 = 'km1'
MOUTH = []

MENU = {
    km1: {
        1: 'Ввести данные',
        2: 'Посмотреть рассход',
        3: 'Посмотреть общий пробег',
        4: 'Посмотреть общее топливо',
        10: 'Выйти и сохранить'
    }
}


def start_table():
    mouth1 = input('Введите название месяца: ')
    workbook = xlsxwriter.Workbook('расход_топлива.xlsx')
    bold = workbook.add_format({'bold': True})
    counter = 2
    for date, mouth in km:
        worksheet = workbook.add_worksheet(f"{mouth1}")
        worksheet.write('A1', 'Начальный киллометраж', bold)
        worksheet.write('B1', 'Конечный киллометраж', bold)
        worksheet.write('C1', 'Стредний километраж', bold)
        worksheet.write('D1', 'Количество топлива', bold)
        worksheet.write('E1', 'Коефициент расхода', bold)
        worksheet.write('F1', 'Расход топлива на 100 км', bold)
        worksheet.write('G1', 'Дата', bold)
        for dates in date:
            worksheet.write(f'A{counter},  {int(input("Напиши начальный км: "))}')
            worksheet.write(f'B{counter},  {int(input("Напиши конечные км: "))}')
            worksheet.write(f'C{counter},  {int(input("Напиши литров км: "))}')
            counter += 1
    workbook.close()


def show_menu():
        start_table()
        current_menu = MENU.values()
        print(current_menu)
        try:
            chosen_item = int(input('Выберите пункт меню: '))
            if  chosen_item == 1:
                start_table()
            elif  chosen_item == 2:
                pass
            elif  chosen_item == 3:
                pass
            elif chosen_item == 4:
                pass
            elif chosen_item == 10:
                pass
        except Exception as e:
            print('Вы ввели не правильный пункт')

def write_date():
    pass



def start():
    show_menu()

start()

