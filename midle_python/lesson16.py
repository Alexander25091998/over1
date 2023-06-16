import xlsxwriter
import datetime

date_now = datetime.datetime.now()
print(date_now)
print(f'год: {date_now.year}')
print(f'месяцы: {date_now.month}')
print(f'недели: {date_now.weekday()}')
print(f'дни: {date_now.day}')
print(f'часы: {date_now.hour}')
print(f'минуты: {date_now.minute}')
print(f'секунды: {date_now.second}')

stydens = {
    'Петров': {
        'Математика':[
            (date_now - datetime.timedelta(days=5), 9),
            (date_now - datetime.timedelta(days=3), 7),
            (date_now - datetime.timedelta(days=1), 5),
        ],
        'Физика':[
            (date_now - datetime.timedelta(days=10), 9),
            (date_now - datetime.timedelta(days=1), 5),
            (date_now - datetime.timedelta(days=6), 3),
        ]
    },
    'Сидоров': {
        'Математика':[
            (date_now - datetime.timedelta(days=4), 5),
            (date_now - datetime.timedelta(days=2), 7),
            (date_now - datetime.timedelta(days=1), 5),
            (date_now, 5)

        ],
        'Физика':[
            (date_now - datetime.timedelta(days=5), 9),
            (date_now - datetime.timedelta(days=4), 10),
            (date_now - datetime.timedelta(days=2), 3),
            (date_now, 3),
        ]
    }
}
workbook = xlsxwriter.Workbook('оценки.xlsx')
worksheet = workbook.add_worksheet('Петров')
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'Дата', bold)
worksheet.write('B1', 'Математика', bold)
worksheet.write('C1', 'Физика', bold)

# Запись дат
worksheet.write('A2', str(date_now - datetime.timedelta(days=10))[:10])
worksheet.write('A3', str(date_now - datetime.timedelta(days=5))[:10])
worksheet.write('A4', str(date_now - datetime.timedelta(days=3))[:10])
worksheet.write('A5', str(date_now)[:10])

# Запись отметок
worksheet.write('B3', 9)
worksheet.write('B4', 3)
worksheet.write('B5', 8)


# Запись отметок
worksheet.write('C2', 9)
worksheet.write('C4', 7)
worksheet.write('C5', 8)

workbook.close()