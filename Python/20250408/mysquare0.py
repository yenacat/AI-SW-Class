"""
# mysquare0.py: 정사각형의 속성을 계산하는 모듈
get_area(length): 한 변의 길이가 length인 정사각형의 면적을 반환
get_perimeter(length): 한 변의 길이가 length인 정사각형의 둘레를 반환
set_pos(x, y): 정사각형의 위치를 설정하는 함수

"""

xpos, ypos = 0, 0


def get_area(length):  # 정사각형의 면적을 계산하는 함수
    """
    모듈: mysquare0.py
    함수: get_area(length)
    한 변의 길이가 length인 정사각형의 면적을 계산
    """
    return length**2


def get_perimeter(length):  # 정사각형의 둘레를 계산하는 함수
    """
    모듈: mysquare0.py
    함수: get_perimeter(length)
    한 변의 길이가 length인 정사각형의 둘레를 계산
    """
    return 4 * length


def set_pos(x, y):  # 정사각형의 위치를 설정하는 함수
    """
    모듈: mysquare0.py
    함수: set_pos(x, y)
    정사각형의 위치를 설정
    """
    global xpos, ypos
    xpos, ypos = x, y
