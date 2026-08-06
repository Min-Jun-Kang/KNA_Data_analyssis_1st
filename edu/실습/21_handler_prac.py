# 실습 1번 / 일부러 에러를 내고 트레이스백을 읽어 오류 종류와 위치 찾기

# ① 글자를 숫자로 바꾸는 코드로 ValueError를 내 보기
# # ValueError: invalid literal for int() with base 10: '스물' / line 4
# temp = int("스물")
# # ② 0으로 나누는 코드로 ZeroDivisionError를 내 보기
# ZeroDivisionError: division by zero / line 7
# temp = 10 / 0
# ③ 정의하지 않은 변수를 써서 NameError를 내 보기
# # NameError: name 'temp' is not defined / line 10
# print(temp)
# ④ 각 트레이스백에서 오류 종류와 줄 위치를 읽기

# # 실습 2번 / try-except로 오류 넘기기

# origin = input("온도: ")

# temp = 0

# print(f"입력한 온도는 {origin}")
# try:
#     temp = int(origin)
# except ValueError:
#     # ValueError인 상황이였다면 여기로 예외처리
#     print("숫자 아니면 왜 저를 부르셨나요? 0으로 생각할게요")

# next_temp = temp + 10
# print(f"10도만 더 높으면 {next_temp}")

# 실습 3번 / 구체적 예외로 입력 검증하기

temp = input("숫자를 입력하세요: ")
# ① 입력을 int로 바꾸는 코드를 try에 넣기
try:
    num = int(temp)
    check = 10 / num
    print(f"10을 입력한 값으로 나눈 값 : {check}")
# ② ValueError를 except로 잡아 안내
except ValueError:
    print("숫자를 입력해주세요")
    print("에러는 뜨지 않는다.")
# ③ 여러 except로 ZeroDivisionError도 구분해 처리
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
    print("에러는 뜨지 않는다.")
# ④ 잘못된 입력을 넣어 프로그램이 멈추지 않는지 확인
