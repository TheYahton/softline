from copy import copy
from math import sin, cos
from dataclasses import dataclass


# TODO: self type hint for mypy (do not use deprecated typing module)
@dataclass
class Vec2i:
    x: int
    y: int


@dataclass
class Vec2f:
    x: float
    y: float

    def scale(self, scale: float):
        self.x *= scale
        self.y *= scale

    def rotate(self, theta: float):
        x = self.x * cos(theta) - self.y * sin(theta)
        y = self.x * sin(theta) + self.y * cos(theta)
        self.x, self.y = x, y

    def scaled(self, scale: float):
        copy = copy(self)
        copy.scale(scale)
        return copy

    def rotated(self, theta: float):
        copy = copy(self)
        copy.rotate(theta)
        return copy


@dataclass
class Vec3f:
    x: float
    y: float
    z: float

