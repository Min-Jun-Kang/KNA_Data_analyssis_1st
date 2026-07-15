# 변수 선언 방법
# 변수 이름 = 값
# 오른쪽 값을 왼쪽 이름에 저장하라는 코드

# temp = 36  # 숫자로 저장하고 싶다면 따옴표 금지
# name = "센서A"  # 글자는 무조건 따옴표로 감싸기

# print(temp)  # 36 출력
# print("temp")  # temp 출력

# = 은 '같다'가 아니라 '저장'하는 것
# 비교는 ==을 사용한다.

# print("===== 변수 사용 활용 =====")

# x = 5
# x = x + 5  # 변수를 "재할당"할 때 변수 기존 자신의 값을 활용할 수 있다.
# # 변수에 할당할 때 오른쪽을 먼저 계산한 뒤 x에 값을 재할당

# y = y + 5  # 사용 불가 오류 발생 > y가 선언되지 않았기 때문

# print(x)  # 10 출력


# =====================
# print("===== 재할당 =====")

# print("재할당하기 전 temp :", temp)
# temp = 15  # 위에서 할당했던 36이라는 값을 15로 재할당(값 수정)
# Temp = 150  # temp와 다른 변수로 작동
# print("temp :", temp)
# print("Temp :", Temp)


# # 재할당은 지금까지 실행된 코드 중 가장 마지막으로 저장됨 값이 불러옴
# print(score) # NameError 발생
# score = 10
# print(score) # 10
# score = 20
# score = 30
# print(score) # 30

# # =================================
# print("====== 값 복사 ======")
# a = 10
# b = a  # b 변수에 10이 저장 (저장할 때의 그 순간의 a 값을 b에 복사)
# a = 100  # a 변수에 할당된 값을 재할당해도
# print(b)  # b 변수의 값은 10으로 유지된다.


# # =================================
# print("===== 여러 변수 한 번에 선언 및 할당 =====")

# # 형식 : 변수1, 변수2, .... = 값1, 값2, ..... > 변수 개수와 값의 개수가 동일해야함
# width, height = 10, 20  # width에는 10, height에는 20이 할당
# print("width:", width)
# print("height:", height)

# # x, y, z = 10, 20  # 변수 3개, 값 2개 > ValueError 발생

# # ==================================
# print("===== 주석으로 변수 설명 =====")

# temp = 25  # 온도(섭씨)
# count = 3  # 센서 개수
# # temp = 10000000000 # 주석처리된 코드는 동작하지 않음
# print(temp)  # 25 출력

# temperature = 25
# # print(temp)
# # name = "센서A"
# # print(name)

# temp = 30
# print(temp)
# print(temperature)

# my_number = 77
# print(my_number)
# mood = "Happy"
# print(mood)

# my_age = 30
# label = "내 나이"
# print(label)
# print(my_age)

# x = 10
# print(x)  # 10 출력 예상
# x = x + 5
# print(x)  # 10+5 = 15 출력 예상
# x = x * 2
# print(x)  # 15*2 = 30 출력 예상

# a = 100
# b = a  # b에 100저장
# a = 999
# print(a)
# print(b)
# # b에 저장된 값은 b = a 이후에 바뀌지 않았기 때문에 100이 나올 것이다.

# # print(temp)
# # NameError: name 'temp' is not defined > NameError 발생
# temp = 25
# print(temp)
# # 오류 해결 > 25 출력
# score = 90
# # print(Score)
# # NameError: name 'Score' is not defined. Did you mean: 'score'? > NameError 발생
# print(score)

# temp = 25  # 온도(섭씨)
# count = 3  # 센서 개수
# # temp = 100 # 주석은 실행되지 않음
# print(temp)  # 25출력

# x = 5
# x = 10
# x = x + 1
# print(x)
# # 코드는 위에서 아래로 진행되므로 마지막 10+1 = 11이 출력될 것이다.

# my_name = "강민준"
# my_age = 30
# my_city = "서울"
# print("자기소개")
# print("이름:", my_name)
# print("나이:", my_age)
# print("고향:", my_city)

# a = 25
# b = 3
# # 변수 이름은 다른 사람도 한 눈에보고 이해할 수 있어야한다.
# device_temp = 25  # 장비의 온도(섭씨)
# sensor_count = 3  # 센서의 개수
# print(device_temp)
# print(sensor_count)

# x, y, z = 1, 2, 3
# width, height = 4, 3
# print(width)  # 4 출력
# print(height)  # 3 출력
# a, b, c = 4, 5
# # ValueError: not enough values to unpack (expected 3, got 2)
# # 변수의 개수와 값의 개수가 동일하지 않아 오류가 나는 모습을 확인할 수 있다.
