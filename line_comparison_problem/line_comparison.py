'''

@Author: Joshikaran.k

@Date: 2024-01-22 16:30:00

@Last Modified by: Joshikaran.k

@Last Modified time: 2024-01-22 16:30:00

@Title : Creating LineComparision Program

'''
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.point1 = Point(x1, y1)
        self.point2 = Point(x2, y2)

    def get_Length(self):
        return math.sqrt((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2)

    def __eq__(self, other):
        return self.get_Length() == other.get_Length()

    def __lt__(self, other):
        return self.get_Length() < other.get_Length()

    def __gt__(self, other):
        return self.get_Length() > other.get_Length()

    def __str__(self):
        return f"Line({self.point1.x},{self.point1.y},{self.point2.x},{self.point2.y})"



if __name__ == "__main__":
    line1 = Line(2, 5, 3, 4)
    line2 = Line(2, 5, 3, 4)
    line3 = Line(3, 4, 10, 8)
    line4 = Line(3, 1, 4, 4)
    line5 = Line(5, 2, 6, 10)

    lines = [line1, line2, line3, line4, line5]

    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            if lines[i] == lines[j]:
                print(f"{lines[i]} is equal to {lines[j]}")
            if lines[i] > lines[j]:
                print(f"{lines[i]} is greater than {lines[j]}")
            if lines[i] < lines[j]:
                print(f"{lines[i]} is less than {lines[j]}")