from point import Point
from buffer import Buffer


def dda(buffer: Buffer, p1: Point, p2: Point):
    x1, y1, x2, y2 = *p1.pos, *p2.pos
    L = max(abs(x2 - x1), abs(y2 - y1)) + 1
    x, y = float(x1), float(y1)
    for i in range(L):
        percent = 1.0 - i / L
        color = p1.color.blend(p2.color, percent)
        buffer.pixel(int(x), int(y), color)
        x += (x2 - x1) / L
        y += (y2 - y1) / L

def draw_triangle(buffer: Buffer, p1: Point, p2: Point, p3: Point):
    width, height = buffer.width, buffer.height
    triangle = Buffer(width, height)
    dda(triangle, p1, p2)
    dda(triangle, p2, p3)
    dda(triangle, p3, p1)
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
                    dda(triangle, p1, p2)

    buffer.blit(triangle)

