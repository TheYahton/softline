from time import sleep

from color import Color, Colors
from vec import Vec2f
from point import Point2f
from model import Triangle
from buffer import ScreenBuffer


if __name__ == "__main__":
    buffer = ScreenBuffer()
    width, height = buffer.width, buffer.height
    p1 = Point2f(Vec2f(-1.0, 1.0), Colors.RED)
    p2 = Point2f(Vec2f(1.0, 1.0), Colors.BLUE)
    p3 = Point2f(Vec2f(1.0, -1.0), Colors.GREEN)
    p4 = Point2f(Vec2f(-1.0, -1.0), Colors.BLUE)
    triangle1 = Triangle(p1.clone(), p2.clone(), p3.clone())
    triangle2 = Triangle(p1.clone(), p3.clone(), p4.clone())
    triangle1.scale(0.5)
    triangle2.scale(0.5)
    while True:
        buffer.clear()
        triangle1.rotate(0.1)
        triangle2.rotate(0.1)
        triangle1.draw(buffer)
        triangle2.draw(buffer)
        buffer.print()
        sleep(1/60)

