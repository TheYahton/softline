from sys import stdout
from os import get_terminal_size
from typing import Self, Optional, List, cast

from color import Color, Colors


class Buffer:
    def __init__(self, width: int, height: int) -> None:
        self.body = cast(List[Optional[Color]], [None] * width * height)
        self.width = width
        self.height = height

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


class ScreenBuffer(Buffer):
    def __init__(self):
        width, height = get_terminal_size()
        super().__init__(width, height)

    def print(self):
        stdout.write("".join([f"\x1b[38;2;{int(color.r*255)};{int(color.g*255)};{int(color.b*255)}m█\x1b[0m" if color is not None else " " for color in self.body]))



