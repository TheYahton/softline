from color import Color, Colors
from point import Point
from buffer import ScreenBuffer
from render import draw_triangle


if __name__ == "__main__":
    buffer = ScreenBuffer()
    width, height = buffer.width, buffer.height
    p1 = Point((width // 2, 4), Colors.RED)
    p2 = Point((width // 2 - width // 3, 20), Colors.BLUE)
    p3 = Point((width // 2 + width // 3, 20), Colors.GREEN)
    draw_triangle(buffer, p1, p2, p3)
    buffer.print()

