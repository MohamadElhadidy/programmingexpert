import math


class Polygon:
    def get_sides(self):
        raise NotImplementedError('')

    def get_area(self):
        raise NotImplementedError('')

    def get_perimeter(self):
        return sum(self.get_sides())


class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_sides(self):
        return self.side1, self.side2, self.side3

    def get_area(self):
        return get_triangle_area(self.side1, self.side2, self.side3)


class Rectangle(Polygon):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def get_sides(self):
        return self.side1, self.side2, self.side1, self.side2

    def get_area(self):
        return self.side1 * self.side2


class Square(Rectangle):
    def __init__(self, side1):
        super().__init__(side1, side1)


# Use this function in your solution.
def get_triangle_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(
        semi_perimeter *
        (semi_perimeter - side1) *
        (semi_perimeter - side2) *
        (semi_perimeter - side3)
    )


# Use this function in your solution.
def get_rectangle_area(width, height):
    return width * height
