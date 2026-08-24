# tuple : 값을 묶어주는 역할
# () 안에 쉼표로 나누어서 여러가지 자료형의 값을 저장
# 그리고 마지막 값에는 꼭 ,를 붙여야 Python이 튜플로 인식을 함
# 짝지어진 값을 하나로 묶을 때 사용 가능한 자료형

# # sensor = ("모터온도", 78)  # 괄호 있고, 끝에 쉼표 없음
# # print("sensor: ", sensor)
# # print("type(sensor): ", type(sensor))  # <class 'tuple'>

# # sensor = "모터온도", 78  # 괄호 없고, 끝에 쉼표 없음
# # print("sensor: ", sensor)
# # print("type(sensor): ", type(sensor))  # <class 'tuple'>

# # sensor = (
# #     "모터온도",
# #     78,
# # )  # 괄호 있고, 끝에 쉼표 있음
# # print("sensor: ", sensor)
# # print("type(sensor): ", type(sensor))  # <class 'tuple'>

# # sensor = 78  # 괄호 없고, 끝에 쉼표 없음
# # print("sensor: ", sensor)
# # print("type(sensor): ", type(sensor))  # <class 'int'>

# # sensor = (78,)  # 괄호 있고, 끝에 쉼표 있음
# # print("sensor: ", sensor)
# # print("type(sensor): ", type(sensor))  # <class 'tuple'>

# # sensor = ()  # 괄호 있고, 끝에 쉼표 없고, 값도 안담김
# # print("sensor: ", sensor)
# # print("type(sensor): ", type(sensor))  # <class 'tuple'>


# # # 요소 개수
# # # 요소 2개 이상 : 쉼표가 있다면 튜플
# # # 요소 1개 : 쉼표 여부
# # # 요소 0개 : () 튜플

# # # 튜플에서 많이 헷갈려하는 부분
# # # (1) : int
# # # (1,) : tuple

# # # (1,2,3,) -> 가장 마지막에 쉼표를 붙여서 튜플임을 명시
# # # (1,2,3) -> 튜플 맞음

# # 튜플의 인덱스

# # sensor = ("모터온도", 78)
# # print(sensor[0])  # 모터온도
# # print(sensor[1])  # 78


# # 튜플의 슬라이싱

# # sensor = ("모터온도", 78, "a", "B", "c", 1, 2, 3)
# # print(sensor[:3])  # 0~2까지
# # print(sensor[3:])  # ('B', 'c', 1, 2, 3)
# # print(sensor[2:4])  # ('a', 'B')
# # print(sensor[1:5:2])  # (78, 'B')

# # 튜플 언패킹
# # 튜플에 담긴 값을 변수로 한 번에 분리

# # 복습) 복수의 변수 한번에 선언

# # a, b, c = "a", "b", "c"
# # print(a)
# # print(b)
# # print(c)

# unpacking = (
#     1,  # 변수 one
#     2,  # 변수 two
#     3,  # 변수 three
# )
# # 언패킹
# one, two, three = unpacking

# print(one)
# print(two)
# print(three)

# # 튜플의 언패킹은 변수의 개수와
# # 튜플에 담긴 값의 개수가 동일해야 함

# # # 리스트 언패킹이 가능할까
# # one, two, three, four = [11, 22, 33, 44]
# # print(one)
# # print(two)
# # print(three)
# # print(four)

# tup = (
#     "normal",
#     "normal",
#     "warning",
#     "normal",
#     "warning",
# )

# # 튜플의 길이
# print(len(tup))  # 5

# # 특정 값의 갯수 세기
# print(tup.count("warning"))  # 2
# # 찾고자 하는 값이 없다면 0 출력
# print(tup.index("Warning"))

# # 특정 값이 처음 나온 인덱스 찾기
# print(tup.index("warning"))  # 2
# # 찾고자 하는 값이 없다면 Error
# print(tup.index("Warning"))  # ValueError: tuple.index(x): x not in tuple

# 튜플 리스트
# 리스트 안에 복수의 튜플을 담는 것을 표현
# for문으로 리스트를 사용해서
# 리스트 내분의 튜플에 접근하고
# 튜플에 담긴 값을 사용할 수 있음

# 언패킹을 사용해서 접근한 튜플 내부의 값을
# 변수에 바로 할당해서 접근

# # 튜플 리스트를 반복문으로 처리
# hour_13 = [("모터온도", 77), ("모터진동", 0.2), ("모터압력", 91)]

# now = 0

# for name, value in hour_13:
#     now += 1
#     # print(now, "번째 반복")
#     print(f"{now}번째 반복")
#     print("name:", name, "value:", value)


# temps_13 = [
#     ("qox_001", 81),
#     ("qox_002", 88),
#     ("qox_003", 95),
#     ("qox_004", 89),
# ]

# warning = 90

# for name, temp in temps_13:
#     if temp >= warning:
#         print(f"경고! {name} 설비 온도 이상")


# # 리스트 안의 튜플 개수가 늘어나면
# # for문에서 변수를 여러 개 작성하면 됨

# tup_list = [
#     ("일", "one", 1, "1"),
#     ("이", "two", 2, "2"),
# ]

# # for문에서도 언패킹 할 때는 무조건 튜플의 값 개수와
# # for문의 변수 개수 통일
# # 통일하지 않을 경우 Erro 발생
# for kor_str, eng_str, num, num_str in tup_list:
#     print(f"kor_str: {kor_str}\neng_str: {eng_str}\nnum: {num_str}\nnum_str: {num_str}")

# # 튜플 리스트 정렬
# # sorted()를 사용하여
# # 튜플의 특정 값 기준으로 리스트를 정렬

# temps_13 = [
#     ("qox_001", 81),
#     ("qox_002", 88),
#     ("qox_003", 95),
#     ("qox_004", 89),
# ]

# hot = sorted(temps_13, reverse=True)
# print(hot)
# hot = sorted(temps_13, reverse=False)
# print(hot)

# # sorted()는 원본 배열을 수정하지 않고
# # 새 리스트를 반환해줌
# print(temps_13)
