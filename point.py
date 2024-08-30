from color import Color, Colors
from vec import Vec2i, Vec2f, Vec3f


class Point2i:
    def __init__(self, pos: Vec2i, color: Color = Colors.WHITE) -> None:
        self.pos = pos
        self.color = color


class Point2f:
    def __init__(self, pos: Vec2f, color: Color = Colors.WHITE) -> None:
        self.pos = pos
        self.color = color

    def clone(self):
        return Point2f(self.pos.clone(), self.color.clone())


class Point3f:
    def __init__(self, pos: Vec3f, color: Color = Colors.WHITE) -> None:
        self.pos = pos
        self.color = color

    def project(self) -> Point2f:
        np = 1
        tga = self.pos.y / self.pos.z
        tgb = self.pos.x / self.pos.z
        pos = Vec2f(np * tgb, np * tga)
        return Point2f(pos, self.color)


def transform(p: Point2f, width: int, height: int) -> Point2i:
    nx: int = int((p.pos.x + 1) / 2 * width)
    ny: int = height - int((p.pos.y + 1) / 2 * height)
    return Point2i(Vec2i(nx, ny), p.color)

