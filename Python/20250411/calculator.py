def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "오류: 0으로 나눌 수 없습니다."
    return x / y


# 계산기 메인 로직
print("사칙연산 계산기입니다.")
print("사용 가능한 연산자: +, -, *, /")

while True:  # 사용자가 원할 때까지 반복
    try:
        # 첫 번째 숫자 입력받기
        num1_str = input("첫 번째 숫자를 입력하세요: ")
        num1 = float(num1_str)  # 입력받은 문자열을 실수로 변환

        # 연산자 입력받기
        operator = input("연산자를 입력하세요 (+, -, *, /): ").strip()  # 공백 제거

        # 유효한 연산자인지 확인
        if operator not in ["+", "-", "*", "/"]:
            print("잘못된 연산자입니다. +, -, *, / 중 하나를 입력해주세요.")
            continue  # 루프의 처음으로 돌아감

        # 두 번째 숫자 입력받기
        num2_str = input("두 번째 숫자를 입력하세요: ")
        num2 = float(num2_str)  # 입력받은 문자열을 실수로 변환

        # 연산자에 따라 적절한 함수 호출 및 결과 출력
        result = None
        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)  # 0 나누기 오류는 divide 함수 내에서 처리

        # 결과 출력 (오류 메시지 또는 계산 결과)
        if isinstance(result, str):  # 결과가 문자열이면 (오류 메시지)
            print(result)
        else:
            print(f"결과: {num1} {operator} {num2} = {result}")

    except ValueError:
        # 숫자가 아닌 값을 입력했을 때 오류 처리
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
        continue  # 루프의 처음으로 돌아감
    except Exception as e:
        # 기타 예상치 못한 오류 처리
        print(f"오류가 발생했습니다: {e}")
        continue

    # 추가 계산 여부 확인
    next_calculation = input("다른 계산을 하시겠습니까? (y/n): ")
    if next_calculation.lower() != "y":
        break  # 'y'가 아니면 루프 종료

print("계산기를 종료합니다.")
