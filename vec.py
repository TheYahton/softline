from math import sin, cos


# TODO: self type hint for mypy (do not use deprecated typing module)
class Vec2i:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def as_tuple(self) -> tuple[int, int]:
        return (self.x, self.y)


class Vec2f:
    def __init__(self, x: float, y: float) -> None:
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


class Vec3f:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

