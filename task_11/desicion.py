class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius


if __name__ == '__main__':
    circle = Circle(5)
    print(f"Площадь: {circle.area()}")
    print(f"Длина окружности: {circle.circumference()}")
