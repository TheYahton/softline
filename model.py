from vec import Vec2i
from point import Point2f, Point2i, transform
from buffer import Buffer


class Triangle:
    def __init__(self, p1: Point2f, p2: Point2f, p3: Point2f):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def get_transformed(self, width, height) -> tuple[Point2i, Point2i, Point2i]:
        return (transform(width, height, self.p1),
                transform(width, height, self.p2),
                transform(width, height, self.p3))

    def draw(self, outer: Buffer):
        width, height = outer.width, outer.height
        p1, p2, p3 = self.get_transformed(width, height)
        buffer = Buffer(width, height)
        buffer.dda(p1, p2)
        buffer.dda(p2, p3)
        buffer.dda(p3, p1)
        for j in range(height):
            for i in range(width):
                start_color = buffer.body[i + j * width]
                if start_color is not None:
                    k = i + 1
                    while k < width and (end_color := buffer.body[k + j * width]) is None:
                        k += 1
                    if end_color is not None:
                        p1 = Point2i(Vec2i(i, j), start_color)
                        p2 = Point2i(Vec2i(k, j), end_color)
                        buffer.dda(p1, p2)

        outer.blit(buffer)

