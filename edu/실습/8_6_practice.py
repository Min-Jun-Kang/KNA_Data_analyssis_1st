# 실습 1번 / open으로 파일 읽기

# ① open으로 파일을 읽기 모드 r, utf-8로 열기
f = open("practice_1.txt", "r", encoding="utf-8")
# ② read로 전체를 한 문자열로 읽어 출력
read_txt = f.read()
print(f"read로 출력: {read_txt}")
f.close()
# ③ readlines로 줄 리스트로 읽어 출력
with open("practice_1.txt", "r", encoding="utf-8") as f:
    readlines_txt = f.readlines()
print(f"readlines로 출력: {readlines_txt}")
# ④ 두 방식의 결과 차이를 비교하고 파일을 close

# print("==================================================")

# 실습 2번 / with open으로 파일에 쓰기

# ① with open으로 파일을 쓰기 모드 w, utf-8로 열기
with open("practice_2.txt", "w", encoding="utf-8") as f:
    # ② write로 내용을 쓰기(줄을 나눌 땐 줄바꿈 기호)
    f.write("실습 문제 2번입니다.\n")
    f.write("화이팅\n")
# ③ with 블록이 끝나면 파일이 자동으로 닫힘
# ④ r 모드로 다시 열어 쓴 내용을 확인
with open("practice_2.txt", "r", encoding="utf-8") as f:
    with_open_txt = f.read()
    print(f"write 모드 출력 : \n{with_open_txt}")

# print("==================================================")

# 실습 3번 / a 모드로 기록 이어붙이기

# ① with open으로 파일을 추가 모드 a로 열기
with open("practice_2.txt", "a", encoding="utf-8") as f:
    # ② write로 새 기록 문장을 쓰기
    f.write("실습 3번은 이어쓰기 입니다.")
# ③ w 모드와 달리 기존 내용이 보존됨을 확인
# ④ r 모드로 열어 전체가 쌓였는지 확인
with open("practice_2.txt", "r", encoding="utf-8") as f:
    a_mode_txt = f.read()
    print(f"append 모드 출력 : \n{a_mode_txt}")

# print("==================================================")

# 실습 4번 / csv.reader로 CSV 읽기

# ① csv 모듈을 import
import os
import sys
import csv

csv_path = os.path.join(os.getcwd(), "edu", "data", "08_press.csv")

# if not os.path.exists(csv_path):
#     print("파일이 없습니다")
#     sys.exit(1)

# print("파일이 있습니다")

# ② with open으로 CSV를 읽기 모드 utf-8로 열기

with open(csv_path, "r", encoding="utf-8") as f:
    # ③ csv.reader로 reader 객체를 만들기
    reader = csv.reader(f)
    # ④ for로 각 행(리스트)을 하나씩 꺼내 출력
    for row in reader:
        print(f"각 행 출력 : {row}")

# print("==================================================")

# 실습 5번 / csv.writer로 CSV 쓰기

# ① csv를 import
import os
import csv

csv_path = os.path.join("edu", "실습", "practice5.csv")
# ② with open으로 w·utf-8·newline 옵션으로 열기
with open(csv_path, "w", encoding="utf-8", newline="") as f:
    # ③ csv.writer로 writer 객체를 만들기
    writer = csv.writer(f)
    # ④ writerow로 헤더와 각 데이터 행을 쓰기
    writer.writerow(["시각", "설비", "상태"])
    writer.writerow(["09:00", "PUMP-01", "정상"])
    writer.writerow(["10:00", "PUMP-02", "주의"])

# print("==================================================")

# 실습 6번 / CSV 읽어 조건 저장하기

# ① csv를 import
import csv
import os

csv_path = os.path.join("edu", "data", "08_press.csv")

float_list = []
header = []

with open(csv_path, "r", encoding="utf-8", newline="") as f:
    # ② csv.reader로 읽고 첫 줄 헤더는 건너뛰기
    reader = csv.reader(f)
    header = next(reader)
    # ③ 값을 float로 변환해 기준(90) 초과 행만 리스트에 모으기
    for row in reader:
        if float(row[4]) > 90:
            float_list.append(row)
# ④ csv.writer로 모은 행들을 새 CSV에 저장

csv_path2 = os.path.join("edu", "실습", "practice6_result.csv")

with open(csv_path2, "w", encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    for row in float_list:
        csv_writer.writerow(row)

# print("==================================================")

# 실습 7번 / 구체적 예외로 입력 검증하기

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
