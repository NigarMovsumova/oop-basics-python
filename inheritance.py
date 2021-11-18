class Point:
    is_parent = True

    def __init__(self, x=0):
        self.x = x

    def who_am_i(self):
        print('I am a parent point')

    def __str__(self):
        return f'Point: x = {self.x}'


class TwoDimensionalPoint(Point):

    def __init__(self, x=0, y=0):
        super(TwoDimensionalPoint, self).__init__(x)
        self.y = y

    # def who_am_i(self):
    #     print('I am a 2d point')

    def __str__(self):
        return f'2DPoint: x={self.x}, y={self.y}'


class ThreeDimensionalPoint(TwoDimensionalPoint):

    def __init__(self, x=0, y=0, z=0):
        # super(ThreeDimensionalPoint, self).__init__(x, y)
        # super(TwoDimensionalPoint, self).__init__(x)
        self.x = x
        self.y = y
        self.z = z
        # super()

    # def who_am_i(self):
    #     print('I am a 3d point')

    def __str__(self):
        return f'3DPoint: x={self.x}, y={self.y}, z={self.z}'


parent = Point(3)
point_2d = TwoDimensionalPoint()
point_3d = ThreeDimensionalPoint()

print(parent)
print(point_2d)
print(point_3d)

parent.who_am_i()
point_2d.who_am_i()
point_3d.who_am_i()

