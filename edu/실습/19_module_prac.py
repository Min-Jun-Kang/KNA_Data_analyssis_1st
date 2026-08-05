# 실습 1번 / import 세 방식으로 모듈 가져오기

# ① import 모듈명으로 통째로 가져와 모듈명.기능() 으로 사용
import math

print(math.sqrt(100))
# ② from 모듈 import 기능 으로 일부만 가져와 모듈명 없이 사용
from math import sqrt

print(sqrt(100))
# ③ import 모듈 as 별명 으로 별명.기능() 으로 사용
import math as m

print(m.sqrt(100))

# ④ 세 방식의 출력이 같은지 확인

# 실습 2번 / 표준 라이브러리로 센서 값 만들기

# ① random 모듈을 import
import random

# ② randint로 무작위 센서값을 만들어 출력
sensor_value = random.randint(1, 100)
print(f"무작위 센서값: {sensor_value}")
# ③ math 모듈로 그 값을 가공(제곱근)
sqrt_value = math.sqrt(sensor_value)
# ④ 다시 실행하면 값이 달라지는지 확인
print(f"가공한 센서 값: {sqrt_value}")

# 실습 3번 / os로파일존재확인하기

# ① os를 import

import os

# ② path.join으로 폴더와 파일 이름을 이어 경로를 만들기
file_path = os.path.join(os.getcwd(), "08_press.csv")
# ③ path.exists로 그 경로가 있는지 참·거짓 확인
print(os.path.exists(file_path))
# ④ if로 있으면·없으면 다른 메시지 출력
if os.path.exists(file_path):
    print("파일이 있습니다.")
else:
    print("파일이 없습니다.")

# 실습 4번 / datetime으로 점검 기록 남기기

# ① os와 datetime을 import
import os, datetime

# ② listdir로 폴더 파일 수를 구하기
file_count = len(os.listdir(os.getcwd()))
# ③ datetime.now로 현재 시각을 담기
time_check = datetime.datetime.now()
# ④ f-string으로 파일 수와 시각을 한 문장으로 출력
print(f"파일 수: {file_count}, 점검 시간: {time_check}")

# 실습 5번 / os로 폴더 목록 살펴보기

# ① os 모듈을 import
import os

# ② getcwd로 현재 작업 폴더를 확인
print(os.getcwd())
# ③ listdir로 폴더 안 목록을 변수에 담기
file_list = os.listdir(os.getcwd())
# ④ for로 목록을 하나씩 출력하고 csv만 골라 출력
for file in file_list:
    print(f"파일 목록 : {file}")
    if file.endswith(".csv"):
        print(f"csv 파일 : {file}")

# 실습 6번 / 폴더에서 csv 파일만 골라내기

# ① os를 import하고 listdir로 폴더 목록을 구하기
import os

file_list = os.listdir(os.getcwd())
csv_name_list = []
# ② for-if로 .csv로 끝나는 이름만 빈 리스트에 모으기
for file in file_list:
    if file.endswith(".csv"):
        csv_name_list.append(file)
# ③ 모은 csv마다 path.join으로 전체 경로를 만들기
csv_list = []
for name in csv_name_list:
    csv_list.append(os.path.join(os.getcwd(), name))
# ④ 골라낸 csv 목록을 출력
print(f"csv 파일 목록 : {csv_list}")
