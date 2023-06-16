import xlsxwriter
import bot
def start_table(mouth1):

    workbook = xlsxwriter.Workbook('расход_топлива.xlsx')
    bold = workbook.add_format({'bold': True})
    counter = 2
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