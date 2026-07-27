# # 실습 :
# # 결과 값 :
# # 설비 : PUMP_A > str
# # 상태 : 정상 > str
# # 가동 : 1200 > int
# # 점검 : 2026-07-16 > str

# name = input("설비 이름을 적어주세요 > ")
# status = input("설비 상태를 적어주세요 > ")
# time = int(input("설비 가동 시간을 적어주세요 > "))
# date = input("설비 점검 시간을 적어주세요 > ")

# print("설비:", name, "\n상태:", status, "\n가동:", time, "\n점검:", date)

# # 실습 [:n] start 생략

# word = "temp_sensor"

# print("4글자만 추출 >", word[:4])

# # 실습 [n:] end 생략

# word = "temp_sensor"

# print("5번부터 끝까지 추출 >", word[5:])

# # 실습 [-n:] 음수 슬라이싱 (뒤n글자)

# word = "sensor_01"

# print("뒤 2글자 출력 >", word[-2:])

# # 실습 step으로 건너뛰기

# word = "PYTHON"

# print("두 칸씩 건너뛴 글자 출력 >", word[::2])

# # 실습 문자열 뒤집기

# word = "PYTHON"

# print("문자열 뒤집어서 출력 >", word[::-1])

# # 실습 len()으로 길이 확인

# phone_num = "01012345678"

# print("전화번호 길이:", len(phone_num))

# # 실습 .count()로 개수 세기

# word = "a,b,c,d"
# print("문자열에 포함된 ,의 개수: >", word.count(","))


# # 실습 / startswith(), endswith()

# str = "sensor_log.csv"

# print(str.startswith("sensor"))
# print(str.endswith(".csv"))

# # 실습 / 대문자 바꾸기

# word = "ready"
# WORD = word.upper()
# print(WORD)

# # 실습 / 소문자 바꾸기

# WARN = "WARNING"

# warn = WARN.lower()

# print(warn)

# # 실습 / capitalize(), title() 이용

# name = "kang min jun"
# test = "I'm full"

# # 실습 / 대문자 소문자 확인

# word_1 = "ABC"
# word_2 = "abc"
# word_3 = "Abc"

# print(word_1.isupper())  # True
# print(word_2.islower())  # True
# print(word_3.isupper())  # False
# # print(word_3.islower()) # False

# # 실습 / 파일명 규칙 한 번에 점검하기

# file = "Sensor_LOG.CSV"

# file_lower = file.lower()


# print(file.startswith("sensor"))
# print(file.endswith(".csv"))
# print(file_lower.startswith("sensor"))
# print(file_lower.endswith(".csv"))


# # 실습 / 문자열 형태 바꿔서 출력하기

# str = "   Warning      "

# # 출력 예상, 체이닝 해보기

# str1 = str.lower()
# str2 = str.strip().lower()

# print("[" + str1 + "]")
# print("[" + str2 + "]")

# # 실습 / 쉼표 기준으로 나누기

# word = "a,b,c,d"
# word_list = word.split(",")
# print(word_list)

# # 실습 / join 이용해서 리스트 합치기

# list1 = ["2025", "01", "15"]
# print("-".join(list1))

# # 실습 / python -> pyThon으로 바꾸기

# word = "python"

# # strip + capitalize
# print(word[:2] + word.strip("py").capitalize())

# # strip + title
# print(word[:2] + word.strip("py").title())

# # replace
# print(word.replace("t", "T"))

# # 슬라이싱 + upper 사용
# print(word[:2] + word[2].upper() + word[3:])

# # 인덱싱으로 글자 하나씩 연결
# print(word[0] + word[1] + word[2].upper() + word[3] + word[4] + word[5])

# # split, join 이용
# print("T".join(word.split("t")))
# print(word[2].upper().join(word.split("t")))

# # 실습 / 구분자 통째로 바꾸기

# date = "2025/01/15"
# date_list = date.split("/")  # ['2025', '01', '15']
# print("-".join(date_list))  # 2025-01-15

# # 실습 / csv 한 줄에서 값 꺼내 정리하기

# senten = "1, NORMAL ,25.3"
# print(senten.split(",")[1].strip().lower())
