# class Counter:
#     def __init__(self):
#         self.count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         return self.count
#
#
# counter = Counter()
# print(counter())
# print(counter())
# print(counter())
# print(counter())
# print(counter())
# print(counter())

# 1
# 2
# 3
# 4
# 5
# 6

import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        rez = self.func()
        finish_time = time.time()
        print(f'отработала за {finish_time - start_time} секунд')
        return rez
@Timer
def do_any_action():
    print('1')
    time.sleep(0.5)
    print('2')
    time.sleep(0.5)
    print('3')
    time.sleep(0.5)
    print('4')
    time.sleep(0.5)
    print('5')


do_any_action()

# 1
# 2
# 3
# 4
# 5
# отработала за 2.0124595165252686 секунд