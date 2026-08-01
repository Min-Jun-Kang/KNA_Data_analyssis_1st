# # 실습 / 센서를 튜플로 묶고 꺼내기

# sensor_tuple = ("모터온도", 78)
# index_0 = sensor_tuple[0]
# index_1 = sensor_tuple[1]
# unpack_1, unpack_2 = sensor_tuple

# print(f"인덱스 0번: {index_0}")
# print(f"인덱스 1번: {index_1}")
# print(f"언패킹 : {unpack_1}, {unpack_2}")


# # 실습 / 튜플 리스트를 반복 처리하기

# tuple_list = [("온도센서", 70), ("회전센서", 90), ("펌프센서", 100), ("압력센서", 80)]

# for name, value in tuple_list:
#     if value > 80:
#         print(f"{name} 경고!!!!")

# # 실습 / 중첩 튜플로 센서 위치 관리하기

# sensor_tup = [
#     ("온도센서", 80, (7, 8)),
#     ("압력센서", 90, (4, 10)),
#     ("회전센서", 100, (8, 19)),
# ]

# for name, value, position in sensor_tup:
#     x, y = position
#     print(f"센서 이름 : {name}, 센서 위치 : ({x}, {y})")

# for name, value, position in sensor_tup:
#     x, y = position
#     if x <= 5:
#         print(f"x<=5 이하인 센서 : {name}")
