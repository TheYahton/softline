from time import sleep

from color import Color, Colors
from vec import Vec2f, Vec3f
from point import Point2f, Point3f, transform
from model import Triangle
from buffer import ScreenBuffer


# TODO: вращение для Point3f через матрицы/кватернионы/углы Эйлера
# TODO: исправить рендеринг Triangle на буфере: сделать размер буфера зависящим от размера треугольника
# TODO: исправить рисование линий: линия (x, y) и линия (y, x) неидентичны, хотя должны быть таковыми
# TODO: вращение и рендеринг куба
# TODO: новый стиль рендера: незаполненные полигоны
# TODO: полигоны вместо треугольников (возможность рендерить любые многоугольники)
# TODO: вращение и перемещение камеры
# TODO (optional): шейдеры как в OpenGL

if __name__ == "__main__":
    buffer = ScreenBuffer()
    width, height = buffer.width, buffer.height
    p1 = Point3f(Vec3f(-1.0, 1.0, 2.0), Colors.RED)
    p2 = Point3f(Vec3f(1.0, 1.0, 2.0), Colors.BLUE)
    p3 = Point3f(Vec3f(1.0, -1.0, 2.0), Colors.GREEN)
    p4 = Point3f(Vec3f(-1.0, -1.0, 2.0), Colors.BLUE)
    while True:
        buffer.clear()
        pp1 = p1.project()
        pp2 = p2.project()
        pp3 = p3.project()
        pp4 = p4.project()
        triangle1 = Triangle(pp1.clone(), pp2.clone(), pp3.clone())
        triangle2 = Triangle(pp1.clone(), pp3.clone(), pp4.clone())
        triangle1.draw(buffer)
        triangle2.draw(buffer)
        buffer.print()
        sleep(1/60)

