class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    rectangle = Rectangle(5, 4)
    print(rectangle.area())
    print(rectangle.perimeter())
