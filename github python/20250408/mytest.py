# mycircle0.py
# myrect0.py

import mycircle0
import myrect0
import mysquare0

radius = 5
circle_area = mycircle0.get_area(radius)
circle_perimeter = mycircle0.get_perimeter(radius)
mycircle0.set_pos(100, 100)

print(
    f"반지름이 {radius}인 원의 면적은 {circle_area}, 둘레는 {circle_perimeter}입니다."
)


width = 3
height = 4
rect_area = myrect0.get_area(width, height)
rect_perimeter = myrect0.get_perimeter(width, height)
myrect0.set_pos(200, 200)

print(
    f"가로가 {width}, 세로가 {height}인 직사각형의 면적은 {rect_area}, 둘레는 {rect_perimeter}입니다."
)


length = 50
square_area = mysquare0.get_area(length)
square_perimeter = mysquare0.get_perimeter(length)
mysquare0.set_pos(300, 300)

print(
    f"한 변의 길이가 {length}인 정사각형의 면적은 {square_area}, 둘레는 {square_perimeter}입니다."
)


print(mysquare0.__doc__)
print(mysquare0.get_area.__doc__)
