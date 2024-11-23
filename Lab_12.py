class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return f"{self.__hours:02}:{self.__minutes:02}:{self.__seconds:02}"

    def next_second(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
        if self.__minutes == 60:
            self.__minutes = 0
            self.__hours += 1
        if self.__hours == 24:
            self.__hours = 0

    def previous_second(self):
        self.__seconds -= 1
        if self.__seconds == -1:
            self.__seconds = 59
            self.__minutes -= 1
        if self.__minutes == -1:
            self.__minutes = 59
            self.__hours -= 1
        if self.__hours == -1:
            self.__hours = 23

# Тестування
timer = Timer(23, 59, 59)
print(timer)  # 23:59:59
timer.next_second()
print(timer)  # 00:00:00
timer.previous_second()
print(timer)  # 23:59:59


class WeekDayError(Exception):
    pass


class Weeker:
    valid_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in Weeker.valid_days:
            raise WeekDayError("Sorry, I can't serve your request.")
        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        index = Weeker.valid_days.index(self.__day)
        new_index = (index + n) % 7
        self.__day = Weeker.valid_days[new_index]

    def subtract_days(self, n):
        index = Weeker.valid_days.index(self.__day)
        new_index = (index - n) % 7
        self.__day = Weeker.valid_days[new_index]


# Тестування
weeker = Weeker("Mon")
print(weeker)  # Mon
weeker.add_days(3)
print(weeker)  # Thu
weeker.subtract_days(5)
print(weeker)  # Sun
try:
    invalid_weeker = Weeker("Funday")
except WeekDayError as e:
    print(e)  # Sorry, I can't serve your request.

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())


# Тестування
point1 = Point(1, 1)
point2 = Point(2, 2)
print(point1.distance_from_xy(0, 0))  # 1.4142135623730951
print(point1.distance_from_point(point2))  # 1.4142135623730951

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())


class Triangle:
    def __init__(self, p1, p2, p3):
        self.__points = [p1, p2, p3]

    def perimeter(self):
        side1 = self.__points[0].distance_from_point(self.__points[1])
        side2 = self.__points[1].distance_from_point(self.__points[2])
        side3 = self.__points[2].distance_from_point(self.__points[0])
        return side1 + side2 + side3


# Тестування
point1 = Point(0, 0)
point2 = Point(1, 0)
point3 = Point(0, 1)
triangle = Triangle(point1, point2, point3)
print(triangle.perimeter())  # 3.414213562373095
