class GeometricFigure:

    corner_count = 0


class Rectangle(GeometricFigure):
    corner_count = 4


class Triangle(GeometricFigure):
    corner_count = 3


class Circle(GeometricFigure):
    pass


print(Rectangle.corner_count)
sample_rectangle = Rectangle()
print(sample_rectangle.corner_count)

sample_circle = Circle()
print(sample_circle.corner_count)
print(Circle.corner_count)
