# # 수학 관련 모듈을 불러옵니다
# import math

# # 해당 모듈이름.함수() 식으로 호출해야한다
# result = math.sqrt(16)
# print(result)

# # -----------------------------------
# # 수학 관련 모듈에서 sqrt 기능만 불러옵니다
# from math import sqrt

# # 이젠 sqrt만 불러도 됩니다
# result = sqrt(16)
# print(result)

# # -----------------------------------
# # math라는 모듈 이름 다 쓰기 귀찮아서 줄여봅시다
# import math as mt

# # 별칭으로 가져온 모듈 이름을 언급해봅시다
# result = mt.sqrt(16)
# print(result)

# # datetime 모듈을 가져옵니다
# import datetime as dt

# # datetime의 now()는 현재의 지역 날짜와 시간을 반환합니다.
# now = dt.datetime.now()
# print(now)  # 2026-08-05 11:19:45.776780
# print(type(now))  # <class 'datetime.datetime'>

# 표준 라이브러리의 math 모듈
import math

print(math.sqrt(9))  # 제곱근값 3.0
print(math.ceil(4.2))  # 올림값 5
print(2**3)  # 2의 2승 = 2 * 2 * 2 = 8 math와 무관

# math에서 sqrt, ceil 두개만 사용한다면 이렇게 써도 됩니다
from math import sqrt, ceil

print(sqrt(9))
print(ceil(4.2))

print("==========================")

# 표준 라이브러리의 random 모듈
import random

print(random.randint(1, 10))  # 1~10 중 무작위 정수
print(random.choice(["정상", "경고", "위험"]))  # 셋 중 무작위

print("==========================")

# 표준 라이브러리의 datetime 모듈
import datetime

# datetime 모듈 안의 datetime 클래스에서 지원하는 now() 함수 호출
now = datetime.datetime.now()
print(now)  # 2026-08-05 13:18:26.838908

print("==========================")
# 모듈 도움말 보기 : 참고만 하고 구글링한 웹사이트에서 봅시다!
# print(dir(math))
# help(math.sqrt)
