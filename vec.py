from math import sin, cos


class Vec2i:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Vec2f:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def rotated(self, theta: float):
        x, y = self.x, self.y
        return Vec2f(x * cos(theta) - y * sin(theta),
                     x * sin(theta) + y * cos(theta))

    def rotate(self, theta: float):
        rotated = self.rotated(theta)
        self.x = rotated.x
        self.y = rotated.y

    def scaled(self, scale: float):
        return Vec2f(self.x * scale,
                     self.y * scale)

    def scale(self, scale: float):
        self.x *= scale
        self.y *= scale

    def clone(self):
        return Vec2f(self.x, self.y)

