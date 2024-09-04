from typing import Self


class Color:
    def __init__(self, r: float, g: float, b: float, a: float):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def blend(self, other: Self, ratio: float):
        r = self.r * ratio + other.r * (1 - ratio)
        g = self.g * ratio + other.g * (1 - ratio)
        b = self.b * ratio + other.b * (1 - ratio)
        a = self.a * ratio + other.a * (1 - ratio)
        return Color(r, g, b, a)
    
    def rgb(self) -> tuple[int, int, int]:
        r = int(self.a * self.r * 255)
        g = int(self.a * self.g * 255)
        b = int(self.a * self.b * 255)
        return r, g, b

    def clone(self):
        return Color(self.r, self.g, self.b, self.a)


class Colors:
    RED   = Color(1, 0, 0, 1)
    GREEN = Color(0, 1, 0, 1)
    BLUE  = Color(0, 0, 1, 1)
    WHITE = Color(1, 1, 1, 1)
    BLACK = Color(0, 0, 0, 1)

    YELLOW = Color(1, 1, 0, 1)
    PURPLE = Color(1, 0, 1, 1)
    CYAN   = Color(0, 1, 1, 1)

    TRANSPARENT = Color(0, 0, 0, 0)
