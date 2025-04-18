xpos, ypos = 0, 0


def get_area(width, height):
    area = width * height
    return area


def get_perimeter(width, height):
    perimeter = 2 * (width + height)
    return perimeter


def set_pos(x, y):
    global xpos, ypos
    xpos, ypos = x, y
