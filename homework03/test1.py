class Rectangle:
    def __init__(self, a, b):
        if b >= a:
            self.width = a
            self.height = b
        else:
            self.width = b
            self.height = a

    def get_area(self):
        return self.width * self.height

    def get_parameter(self):
        return 2 * self.width + 2 * self.height

    def __str__(self):
        return 'Параметр = ' + str(self.get_parameter()) + ', а площадь = ' + str(self.get_area())

    def get_sides(self):
        return self.width, self.height


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


square = Square(23)
# rectangle = Rectangle(12, 40)
print(square)
