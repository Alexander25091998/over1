import datetime
import time
class TimeWatching:
    @staticmethod
    def valideit_time(data):
        # if int(data) <= 24:
        # elif int(data) <= 60:
        # elif int(data) <= 60:
        # else:
        return data if int(data) <= 24 and int(data) <= 60 and int(data) <= 60 else 0

    def __set_name__(self, owner, name):
        self.name = '|' + name + '|'


    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, self.valideit_time(value))


class Time:
    hours = TimeWatching()
    minut = TimeWatching()
    second = TimeWatching()

    def __init__(self, hours, minut, second):
        self.hours = hours
        self.minut = minut
        self.second = second


time1 = Time(23, 15, 45)
print(time1.__dict__)
time1.hours = 18
print(time1.__dict__)
