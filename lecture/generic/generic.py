from math import sin, cos, pi
from math import atan2


class Boy:
    def __init__(self, bool, name):
        self.bool = bool
        self.name = name

    def __bool__(self):
        if self.bool == True:
            return True
        else:
            return False

    def __len__(self):
        return len(self.name)


class Adder(object):
    def __init__(self, n):
        self.n = n

    def __call__(self, k):
        return self.n + k


class Number:
    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)


class Complex(Number):
    type_tag = 'Complex'

    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)

    def mul(self, other):
        magnitude = self.magnitude + other.magnitude
        return ComplexMA(magnitude, self.angle + other.angle)


class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)

    def __repr__(self):
        return "ComplexRI({0:g}, {1:g})".format(self.real, self.imag)


class ComplexMA(Complex):

    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
        return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude, self.angle/pi)


# type dispatch
def is_real(c):
    if isinstance(c, ComplexRI):
        return c.imag == 0
    elif isinstance(c, ComplexMA):
        return c.angle % pi == 0
