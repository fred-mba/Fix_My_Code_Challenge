#!/usr/bin/python3
"""
An implementation of a perfect square
"""


class square():
    """Class square function"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize single and keyword arguments"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """String representation"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
