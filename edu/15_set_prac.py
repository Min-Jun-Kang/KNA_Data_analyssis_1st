# # 실습 / 셋으로 중복 센서 제거하기

# Id_list = [
#     "WQR_06",
#     "WQR_01",
#     "WQR_01",
#     "WQR_01",
#     "WQR_01",
#     "WQR_06",
#     "WQR_03",
#     "WQR_05",
# ]

# Id_set = set(Id_list)
# print(Id_set)
# sorted = sorted(Id_set)
# print(sorted)
# print(f"종류 수 : {len(Id_set)}")


# # 실습 / 두 라인의 센서 구성 비교하기

# ID_set1 = {"WQR_01", "WQR_02", "WQR_03", "WQR_04", "WQR_05", "WQR_06"}
# ID_set2 = {
#     "WQR_03",
#     "WQR_01",
#     "WQR_05",
#     "WQR_10",
#     "WQR_08",
#     "WQR_09",
# }

# set_union = ID_set1.union(ID_set2)
# set_inter = ID_set1.intersection(ID_set2)
# set_dif1 = ID_set1.difference(ID_set2)
# set_dif2 = ID_set2.difference(ID_set1)

# print(f"전체 : {set_union}")
# print(f"공통 : {set_inter}")
# print(f"A만 : {set_dif1}")
# print(f"B만 : {set_dif2}")

# # 실습 / 두 시점의 이벤트 센서 추적하기

# set_yester = {"WQR_01", "WQR_02", "WQR_03", "WQR_04", "WQR_05", "WQR_06"}
# set_today = {
#     "WQR_03",
#     "WQR_01",
#     "WQR_05",
#     "WQR_10",
#     "WQR_08",
#     "WQR_09",
# }

# diff_today = set_today.difference(set_yester)  # 오늘자로 차집합을 구해야 신규 이상
# set_inter = set_yester.intersection(set_today)  # 공통 이상

# print(f"신규 이상 : {diff_today}")
# print(f"지속 이상 : {set_inter}")
