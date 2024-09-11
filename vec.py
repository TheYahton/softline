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

    def clone(self):
        return Vec2f(self.x, self.y)

    def scale(self, scale: float):
        self.x *= scale
        self.y *= scale

    def rotate(self, theta: float):
        x = self.x * cos(theta) - self.y * sin(theta)
        y = self.x * sin(theta) + self.y * cos(theta)
        self.x, self.y = x, y

    def scaled(self, scale: float):
        copy = self.clone()
        copy.scale(scale)
        return copy

    def rotated(self, theta: float):
        copy = self.clone()
        copy.rotate(theta)
        return copy


class Vec3f:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

