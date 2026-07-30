# # 실습 / while로 목표값 도달까지 반복하기

# count = 0
# goal = 10

# while count != goal:
#     count = int(input("숫자를 입력하세요 > "))
# print("정답입니다!")

# # 실습 / UP DOWN 게임
# # 1~50 중 하나의 숫자를 정답으로 저장
# # 사용자의 입력값 기준으로 정답이 UP인지 DOWN인지 출력
# # 정답이 나오면 정답과 게임 종료를 출력

# while True:
#     answer_num = int(input("1~50 중 하나의 숫자를 골라주세요 > "))
#     if answer_num < 1 or answer_num > 50:
#         print("숫자를 다시 입력해주세요!!")
#     else:
#         break

# print("==========게임이 시작 됩니다.==========")

# while True:
#     user_input = int(input("1~50 중 정답을 골라주세요 > "))
#     if user_input < 1 or user_input > 50:
#         print("숫자를 다시 입력해주세요!!")
#     else:
#         if user_input > answer_num:
#             print("DOWN!!")
#         elif user_input < answer_num:
#             print("UP!!")
#         else:
#             print("정답 입니다!!")
#             break

# print("==========게임이 종료 되었습니다.==========")

# # 실습 / 플래그로 조건 만족 값 검색하기

# flag = False

# num = int(input("횟수를 입력하세요 > "))

# for i in range(num):
#     temp = int(input("측정값을 입력하세요 > "))
#     if temp > 80:
#         flag = True
#         break

# if flag == True:
#     print("발견!")
# else:
#     print("없음!")
