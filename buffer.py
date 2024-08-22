from os import get_terminal_size
from typing import Self, Sequence, Optional, List, cast

from color import Color, Colors
from point import Point


class Buffer:
    def __init__(self, width: int, height: int) -> None:
        self.body = cast(List[Optional[Color]], [None] * width * height)
        self.width = width
        self.height = height

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

    def dda(self, p1: Point, p2: Point):
        x1, y1, x2, y2 = *p1.pos, *p2.pos
        L = max(abs(x2 - x1), abs(y2 - y1)) + 1
        x, y = float(x1), float(y1)
        for i in range(L):
            percent = 1.0 - i / L
            color = p1.color.blend(p2.color, percent)
            self.pixel(int(x), int(y), color)
            x += (x2 - x1) / L
            y += (y2 - y1) / L

    def triangle(self, p1: Point, p2: Point, p3: Point):
        width, height = self.width, self.height
        triangle = Buffer(width, height)
        triangle.dda(p1, p2)
        triangle.dda(p2, p3)
        triangle.dda(p3, p1)
        for j in range(height):
            for i in range(width):
                start_color = triangle.body[i + j * width]
                if start_color is not None:
                    k = i + 1
                    while k < width and (end_color := triangle.body[k + j * width]) is None:
                        k += 1
                    if end_color is not None:
                        p1 = Point((i, j), start_color)
                        p2 = Point((k, j), end_color)
                        triangle.dda(p1, p2)

        self.blit(triangle)


class ScreenBuffer(Buffer):
    def __init__(self):
        width, height = get_terminal_size()
        super().__init__(width, height)

    def print(self):
        print("".join([f"\x1b[38;2;{int(color.r*255)};{int(color.g*255)};{int(color.b*255)}m█\x1b[0m" if color is not None else " " for color in self.body]))



