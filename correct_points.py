class Point:

    # dunder method - double underscore
    def __init__(self, x, y, z):
        print(self)
        self.x = x
        self.y = y
        self.z = z


point = Point(2, 4, 7)
print(point.x)
print(point.y)
print(point.z)

point2 = Point(3, 6, 9)
print(point2.x)
print(point2.y)
print(point2.z)
