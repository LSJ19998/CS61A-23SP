import math
pi = math.pi


class Butterfly():
    def __init__(self, wings=2):
        self.wings = wings


class Monarch(Butterfly):
    def __init__(self):
        super().__init__()
        self.colors = ['orange', 'black', 'white']


class MimicButterfly(Butterfly):
    def __init__(self, mimic_animal):
        super().__init__()
        self.mimic_animal = mimic_animal


class Shape:
    """All geometric shapes will inherit from this Shape class."""

    def __init__(self, name):
        self.name = name

    def area(self):
        """Returns the area of a shape"""
        print("Override this method in ", type(self))

    def perimeter(self):
        """Returns the perimeter of a shape"""
        print("Override this function in ", type(self))


class Circle(Shape):
    """A circle is characterized by its radii"""

    def __init__(self, name, radius):
        "*** YOUR CODE HERE ***"
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        """Returns the perimeter of a circle (2πr)"""
        "*** YOUR CODE HERE ***"
        super().perimeter()
        return 2 * pi * self.radius

    def area(self):
        """Returns the area of a circle (πr^2)"""
        "*** YOUR CODE HERE ***"
        super().area()
        return pi * pi * self.radius * self.radius


class RegPolygon(Shape):
    """A regular polygon is defined as a shape whose angles and side lengths are all the same.
    This means the perimeter is easy to calculate. The area can also be done, but it's more inconvenient."""

    def __init__(self, name, num_sides, side_length):
        "*** YOUR CODE HERE ***"
        super().__init__(name)
        self.num_sides = num_sides
        self.side_length = side_length

    def perimeter(self):
        """Returns the perimeter of a regular polygon (the number of sides multiplied by side length)"""
        "*** YOUR CODE HERE ***"
        super().perimeter()
        return self.num_sides * self.side_length


class Square(RegPolygon):
    def __init__(self, name, side_length):
        "*** YOUR CODE HERE ***"

    def area(self):
        """Returns the area of a square (squared side length)"""
        "*** YOUR CODE HERE ***"
        return self.side_length * self.side_length


class Triangle(RegPolygon):
    """An equilateral triangle"""

    def __init__(self, name, side_length):
        "*** YOUR CODE HERE ***"
        super().__init__(name)
        self.side_length = side_length

    def area(self):
        """Returns the area of an equilateral triangle is (squared side length multiplied by the provided constant"""
        constant = math.sqrt(3)/4
        "*** YOUR CODE HERE ***"


class Cat:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.live = 9

    def lose_life(self):
        self.live -= 1

    def __repr__(self):
        return f"{self.type}, {self.live} lives"

    def __str__(self):
        return f'{self.type}'
