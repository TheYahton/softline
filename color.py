from typing import Self


class Color:
    def __init__(self, r: float, g: float, b: float):
        self.r = r
        self.g = g
        self.b = b

    def blend(self, other: Self, ratio: float):
        r = self.r * ratio + other.r * (1 - ratio)
        g = self.g * ratio + other.g * (1 - ratio)
        b = self.b * ratio + other.b * (1 - ratio)
        return Color(r, g, b)

    def clone(self):
        return Color(self.r, self.g, self.b)


class Colors:
    RED   = Color(1, 0, 0)
    GREEN = Color(0, 1, 0)
    BLUE  = Color(0, 0, 1)
    WHITE = Color(1, 1, 1)
    BLACK = Color(0, 0, 0)
