# tuple : 값을 묶어주는 역할
# () 안에 쉼표로 나누어서 여러가지 자료형의 값을 저장
# 그리고 마지막 값에는 꼭 ,를 붙여야 Python이 튜플로 인식을 함
# 짝지어진 값을 하나로 묶을 때 사용 가능한 자료형

# sensor = ("모터온도", 78)  # 괄호 있고, 끝에 쉼표 없음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>

# sensor = "모터온도", 78  # 괄호 없고, 끝에 쉼표 없음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>

# sensor = (
#     "모터온도",
#     78,
# )  # 괄호 있고, 끝에 쉼표 있음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>

# sensor = 78  # 괄호 없고, 끝에 쉼표 없음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'int'>

# sensor = (78,)  # 괄호 있고, 끝에 쉼표 있음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>

# sensor = ()  # 괄호 있고, 끝에 쉼표 없고, 값도 안담김
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>


# # 요소 개수
# # 요소 2개 이상 : 쉼표가 있다면 튜플
# # 요소 1개 : 쉼표 여부
# # 요소 0개 : () 튜플

# # 튜플에서 많이 헷갈려하는 부분
# # (1) : int
# # (1,) : tuple

# # (1,2,3,) -> 가장 마지막에 쉼표를 붙여서 튜플임을 명시
# # (1,2,3) -> 튜플 맞음

# 튜플의 인덱스

# sensor = ("모터온도", 78)
# print(sensor[0])  # 모터온도
# print(sensor[1])  # 78


# 튜플의 슬라이싱

# sensor = ("모터온도", 78, "a", "B", "c", 1, 2, 3)
# print(sensor[:3])  # 0~2까지
# print(sensor[3:])  # ('B', 'c', 1, 2, 3)
# print(sensor[2:4])  # ('a', 'B')
# print(sensor[1:5:2])  # (78, 'B')

# 튜플 언패킹
# 튜플에 담긴 값을 변수로 한 번에 분리

# 복습) 복수의 변수 한번에 선언

# a, b, c = "a", "b", "c"
# print(a)
# print(b)
# print(c)

unpacking = (
    1,  # 변수 one
    2,  # 변수 two
    3,  # 변수 three
)
# 언패킹
one, two, three = unpacking

print(one)
print(two)
print(three)

# 튜플의 언패킹은 변수의 개수와
# 튜플에 담긴 값의 개수가 동일해야 함

# 리스트 언패킹이 가능할까
one, two, three, four = [11, 22, 33, 44]
print(one)
print(two)
print(three)
print(four)
