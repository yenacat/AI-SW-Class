import math

PI = math.pi
xpos, ypos = 0, 0


def get_area(radius):
    return PI * radius**2


def get_perimeter(radius):
    return 2 * PI * radius


def set_pos(x, y):
    global xpos, ypos
    xpos, ypos = x, y
