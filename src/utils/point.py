from math import pi, atan, sqrt

class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __add__(self, b):
        return Point(self.x + b.x, self.y + b.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __sub__(self, b):
        return self + (-b)

    def __mul__(self, c):
        return Point(self.x*c, self.y*c)

    def __truediv__(self, c):
        return Point(self.x/c, self.y/c)

    def __str__(self):
        return str((self.x, self.y))

    def ang(self):
        return pi/2 - (atan(self.y/self.x) if self.x else pi/2)

    def crd(self):
        return (self.x, self.y)

    def norm(self):
        return sqrt(self.x**2 + self.y**2)
