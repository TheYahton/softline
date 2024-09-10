from vec import Vec2i
from color import Colors
from point import Point2f, Point2i
from buffer import Buffer


class Polygon:
    def __init__(self, *points, wireframe: bool = False):
        self.points = points
        self.wireframe = wireframe

    def rotate(self, theta: float):
        for p in self.points:
            p.pos.rotate(theta)

    def scale(self, scale: float):
        for p in self.points:
            p.pos.scale(scale)

    def draw(self, outer: Buffer):
        width, height = outer.width, outer.height
        buffer = Buffer(width, height)

        for i in range(len(self.points)):
            buffer.dda_raw(self.points[i-1], self.points[i])

        if not self.wireframe:
            for j in range(height):
                for i in range(width):
                    start_color = buffer.body[i + j * width]
                    if start_color != Colors.TRANSPARENT:
                        k = i + 1
                        while k < width and (end_color := buffer.body[k + j * width]) is Colors.TRANSPARENT:
                            k += 1
                        if end_color != Colors.TRANSPARENT:
                            p1 = Point2i(Vec2i(i, j), start_color)
                            p2 = Point2i(Vec2i(k, j), end_color)
                            buffer.dda(p1, p2)

        outer.blit(buffer)

