from os import get_terminal_size
from typing import Self


class Color:
    def __init__(self, r: float, g: float, b: float):
        self.r = r
        self.g = g
        self.b = b

    def __mul__(self, other: float):
        return Color(self.r * other,
                     self.g * other,
                     self.b * other)

    def __add__(self, other: Self):
        return Color(self.r + other.r,
                     self.g + other.g,
                     self.b + other.b)

class Colors:
    RED   = Color(1, 0, 0)
    GREEN = Color(0, 1, 0)
    BLUE  = Color(0, 0, 1)
    WHITE = Color(1, 1, 1)
    BLACK = Color(0, 0, 0)

class Point:
    def __init__(self, position: tuple[int, int], color: Color = Colors.WHITE) -> None:
        self.pos = position
        self.color = color

class Buffer:
    def __init__(self, width: int, height: int) -> None:
        self.body = [Colors.BLACK] * width * height
        self.width = width
        self.height = height

    def pixel(self, x: int, y: int, color: Color):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return
        self.body[x + y * self.width] = color

    def dda(self, p1: Point, p2: Point):
        x1, y1, x2, y2 = *p1.pos, *p2.pos
        L = max(abs(x2 - x1), abs(y2 - y1)) + 1
        x, y = float(x1), float(y1)
        for i in range(L):
            percent = i / L
            color = p2.color * percent + p1.color * (1 - percent)
            self.pixel(int(x), int(y), color)
            x += (x2 - x1) / L
            y += (y2 - y1) / L

    def triangle(self, p1: Point, p2: Point, p3: Point):
        self.dda(p1, p2)
        self.dda(p2, p3)
        self.dda(p3, p1)

class ScreenBuffer(Buffer):
    def __init__(self):
        width, height = get_terminal_size()
        super().__init__(width, height)

    def print(self):
        print("".join([f"\x1b[38;2;{int(color.r*255)};{int(color.g*255)};{int(color.b*255)}m█\x1b[0m" for color in self.body]))

if __name__ == "__main__":
    buffer = ScreenBuffer()
    width, height = buffer.width, buffer.height
    p1 = Point((width//2, 4), Colors.RED)
    p2 = Point((width//2-width//3, 20), Colors.BLUE)
    p3 = Point((width//2+width//3, 20), Colors.GREEN)
    buffer.triangle(p1, p2, p3)
    buffer.print()

