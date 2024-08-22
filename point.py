from color import Color, Colors


class Point:
    def __init__(self, position: tuple[int, int], color: Color = Colors.WHITE) -> None:
        self.pos = position
        self.color = color

