# mod2.py
PI = 3.141592


class Math:
    def solv(self, r):
        return PI * (r**2)


def sum(a, b):
    return a + b


if __name__ == "__main__":  # 모듈을 직접 실행할 때만 실행됨
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI, 4.4))
