# print("토끼")

x = 20

# print("대한민국은 사계절이 뚜렷한 나라입니다.")

if x  >= 20: # 분기 조건. x가 20보다 크거나 같은지 
    print("x는 20보다 크거나 같습니다.")
else:
    print("x는 20보다 작습니다.")



a = 4
a2 = a**0.5

print(a)
print(a2)


# 반지름을 넣고 원의 둘레와 면적을 구해봅시다.
"""
원의 반지름을 이용해서
원의 둘레와 면적을 구합니다.
"""

radius = 5
pi = 3.14
circumference = 2 * pi * radius # 둘레
area = pi * radius**2 # 넓이

print("원의 반지름은", radius, "입니다.")
print("원의 둘레는", circumference, "입니다.")
print("원의 면적은", area, "입니다.")


print('나의 이름은 :', '송예은')
print('나의 나이는 :', 33, '세')
print('나의 키는 :', 175, 'cm')
print('10 + 20 =', 10 + 20)
print('10 * 20 =', 10 * 20)


# camel case
thanksGivingDay = "2025.11.27"
# snake case
thanks_giving_day = "2025.11.27"
# pascal case
ThanksGivingDay = "2025.11.27"

str1 = "123"
print("str1 = ", str1)
str1 = "456"
print("str1[0:1] = ", str1[0:1])
print(str1)

str2 = '5' + str1[1:]
print("str2 = ", str2)


a = 10
b = '177'
c = a + int(b)
print("c = a + b =", c)

d = 'abc'
e = 222
f = d + str(e)
print("f = d + e :", f)

a, b = 100, 200
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)


if 13 % 2 == 0:
    print("13은 짝수입니다.")
else:
    13 % 2 == 1
    print("13은 홀수입니다.")