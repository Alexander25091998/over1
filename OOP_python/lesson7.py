class Point():
    min = -100
    max = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y


point1 = Point(20, 90)
print(point1.x)
print(point1.y)
point1.x = 1000
point1.y = 1000
print(point1.x, point1.y)
# 20
# 90
# 1000 1000
print("="*80)
print("Protected")
class Point():
    min = -100
    max = 100

    def __init__(self, x, y):
        self._x = x
        self._y = y


point1 = Point(20, 90)
print(point1._x)
print(point1._y)
point1._x = 1000
point1._y = 1000
print(point1._x, point1._y)
# Protected
# 20
# 90
# 1000 1000

print("="*80)
print("Privat")
class Point():
    min = -100
    max = 100

    def __init__(self, x, y):
        self._x = x
        self._y = y

point1 = Point(20, 90)
print(dir(point1))
# Privat
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
# '_x', '_y', 'max', 'min']



# point1 = Point(20, 90)
# print(point1.__x)
# print(point1.__y)
# point1.__x = 1000
# point1.__y = 1000
# print(point1.__x, point1.__y)
# Privat
# Traceback (most recent call last):
#   File "C:\Users\saha1\PycharmProjects\pythonProject2\OOP_python\lesson7.py", line 54, in <module>
#     print(point1.__x)
# AttributeError: 'Point' object has no attribute '__x'
print("="*80)
class Point():
    min = -100
    max = 100
    DEFAULT_VALUE = 0

    @classmethod
    def __correct_value(self, value):
       return value if self.min <= value <= self.max else self.DEFAULT_VALUE

    def __init__(self, x, y):
        self.__x = self.__correct_value(x)
        self.__y = self.__correct_value(y)

    def set_x(self, x):
        self.__x = self.__correct_value(x)
    def set_y(self, y):
        self.__y = self.__correct_value(y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


point1 = Point(20, 90)
print(point1.get_x())
print(point1.get_y()),
point1.set_x(1000)
point1.set_y(50)
print(point1.get_x(), point1.get_y())
# 20
# 90
# 0 50