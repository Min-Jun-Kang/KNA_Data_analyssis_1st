# # 최댓값 찾기
# first = int(input("1번째 입력 값 > "))

# # 첫 번째 입력 값은 자동으로 최댓값이 됨 (비교할 값이 없기 때문)
# max_value = first

# # for문을 사용해서 입력을 4번 받고
# # 입력 받은 값중에서 가장 큰 값을 출력
# for i in range(4):
#     v = int(input(f"{i+2}번째 입력 값 > "))

#     # max_value에는 현 시점 최댓값
#     # v에는 방금 사용자가 입력한 값
#     # max_value와 v 값을 비교 더 큰 값을 재할당
#     if v > max_value:
#         max_value = v

# print(f"최댓값은 {max_value}입니다.")

# 리스트도 포문 가능

# total = 0

# for i in [4, 7, 6]:
#     if i > 5:
#         total += i
# print(f"합계는 {total}입니다.")

# # 빈 리스트에서 시작해 값 채우기

# temps = [25, 26, 24, 28]
# doubled = []
# for t in temps:
#     doubled.append(t * 3)
# print(doubled)

# # 조건에 맞는 값으로 새 리스트 만들기

temps = [25, 32, 28, 35, 27]
high = []
low = []
for t in temps:
    if t > 30:
        high.append(t)
    else:
        low.append(t)
print(f"high: {high}")
print(f"low: {low}")

# 복습 sort(): 원본 배열을 오름차순으로 정렬해줌
# 하지만 반환해주지 않기 때문에 print로 바로 찍으면 None 출력

print(low.sort())
print(f"low_sort: {low}")

# 리스트 안의 리스트

rows = [["펌프", 25], ["모터", 32]["압축기", 28]]
# 표 (행,열)처럼 한줄에 여러 값이 묶인 데이터
# 바깥 대괄호를 "행", 안쪽 인덱스 리스틀 "열"이라고 함

print(rows[0])
