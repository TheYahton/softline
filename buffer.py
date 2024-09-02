from sys import stdout
from os import get_terminal_size
from typing import Self, Optional, List, cast

from color import Color, Colors
from point import Point2i


class Buffer:
    def __init__(self, width: int, height: int) -> None:
        self.body = cast(List[Optional[Color]], [None] * width * height)
        self.width = width
        self.height = height

    def clear(self):
        self.body = cast(List[Optional[Color]], [None] * self.width * self.height)

    def fill(self, color: Color):
        self.body = cast(List[Optional[Color]], [color] * self.width * self.height)

    def blit(self, other: Self):
        for j in range(other.height):
            for i in range(other.width):
                color = other.body[i + j * other.width]
                if color is not None:
                    self.pixel(i, j, color)

    def pixel(self, x: int, y: int, color: Color):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return
        self.body[x + y * self.width] = color

    def dda(self, p1: Point2i, p2: Point2i):
        x1, y1, x2, y2 = p1.pos.x, p1.pos.y, p2.pos.x, p2.pos.y
        L = max(abs(x2 - x1), abs(y2 - y1)) + 1
        x, y = float(x1), float(y1)
        for i in range(L):
            percent = 1.0 - i / L
            color = p1.color.blend(p2.color, percent)
            self.pixel(int(x), int(y), color)
            x += (x2 - x1) / L
            y += (y2 - y1) / L


class ScreenBuffer(Buffer):
    def __init__(self):
        width, height = get_terminal_size()
        super().__init__(width, height)

    def print(self):
        stdout.write("\033[1;1H")  # move cursor to (1,1)
        stdout.write("".join([f"\x1b[38;2;{int(color.r*255)};{int(color.g*255)};{int(color.b*255)}m█\x1b[0m" if color is not None else " " for color in self.body]))



