class Point:

    # dunder method - double underscore
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.__class__.__name__}  (x = {self.x}, y = {self.y}, z = {self.z})\n"


point = Point(2, 4, 7)
print(point.x)
print(point.y)
print(point.z)
print(point)

