from sys import stdout
from os import get_terminal_size

from color import Color, Colors
from point import Point2i, Point2f, transform


class Buffer:
    def __init__(self, width: int, height: int) -> None:
        self.body = [Colors.TRANSPARENT] * width * height
        self.width = width
        self.height = height

    def clear(self) -> None:
        self.fill(Colors.TRANSPARENT)

    def fill(self, color: Color) -> None:
        self.body = [color] * self.width * self.height

    def blit(self, other):  # TODO: self type hint for mypy
        for j in range(other.height):
            for i in range(other.width):
                index = i + j * other.width
                F = other.body[index]
                A = F.a
                B = self.body[index]
                r = B.r * (1 - A) + F.r * A
                b = B.b * (1 - A) + F.b * A
                g = B.g * (1 - A) + F.g * A
                self.body[index] = Color(r, g, b)

    def pixel(self, x: int, y: int, color: Color) -> None:
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return
        self.body[x + y * self.width] = color

    def dda(self, p1: Point2i, p2: Point2i) -> None:
        x1, y1, x2, y2 = p1.pos.x, p1.pos.y, p2.pos.x, p2.pos.y
        L = max(abs(x2 - x1), abs(y2 - y1)) + 1
        x, y = float(x1), float(y1)
        for i in range(L):
            percent = 1.0 - i / L
            color = p1.color.blend(p2.color, percent)
            self.pixel(int(x), int(y), color)
            x += (x2 - x1) / L
            y += (y2 - y1) / L

    def dda_raw(self, p1: Point2f, p2: Point2f) -> None:
        self.dda(transform(p1, self.width, self.height),
                 transform(p2, self.width, self.height))


class ScreenBuffer(Buffer):
    def __init__(self) -> None:
        width, height = get_terminal_size()
        super().__init__(width, height)

    def print(self) -> None:
        stdout.write("\033[1;1H")  # move cursor to (1,1)

        output = []
        prev_color = None
        for color in self.body:
            if color != prev_color:
                prev = color
                r, g, b = color.rgb()
                output.append(f"\x1b[38;2;{r};{g};{b}m█")
            else:
                output.append("█")

        stdout.write("".join(output))

