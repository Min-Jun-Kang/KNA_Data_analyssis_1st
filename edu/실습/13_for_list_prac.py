# # 실습 / 리스트에서 값 고르기

# temps = [28, 22, 25, 30, 32, 31, 40, 12]

# for i in temps:
#     if i >= 30:
#         print(f"고온: {i}")

# 실습 / 두 조건을 모두 만족하는 값 고르기

# hours = [3, 8, 12, 6, 10, 4, 9]
# for h in hours:
#     if h >= 5 and h <= 10:
#         print(h)

# # 실습 / 조건에 맞는 값만 골라 평균 구하기

# temps = [22, 24, 25, 30, 31, 32, 36]

# count = 0
# total = 0

# for i in temps:
#     if i > 30:
#         total += i
#         count += 1

# print(f"고온 평균 : {total/count}")

# # 실습 / 조건에 맞는 값으로 새 리스트 만들기

# temps = [22, 24, 25, 30, 31, 32, 36]
# empty = []

# for i in temps:
#     if i > 30:
#         empty.append(i)

# print(f"원본 리스트 : {temps}")
# print(f"새 리스트 : {empty}")
# print(f"새 리스트 길이 : {len(empty)}")

# # 실습 / 값을 가공해서 새 리스트 만들기

# temps = [22, 24, 25, 30, 31, 32, 36]
# empty_list = []
# for i in temps:
#     F_temps = round(i * 1.8 + 32, 2)
#     empty_list.append(F_temps)

# print(f"{empty_list}")

# 실습 / 센서 데이터 종합 분석

temps = [22, 24, 25, 30, 31, 32, 36]
empty_temps = []
total_1 = 0
total_2 = 0

for i in temps:
    total_1 += i
    if i > 30:
        empty_temps.append(i)

for i in empty_temps:
    total_2 += i

print(
    f"전체 평균 : {round(total_1/len(temps),1)} / 고온 개수 : {len(empty_temps)} / 고온 평균 : {round(total_2/len(empty_temps),1)}"
)
