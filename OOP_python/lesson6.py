class Point():
    min = -100
    max = 100
    def __init__(self, x, y):
        self.x = 0
        self.y = 0
        if self.min <= x <= self.max:
            self.x = x
        if self.min <= y <= self.max:
            self.y = y

    def __str__(self):
        return f"x:{self.x}, y:{self.y}"


point1 = Point(20, 30)
point2 = Point(10, 1001)
print(point1)
print(point2)
print(Point.min, Point.max)
# x:20, y:30
# x:10, y:0
# -100 100
print('='*80)

class Point():
    min = -100
    max = 100

    def __init__(self, x, y):
        self.x = 0
        self.y = 0
        if self.min <= x <= self.max:
            self.x = x
        if self.min <= y <= self.max:
            self.y = y

    @staticmethod
    def sam_point(p1, p2):
        return Point(p1.x+p2.x,
                     p1.y+p2.y)

    def __str__(self):
        return f"x:{self.x}, y:{self.y}"


point1 = Point(20, 30)
point2 = Point(10, 40)
point3 = Point.sam_point(point1, point2)
print(point1)
print(point2)
print(point3)
# x:20, y:30
# x:10, y:40
# x:30, y:70
print('='*80)

class Point():
    min = -100
    max = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # if self.min <= x <= self.max:
        #     self.x = x
        # if self.min <= y <= self.max:
        #     self.y = y

    @classmethod
    def sum_point_with_check(cls, p1, p2):
        rezault_x = p1.x+p2.x
        rezault_y = p1.y+p2.y
        return Point(
           rezault_x if rezault_x <= cls.max else cls.max,
           rezault_y if rezault_y >= cls.max else cls.max,
        )

    def __str__(self):
        return f"x:{self.x}, y:{self.y}"


point1 = Point(20, 90)
point2 = Point(10, 40)
point3 = Point.sum_point_with_check(point1, point2)
print(point1)
print(point2)
print(point3)
# x:20, y:90
# x:10, y:40
# x:30, y:130
