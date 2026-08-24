# while은 특정 조건(횟수 제한 없음)이 False가 될 때까지
# 반복해야 하는 경우 사용

# 1. 반복 전 변수(시작 값) 존재 여부
# 2. 반복을 하다가 언젠가 False가 될 수 있는 종료 조건 포함 여부
# 3. 변수가 거짓 방향으로 값이 변경되는지

# break로 반복 중단하기
# 원하는 시점에 종료 반복문 종료 가능(굳이 반복문 전체를 돌 필요가 없음)
# 반복문 중 break를 만나면 반복문 종료

# input_sum = 0

# while True:
#     user_input = int(input("값을 입력하세요. 값의 누적이 15를 넘으면 종료합니다."))
#     input_sum += user_input  # 누적값 업데이트
#     if input_sum > 15:
#         print(f"누적 합계 : {input_sum} 입력을 종료합니다.")
#         break  # 반복문 강제 종료

# # 사용자 입력 값을 확인만 하고 저장할 필요가 없는 경우
# while True:
#     x = input("입력 (종료는 q를 입력하세요): ")
#     if x == "q":
#         break
#     print("입력받은 값: ", x)

# n = int(input("횟수: "))

# for i in range(n):
#     v = int(input("측정값: "))

#     if v > 80:
#         print("이상 발생")
#         print(f"가동 횟수: {n}")
#         break
#     else:
#         print("정상 상태")

# continue로 회차 건너뛰기
