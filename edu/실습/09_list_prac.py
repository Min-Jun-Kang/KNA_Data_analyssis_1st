# # 실습 / 나만의 데이터 리스트 만들기

# datas = [34, 35, 36, 32, 31]

# empty = []

# print(f"데이터리스트 출력: {datas}")
# print(f"데이터리스트 길이: {len(datas)}")
# print(f"빈 리스트 길이: {len(empty)}")

# # 실습 / 인덱스로 값 꺼내기

# datas = [34, 35, 36, 32, 31, 37]

# print(f"첫 번째 값: {datas[0]}")
# print(f"세 번째 값: {datas[2]}")
# print(f"마지막 값: {datas[-1]}")

# # 실습 / 인덱스로 꺼낸 값 계산

# datas = [20, 22, 29, 19, 18, 25]

# first_data = datas[0]
# last_data = datas[-1]
# datas_sum = first_data + last_data

# print(f"두 생산량의 합: {datas_sum} 두 생산량의 평균: {(datas_sum)/2}")

# # 실습 / 슬라이싱으로 구간 자르기

# # 4번

# temp_datas = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# temps_slice = temp_datas[:3]
# temps_last = temp_datas[-3:]

# print(temps_slice)
# print(temps_last)
# print(len(temps_slice))
# print(len(temps_last))

# # 5번

# datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# first = datas[:6]
# second = datas[-6:]

# print(first)
# print(second)
# print(len(first))
# print(len(second))


# # 실습 / 값 찾아 바꾸기

# temps = [26, 27, 24, 25, 240]

# print(240 in temps)  # 240이 존재하면 True
# temps[temps.index(240)] = 24
# print(temps)
# print(240 in temps)

# # 실습 / 측정 값 추가하기

# empty = []

# empty.append(100)
# empty.insert(0, 50)

# extend_list = [150, 200]

# empty.extend(extend_list)

# print(empty)

# # 실습 / 잘못된 값 제거하기

# datas = [1, 2, 3, 4, 5, 6, 7, 999]

# datas.remove(999)
# print(f"remove로 제거한 리스트: {datas}")
# print(f"꺼낸 값(datas.pop(2)): {datas.pop(2)}")
# del datas[0]
# print(f"값을 제거한 리스트: {datas}")

# 실습 / 정렬하고 탐색하기

temps = [10, 20, 30, 33, 31, 29, 28, 10, 19, 15]

temps.sort()
print(f"오름차순으로 정렬: {temps}")
temps.reverse()
print(f"리버스로 뒤집어 출력: {temps}")
print(f"10도가 몇 번인지 출력: {temps.count(10)}")
print(f"index로 처음 위치 출력: {temps.index(10)}")
