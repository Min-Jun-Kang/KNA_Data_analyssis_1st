# 학생들의 점수를 가져와서
# 각 학생별 합계와
# 모든 학생들의 평균 점수를 내는 코드
import os
import csv
import sys

# 전체 학생 합계 및 평균 구하기
sum_all = 0
student_count = 0
avg_all = 0
# 1. 파일을 연다
file_path = os.path.join("edu", "data", "student_scores.csv")
student_dic = {}
# 파일이 존재하는지 확인하고 파일이 없다면 프로세스 강제 종료
if not os.path.exists(file_path):
    sys.exit(-1)
# 2. 파일 내용으로부터 리스트 데이터를 얻는다.
# with open(file_path, "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         name = row.get("\ufeff이름", "(이름없음)")
#         kor = int(row.get("국어", "0"))
#         eng = int(row.get("영어", "0"))
#         math = int(row.get("수학", "0"))
#         # print(f"{name} {kor} {eng} {math}")
#         # 3. 점수 계산 (합계, 평균)
#         sum = kor + eng + math
#         sum_all += sum
#         avg = round(sum / 3, 2)
#         avg_all += avg
#         student_count += 1
#         # 4. 결과를 화면에 보여준다.
#         print(f"{name}-> 합계: {sum}, 평균:{avg}")

# print(
#     f"학생의 전체 수: {student_count}, 합산: {sum_all}, 평균: {round(avg_all/student_count ,2)}"
# )


# 실습
# 10_student_score.py를 기반으로
# 1. 최고점 학생, 최저점 학생도 찾아서 출력해보기
# 2. 실행 끝날 때 각 과목별 평균 출력

kor_max_score = 0
kor_max_name = ""
kor_min_score = 100
kor_min_name = ""
eng_max_score = 0
eng_max_name = ""
eng_min_score = 100
eng_min_name = ""
math_max_score = 0
math_max_name = ""
math_min_score = 100
math_min_name = ""
sum_max_score = 0
sum_max_name = ""
sum_min_score = 300
sum_min_name = ""
sum_kor = 0
sum_eng = 0
sum_math = 0
student_count = 0
with open(file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row.get("\ufeff이름", "(이름없음)")
        kor = int(row.get("국어", "0"))
        eng = int(row.get("영어", "0"))
        math = int(row.get("수학", "0"))
        sum = kor + eng + math
        if kor > kor_max_score:
            kor_max_score = kor
            kor_max_name = name
        if kor < kor_min_score:
            kor_min_score = kor
            kor_min_name = name
        if eng > eng_max_score:
            eng_max_score = eng
            eng_max_name = name
        if eng < eng_min_score:
            eng_min_score = eng
            eng_min_name = name
        if math > math_max_score:
            math_max_score = math
            math_max_name = name
        if math < math_min_score:
            math_min_score = math
            math_min_name = name
        if sum > sum_max_score:
            sum_max_score = sum
            sum_max_name = name
        if sum < sum_min_score:
            sum_min_score = sum
            sum_min_name = name
        sum_kor += kor
        sum_eng += eng
        sum_math += math
        student_count += 1

print(f"총 학생 수: {student_count}")
print(f"국어 점수 합계: {sum_kor}, 평균: {round(sum_kor/student_count, 2)}")
print(f"영어 점수 합계: {sum_eng}, 평균: {round(sum_eng/student_count, 2)}")
print(f"수학 점수 합계: {sum_math}, 평균: {round(sum_math/student_count, 2)}")
print(f"국어 점수 최고점자: {kor_max_name}, 점수: {kor_max_score}")
print(f"국어 점수 최저점자: {kor_min_name}, 점수: {kor_min_score}")
print(f"영어 점수 최고점자: {eng_max_name}, 점수: {eng_max_score}")
print(f"영어 점수 최저점자: {eng_min_name}, 점수: {eng_min_score}")
print(f"수학 점수 최고점자: {math_max_name}, 점수: {math_max_score}")
print(f"수학 점수 최저점자: {math_min_name}, 점수: {math_min_score}")
print(f"합산 점수 최고점자: {sum_max_name}, 점수: {sum_max_score}")
print(f"합산 점수 최저점자: {sum_min_name}, 점수: {sum_min_score}")
