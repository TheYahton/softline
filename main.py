from color import Color, Colors
from vec import Vec2f
from point import Point2f
from model import Triangle
from buffer import ScreenBuffer


if __name__ == "__main__":
    buffer = ScreenBuffer()
    width, height = buffer.width, buffer.height
    p1 = Point2f(Vec2f(0, 1.0), Colors.RED)
    p2 = Point2f(Vec2f(-1.0, -1.0), Colors.BLUE)
    p3 = Point2f(Vec2f(1.0, -1.0), Colors.GREEN)
    triangle = Triangle(p1, p2, p3)
    triangle.rotate(1.0)
    triangle.draw(buffer)
    buffer.print()

