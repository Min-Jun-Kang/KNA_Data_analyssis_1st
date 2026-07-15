# int - 정수형

count = 3
age = 20
tall = 173

# 소수점 없이 딱 떨어지는 수
# 0과 음수도 포함 됨

temp = -30
zero = 0

# ============================

# float - 실수
# 소수점이 붙은 숫자
# 5.0처럼 딱 떨어지는 수이지만 소수점이 있다면 무조건 float

tired = 99.999999999
height = 17.2

# ===========================

# str - 문자열
# ""에 감싸져 있는 모든 값

hello = "안녕하세요~!"
emoji = "👍"
empty = ""  # 이것 또한 str
fake_num = "12345"
fake_num_2 = "5.0"
illit = "It's me"
# 따옴표가 "" 와 '' 둘 다 사용할 수 있는 이유는
# 문자열 안에 따옴표가 필요한 경우가 있기 때문
# 이럴 경우 사용하지 않는 따옴표로 쌍을 맞춰 가장 바깥에 감싸줘야 한다.

# ==========================

# bool - boolean형
# True or False 만
# 첫문자는 대문자, 따옴표 없이 작성

# ok = True
# no = False

# # 비교할 경우 bool로 출력
# print(10 < 5)  # False
# print(5 == 5)  # True


# ==========================

# type() - 자료형 확인
# type(확인하고자 하는 것) > 입력한 것의 자료형을 알려줌

# type(5)  # print로 확인하지 않으면 알 수가 없다.
# print(type(5))  # <class 'int'>
# print(type("센서A"))  # <class 'str'>
# print(type(True))  # <class 'bool'>
# print(type(3 > 4))  # <class 'bool'>

# print(3, type(3))  # 3 <class 'int'>

# num = 123
# fake_num = "123"
# str = "문자열"
# ok = True
# # 터미널에서 출력된 결과 중에서
# # type()을 사용해서 출력된 자료형을 쉽게 확인할 수 있는 방법
# print(num, type(num))  # 123 <class 'int'>
# print(fake_num, ">>>", type(fake_num))  # 123 >>> <class 'int'>
# print(str, ":", type(str))  # 123 : <class 'str'>
# print("str :", type(str))  # str : <class 'str'>

# # ======================================

# print(3 + 5)  # 8 숫자끼리 더하기 > 계산
# print("3" + "5")  # 35 > str끼리 더하기는 이어 붙이기
# print("안녕" + "하세요")

# # ======================================

# print(0.1 + 0.8)
# # 0.9가 출력되지만 가끔 컴퓨터 내부 과정에서 아주 작은 오차가 발생할 수도 있음

# # 작은 오차 해결법

# # print(round(0.15 + 0.845, 2))  # 소수 둘째 자리부터 반올림해서 0.9 출력

# # str 과 int/float은 덧셈 불가
# # print("123" + 456)  # TypeError 발생
# # print(10 / 2)  # 5.0(나눗셈은 결과가 딱 떨어져도 무조건 float)
