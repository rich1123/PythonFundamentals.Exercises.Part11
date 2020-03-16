# import shapes


class Rectangle:

    def __init__(self, length, width):
        self.length = length

        self.width = width

    def area(self):
        print(self.length * self.width)

    def perimeter(self):
        print(2*(self.length + self.width))


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


# import shapes
rect = Rectangle(2, 4)
rect.area()
# # 8

square = Square(8)
square.area()
# # 64
#
square.perimeter()
# # 32
