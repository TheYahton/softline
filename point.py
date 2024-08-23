from color import Color, Colors
from math import Vec2i, Vec2f


class Point2i:
    def __init__(self, pos: Vec2i, color: Color = Colors.WHITE) -> None:
        self.pos = pos
        self.color = color

class Point2f:
    def __init__(self, pos: Vec2f, color: Color = Colors.WHITE) -> None:
        self.pos = pos
        self.color = color

def transform(width: int, height: int, p: Point2f) -> Point2i:
    nx: int = int((p.pos.x + 1) / 2 * width)
    ny: int = height - int((p.pos.y + 1) / 2 * height)
    return Point2i(Vec2i(nx, ny), p.color)

