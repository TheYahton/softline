from dataclasses import dataclass


def clamp(vmin: int, vmax: int, value: int) -> int:
    return max(min(value, vmax), vmin)


@dataclass
class Color:
    r: float
    g: float
    b: float
    a: float = 1.0

    # TODO: type hint for mypy
    def blend(self, other, ratio: float):
        r = self.r * ratio + other.r * (1 - ratio)
        g = self.g * ratio + other.g * (1 - ratio)
        b = self.b * ratio + other.b * (1 - ratio)
        a = self.a * ratio + other.a * (1 - ratio)
        return Color(r, g, b, a)
    
    def rgb(self) -> tuple[int, int, int]:
        r = clamp(0, 255, int(self.a * self.r * 255))
        g = clamp(0, 255, int(self.a * self.g * 255))
        b = clamp(0, 255, int(self.a * self.b * 255))
        return r, g, b


class Colors:
    RED   = Color(1, 0, 0)
    GREEN = Color(0, 1, 0)
    BLUE  = Color(0, 0, 1)
    WHITE = Color(1, 1, 1)
    BLACK = Color(0, 0, 0)

    YELLOW = Color(1, 1, 0)
    PURPLE = Color(1, 0, 1)
    CYAN   = Color(0, 1, 1)

    TRANSPARENT = Color(0, 0, 0, 0)
