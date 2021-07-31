import math


class Circle:
    def _init_(self, radius):
        self.radius = radius

    def getradius(self):
        return self.radius

    def calc_area(self):
        return math.pi * (self.radius ** 2)


class cylinder(Circle):
    def _init_(self, height, radius):
        super()._init_(radius)
        self.height = height

    def cal_area(self):
        return 2 * math.pi * self.radius * self.height


a = Circle(3)
print("Area of circle is : ", a.calc_area())
b = cylinder(4, 3)
print("Area of cylinder is : ", b.calc_area())