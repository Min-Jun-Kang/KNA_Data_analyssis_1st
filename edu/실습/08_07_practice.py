# 실습 1번 / finally로 파일 안전하게 닫기

# ① try 블록에서 파일을 열어 처리
try:
    f = open("open_file.txt", "r", encoding="utf-8")
    lines = f.readlines()
    print(lines)
# ② 처리 도중 오류가 날 수 있음을 가정
except:
    print("오류가 났습니다.")
# ③ finally 블록에 close를 넣어 오류 여부와 상관없이 닫기
finally:
    f.close()
# ④ 일부러 오류를 내도 finally가 실행되는지 확인
# 모드를 r 또는 w를 통해 코드가 정상 작동하거나 오류나는지 확인가능

# 실습 2번 / 반복문에서 불량 줄 건너뛰기

# 소숫점 이하의 숫자가 포함된 숫자들을 20개정도 만들어 문자로 배열에 담기
# 그 사이에 엉뚱한 글자들이 포함된 내용도 포함시키기
# 위 리스트 데이터를 사용해서 문제를 풀기

float_list = [
    "123.123",
    "1234.123",
    "12.32",
    "443.33",
    "김도진",
    "파이썬",
    "9809.13213",
    "123222.1123",
    "python",
    "12.1",
    "121.23",
    "차승윤",
    "최영준",
    "1223.123",
    "13.121",
    "1231.123",
    "1.12",
    "넥스트서퍼",
    "데이터분석",
    "123123.123123",
]
total = 0
count = 0
# ① 여러 측정값(일부는 숫자가 아님)을 반복
for i in float_list:
    # ② try에서 float로 변환
    try:
        float_num = float(i)
        total += float_num
    # ③ 변환 실패(ValueError) 시 continue로 그 줄만 건너뛰기
    except ValueError:
        count += 1
        continue
# ④ 정상 값만 합계에 더해 출력
print(f"리스트 안의 정상 값 합계: {total}")
print(f"리스트 안의 이상 값: {count}개")

# 실습 3번 / 여러 파일 묶어 처리하기

# 다음과 같은 식의 리스틀 만들어 반복문 처리
# for문으로 문자열을 꺼내어 해당 이름의 파일들을 열어보기 시도

# file_names = ["파일이름", "파일이름", ...]

import os

file_names = [
    "08_press.csv",
    "09_ict_inspection_dirty.csv",
    "09_ict_inspection.csv",
    "이상한 파일",
    "result.csv",
]
file_count = 0
not_file_count = 0
# ① 여러 파일 이름을 반복
for i in file_names:
    # ② try에서 파일을 열어 처리
    try:
        file_path = os.path.join("data", i)
        with open(file_path, "r", encoding="utf-8", newline="") as f:
            file_count += 1
    # ③ 없는 파일(FileNotFoundError) 시 continue로 건너뛰기
    except:
        not_file_count += 1
        continue
# ④ 처리한 파일 수를 세어 출력
print(f"처리한 파일 개수: {file_count}개")
print(f"처리 못한 파일 개수: {not_file_count}개")

# 종합 실습 / 1단계 CSV 읽기

# data/09_ict_inspection_dirty.csv 를 읽어 헤더와 데이터 행을 분리하고, 데이터가 몇 행인지 출력하는 함수를 만든다.
# 함수로 만들어 이후 단계에서 그대로 재사용한다.
# 예외 처리
# 파일이 없는 경우 FileNotFoundError가 발생한다.
# 안내 메시지를 출력한 뒤 빈 결과(빈 header, 빈 rows)를 반환하도록 한다.

import os
import csv


def data_print(path):
    try:
        count = 1
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
            rows = []
            print(f"헤더 : {header}")
            for row in reader:
                if len(row) > 0:
                    rows.append(row)
            for i in rows:
                print(f"{count}행 : {i}")
                count += 1
            return header, rows
    except FileNotFoundError:
        print("파일이 존재하지 않습니다. [], []")
        return [], []


file_path = os.path.join("data", "09_ict_inspection_dirty.csv")
file1_path = os.path.join("data", "empty.txt")

data_header, data_rows = data_print(file_path)

header1, rows1 = data_print(file1_path)
# 종합 실습 2번 / 2단계 조건 분류

# 만들어야 할 것
# 1단계 데이터를 설비별로 분류해, 각 설비에 몇 개의 데이터가 있는지 출력한다.
# 딕셔너리의 키는 설비명, 값은 행 리스트다.
# 핵심 패턴
# 처음 보는 설비명이면 빈 리스트를 먼저 만들고, 거기에 행을 추가하는 방식이다.


def data_classify(rows):
    data_dict = {}
    for row in rows:
        facility_name = row[1]
        if facility_name not in data_dict:
            data_dict[facility_name] = []
        data_dict[facility_name].append(row)
    return data_dict


data_dict = data_classify(data_rows)
# print(data_dict)
for key, value in data_dict.items():
    print(f"부품: {key}, 개수: {len(value)}")

# 종합 실습 3번 / 3단계 통계 함수

# 만들어야 할 것
# 특정 칸의 숫자 데이터로 개수, 평균, 최솟값, 최댓값을 계산하는 함수.
# 주의할 점
# 숫자가 아닌 값은 건너뛴다.
# · 값이 하나도 없으면 None을 반환해 0으로 나누는 오류를 막는다.


def data_commute(rows):
    data_dict = {}
    count = 0
    for row in rows:
        name_key = row[0]
        data_dict[row[0]] = row[1:]
    for key, value in data_dict.items():
        data_list = []
        for i in value:
            try:
                data_list.append(float(i))
            except ValueError:
                continue
        if len(data_list) == 0:
            return None
        else:
            print(
                f"설비명: {key} -> 최댓값: {max(data_list)}, 최솟값: {min(data_list)}, 데이터 개수: {len(data_list)}, 평균값: {round(sum(data_list)/len(data_list), 2)}"
            )


data_commute(data_rows)


# 종합 실습 4번 / 4단계 불량 방어

# 만들어야 할 것
# 온도를 처리하며 숫자로 못 바꾸는 값과 정상 범위를 벗어난 값을 모두 걸러낸다.
# 불량 줄은 번호와 이유를 함께 기록한다.
# 한 함수에 모이는 것들
# try-except · continue · raise · as e 가 한 함수에 모두 들어간다.
# 앞서 배운 게 여기서 총정리된다.
