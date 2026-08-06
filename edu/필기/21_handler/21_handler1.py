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
