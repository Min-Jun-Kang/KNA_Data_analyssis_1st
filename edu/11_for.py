# 반복문은 동일한 작업을 특정 횟수만큼 반복해야할 때
# 코드를 길게 쓰지 않고 반복시킬 수 있음

# for 변수 in 범위:

# for 변수 in range(횟수):
#   반복시킬 코드 (들여쓰기 필수)
# 같은 코드를 복사 붙여넣기로 여러 번 작성하는 ㅐ신
# "N번 실행하라"는 의미

# for i in range(3):
#     print("안녕하세요!")  # range에 전달한 인자가 3만큼 3번 반복
#     # i를 쓰지 않아도 됨 -> 목적이 단순 반복

# # 0부터 10까지의 숫자 자체가 필요하거나 출력할 때
# for i in range(11):
#     print(i)  # 0부터 10까지 출력


# for i in range(11):
#     if i % 2 == 1:
#         print(i)
# # 0부터 10까지 짝수만 필요할 때
# for i in range(0, 11, 2):
#     print(i)
# # 0부터 10까지 홀수만 필요할 때
# for i in range(1, 11, 2):
#     print(i)

# # 역순으로 출력
# for i in range(10, 0, -1):
#     print(i)

# # 10부터 1까지 짝수만 역순으로 출력
# for i in range(10, 0, -2):
#     print(i)

# # 시작값이 0에서 -2 했을 때 끝 값이 포함되지 않아서 반복문 종료
# for i in range(0, 10, -2):
#     print(i)

# # 누적변수

# total = 0

# for i in range(1, 6):  # 1 2 3 4 5
#     total += i  # total 에 i (12345) 더함 - 기존 total 값의 i(12345) 재할당
# print("합계: ", total)  # 15

# # for문 안에 누적변수 선언 시

# for i in range(1, 6):
#     total2 = 0  # 반복을 돌 떄마다 새로이 변수에 값이 0으로 할당
#     total2 += i
# print("합게: ", total2)  # 가장 마지막 i 인 5가 출력되어 합계 : 5

# # 번외편

# if 3 == 3:
#     hi = "안녕"
# print(hi)  # 안녕

# # python에서는 if문 안의 변수도
# # 어디서든 호출 가능한 변수로 선언

# # 1~15 사이 4의 배수만 누적
# total3 = 0
# for i in range(1, 16):
#     if i % 4 == 0:
#         total3 += i
# print("1~15사이 4의 배수 누적: ", total3)  # 24


# # 초과하는 수의 갯수 구하기

# cont = 0
# for i in range(1, 13):
#     if i > 5:
#         cont += 1
# print("5보다 큰 값의 개수: ", cont)  # 7


# enumerate(낱낱이 세다)

# # temps = [33, 23, 45, 32, 28]
# # for idx, t in enumerate(temps):
# #     print(f"idx: {idx}, t: {t}")

# temps = [33, 23, 45, 32, 28]

# for idx, t in enumerate(temps):
#     print(f"현재 인덱스 : {idx}")
#     print(f"{idx} 인덱스의 값 : {t}")
#     print(f"{idx+1}번째 반복 끝")


# 안녕의 인덱스 출력
# 이를 위해서는 값을 비교하기 위해 모든 리스트와 값이 필요
# 그리고 그 값의 인덱스를 알아야 출력
# 인덱스와 값이 필요하다.

# 리스트의 모든요소에 접근을 해야 하는 경우가 잦음
# 그래서 Python이 반복문에서 이를 쉽게 할 수 있도록
# enumerate라는 내장 함수를 제공
# enumerate은 리스트의 모든 요소를 앞에서부터
# 순서대로 하나씩 찍어가면서 접근
# 값을 두 개 받으니 우리도 변수를 2개 준비하면
# 각 변수에 쏙쏙 값이 할당
# 돌려주는 순서는 인덱스, 값
# 그렇기 때문에 우리는 enumerate를 사용할 때
# for 뒤에 변수를 2개 전달


# list = ["안녕", "hi", "hi", "안녕", "hi", "안녕"]

# for index, value in enumerate(list):
#     print(f"value: {value}")


# for i in range(len(list)):
#     print(f"list: {list[i]}")

# # 중첩 반복문

# # 2단 출력하기
# for i in range(1, 10):
#     print(f"2 x {i} = {2*i}")

# 1~5단 출력하기
# 필요한 변수 : 2개(몇 단을, 몇 siu를 곱할건지)
# 몇 단을 출력할건지 : 1~5
# 몇 siu를 곱할건지 : 1~9

# 바깥 for문은 단을 늘리고
# 안쪽 for문은 곱할 siu를 늘리도록 구성

# for hou in range(1, 6):
#     for siu in range(1, 10):
#         print(f"{hou} x {siu} = {hou*siu}")
#     print(f"---{i}단 끝---")

# for dan in range(2, 10, 2):
#     for su in range(1, 10):
#         print(f"{dan} x {su} = {dan*su}")

# for dan in range(1, 10):
#     for su in range(1, 10):
#         if dan % 2 == 0:
#             print(f"{dan} x {su} = {dan*su}")
