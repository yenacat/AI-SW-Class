# mod1.py


def sum(a, b):
    return a + b


def safe_sum(a, b):
    if type(a) is not type(b):
        print("더할 수 없습니다.")
        return
    else:
        result = sum(a, b)
        return result
