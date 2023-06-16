# 1 / 0
import traceback


# def run_lichitng():
#     # try:
#         1 / 0
#         print('Свет включён')
#     # except Exception as e:
#     #     traceback.print_exc()
#
#
# def start_light():
#     print('Умный дом включен 2')
#     run_lichitng()
#
#
# def run():
#     print('Умный дом включен 1')
#     start_light()
#
# try:
#     run()
# except Exception as e:
#     traceback.print_exc()
#
# print('Program continue work')

class CustonExeption(Exception):
    pass
# этот метод делаеться для понимания ошибки в программе

try:
    raise CustonExeption('Errors program')
except Exception as e:
    # traceback.print_exc()
    print('Errors works')


