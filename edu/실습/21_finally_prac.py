# # 실습 1번 / finally로 파일 안전하게 닫기

# # ① try 블록에서 파일을 열어 처리
# try:
#     f = open("open_file.txt", "w", encoding="utf-8")
#     lines = f.readlines()
#     print(lines)
# # ② 처리 도중 오류가 날 수 있음을 가정
# except:
#     print("파일이 존재하지 않습니다.")
# # ③ finally 블록에 close를 넣어 오류 여부와 상관없이 닫기
# finally:
#     f.close()
# # ④ 일부러 오류를 내도 finally가 실행되는지 확인
# # 모드를 r 또는 w를 통해 코드가 정상 작동하거나 오류나는지 확인가능

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
        file_path = os.path.join("edu", "data", i)
        with open(file_path, "r", encoding="utf-8", newline="") as f:
            file_count += 1
    # ③ 없는 파일(FileNotFoundError) 시 continue로 건너뛰기
    except:
        not_file_count += 1
        continue
# ④ 처리한 파일 수를 세어 출력
print(f"처리한 파일 개수: {file_count}개")
print(f"처리 못한 파일 개수: {not_file_count}개")
