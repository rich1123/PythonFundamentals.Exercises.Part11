import shapes
# import typing


class Rectangle:

    def __init__(self, length: int, width: int):
        self.length = length

        self.width = width

    def area(self):
        print(self.length * self.width)

    def perimeter(self):
        print(2*(self.length + self.width))


class Square(Rectangle):
    def __init__(self, length: int):
        super().__init__(length, length)


import shapes
rect = Rectangle(2, 4)
rect.area()
# # 8

square = Square(8)
square.area()
# # 64
#
square.perimeter()
# # 32
