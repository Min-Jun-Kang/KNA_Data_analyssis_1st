# # 딕셔너리
# # 순서 번호 대신 이름표로 값을 바로 찾는 자료구조
# # 센서 이름처럼 이름이 분명한 데이터에 가장 적합
# # 구조 : {키:값, 키:값}

# # data_class_list = ["태", "수", "영"]

# # # 딕셔너리로 정확하게 역할까지 부여

# # # key 하나당 한 개의 value
# # data_class_dict = {"반장": "태", "부반장": "수", "당번": "영"}

# # # 센서로 부터 얻는 예시 데이터로 딕셔너리를 만들어보기
# sensors = {"센서이름": "보일러", "모터온도": 78, "진동": 0.5}

# # print(sensors)
# # print(type(sensors))  # <class 'dict'>
# # empty = {}  # 빈 딕셔너리
# # print(type(empty))  # <class 'dict'>

# # print(sensors["센서이름"])
# # print(sensors["모터온도"])
# # print(sensors["진동"])

# # 기존에 있던 key의 값을 변경
# sensors["센서이름"] = "펌프"  # 센서이름 값 변경

# # 기존에 없던 key의 값으 추가
# sensors["펌프압력"] = 95
# sensors["유량"] = 42

# # 더 이상 필요없는 key와 그 value를 삭제
# del sensors["펌프압력"]
# del sensors["모터온도"]

# # # 더 이상 없는 key를 호출하면 에러 발생
# # print(sensors["모터온도"])

# # get으로 없는 키 안전하게 다루기

# print(sensors.get("센서이름"))
# print(sensors.get("모터온도"))

# # # 숫자가 담길거라 예상했지만
# # motor_degree = sensors.get("모터온도") # 에러 발생 모터온도에 None이 담겨서 int형과 연산 불가
# # get으로 꺼내올 때 안전하게 가져오기 위해 기본 값을 설정
# motor_degree = sensors.get("모터온도", 0)
# next_degree = motor_degree + 10

# print(next_degree)

# in으로 키 존재 확인하기
# 키 in 딕셔너리

# is_motor_degree_key = "모터온도" in sensors
# print(is_motor_degree_key)

# print(sensors)

# if is_motor_degree_key:
#     print("그런 키 있어요")
# else:
#     print("그런 키 없어요")


# if "모터온도" in sensors:
#     print("그런 키 있어요")
# else:
#     print("그런 키 없어요")

# # keys를 가져오기
# print(sensors.keys())
# # len을 통해 몇개의 key-value 조합들이 있는지 알아보기
# print(len(sensors))

# # keys 는모든이름표를, values는 모든 값을 한 번에 모은다.
# # 딕셔너리.keys()
# # 딕셔너리.values()

# sensors = {"모터온도": 78, "압력": 95}
# print(list(sensors.keys()))
# print(list(sensors.values()))
# avg = sum(sensors.values()) / len(sensors)
# print(avg)

# # items는 키와값을 짝으로 함께 꺼내 반복문 에서 가장 많이 쓰인다
# # for key, value in 딕셔너리.items()

# sensors = {"모터온도": 78, "진동": 0.5}
# for name, value in sensors.items():
#     print(name, "측정값:", value)

# # len은 딕셔너리에 담긴키-값 쌍이 몇 개인지 세어준다
# # len( 딕셔너리 )

# sensors = {"모터온도": 78, "진동": 0.5, "압력": 95}
# print(len(sensors))
# if len(sensors) < 5:
#     print("센서 데이터 누락 확인 필요")

# 예제 연습
# 나라 이름으로 정리
# 유럽 : 스페인(ESP), 프랑스(FRA), 독일(GER), 스위스(SWI), 네덜란드(NED)
# 아시아 : 한국(KOR), 일본(JPN), 이란(IRA), 사우디(SAU), 중국(CHI)
# 남미 : 아르헨티나(ARG), 브라질(BRA), 칠레(CHI), 콜롬비아(COL), 우루과이(URU)

# # 아시아 국가를 딕셔너리로 만들기

# korea = {"국가명": "대한민국", "약칭": "KOR"}
# japan = {"국가명": "일본", "약칭": "JPN"}

# # 아시아 나라들을 하나의 리스트로 모으기

# asia = [korea, japan]
# print(asia)

# 유럽 나라들을 하나의 리스트로 모으기

# europe = [
#     {"국가명": "스페인", "약칭": "ESP"},
#     {"국가명": "프랑스", "약칭": "FRA"},
#     {"국가명": "독일", "약칭": "DEU"},
#     {"국가명": "스위스", "약칭": "SUI"},
#     {"국가명": "네덜란드", "약칭": "NLD"},
# ]
# print(europe)

# for country in europe:
#     print(country.get("국가명", "없음"))

#     for key, value in country.items():
#         print(f"{key} : {value}")

# 포켓몬 1,2,3 진화단계를 딕셔너리로 만들고
# 그 포켓몬 딕셔너리들이 모인 배열을 만들기
# 그 배열 데이터를 화면에 print
# 가능하면 그 배열의 데이터들을 for-in을 사용해서 꺼내 print (선택사항)

# 1. 꼬부기 어니부기 거북왕
# 2. 이상해씨 이상해풀 이상해꽃
# 3. 파이리 리자드 리자몽
# 4. 피츄 피카츄 라이츄
# 5. 캐터피 단데기 버터플
# 6. 뿔충이 딱충이 독침붕
# 7. 구구 피죤 피죤투
# 8. 알통몬 근육몬 괴력몬
# 9. 고오스 고우스트 팬텀
# 10. 케이시 윤겔라 후딘

# pocket_mon = [
#     {"1단계": "꼬부기", "2단계": "어니부기", "3단계": "거북왕"},
#     {"1단계": "이상해씨", "2단계": "이상해풀", "3단계": "이상해꽃"},
#     {"1단계": "파이리", "2단계": "리자드", "3단계": "리자몽"},
#     {"1단계": "피츄", "2단계": "피카츄", "3단계": "라이츄"},
#     {"1단계": "캐터피", "2단계": "단데기", "3단계": "버터플"},
#     {"1단계": "뿔충이", "2단계": "딱충이", "3단계": "독침붕"},
#     {"1단계": "구구", "2단계": "피죤", "3단계": "피죤투"},
#     {"1단계": "알통몬", "2단계": "근육몬", "3단계": "괴력몬"},
#     {"1단계": "고오스", "2단계": "고우스트", "3단계": "팬텀"},
#     {"1단계": "케이시", "2단계": "윤겔라", "3단계": "후딘"},
# ]

# print(f"포켓몬 종류 : {pocket_mon}")

# for dic in pocket_mon:
#     for name, value in dic.items():
#         print(f"포켓몬 진화 단계 : {name}, 포켓몬 이름 : {value}")

# # 다음의 두 딕셔너리는 같은 key들을 가지고 있다.
# # 실제 데이터
# values = {"모터온도": 95, "압력": 88}
# # 임계치 데이터
# limits = {"모터온도": 90, "압력": 90}

# for name, value in values.items():
#     print(f"{name} : {value}")
#     # limits 딕셔너리에서도 name의 key가 있다면 비교할 수 있다.
#     if value > limits[name]:
#         print(name, "경고")

# # 만약 두개의 딕셔너리의 길이가 다르다면

# # 실제 데이터
# values = {"모터온도": 95, "압력": 88, "진동": 70}
# # 임계치 데이터
# limits = {"모터온도": 90, "압력": 90}

# # for name, value in values.items():
# #     print(f"{name} : {value}")
# #     # limits 딕셔너리에서도 name의 key가 있다면 비교할 수 있다.
# #     if value > limits[name]: # 진동이라는 key가 없기에 에러가 난다.
# #         print(name, "경고")

# for name, value in values.items():
#     print(f"{name} : {value}")
#     # limits 딕셔너리에서도 name의 key가 있다면 비교할 수 있다.
#     # get을 이용하면 에러 없이 비교는 가능하지만 기본 값을 잘 설정해야한다.
#     if value > limits.get(name, 90):
#         print(name, "경고")

# # update로 여러 값 한 번에 갱신하기
# # 딕셔너리.update( 새 딕셔너리 )
# # 동일한 key 값이 있다면 그 key의 value 값을 변화시키고 key가 없다면 딕셔너리에 추가
# # 생각보다 많이 쓰이지는 않는다.(실수 일어날 가능성이 높음)

# sensors = {"모터온도": 78, "진동": 0.5}
# new_data = {"모터온도": 80, "유량": 42}
# sensors.update(new_data)
# print(sensors)

# zip으로 두 리스트를 딕셔너리로 만들기
# dict( zip( 이름, 값 ) )

# names = ["모터온도", "진동", "압력"]
# values = [78, 0.5, 95]
# # zip 기능으로 두 배열을 사용해 묶고 dict 타입 딕셔너리로 만들기
# # 주의할 점 : 두 리스트의 길이가 동일해야 제대로 짝이 지어짐
# # -> 적은 쪽으로 맞춰진다. 따라서, 길이를 맞추는 것이 중요하다.
# sensors = dict(zip(names, values))
# print(sensors)

# 딕셔너리 안에 리스트·튜플 담기
# 딕셔너리 값에 리스트나 튜플을 넣어 센서 하나에 여러 값 저장.

# idols = {
#     "BTS": ["진", "정국", "제이홉", "슈가", "뷔", "지민"],
#     "블랭핑크": ["지수", "리사", "제니", "로제"],
#     "뉴진스": ["민지", "하니", "다니엘", "해린", "혜인"],
# }

# sensors = {"모터온도": [78, 79, 80]}
# temps = sensors["모터온도"]  # 모터온도라는 key의 value 저장
# print(sum(temps) / len(temps))  # value의 평균 구하는 식
# print(max(temps))  # value에서 가장 큰 값

# # 딕셔너리 안에 value로 딕셔너리를 사용하기
# kbo = [
#     {
#         "구단명": "삼성",
#         "마스코트": "라이온스",
#         "구장": {"1구장": "대구라이온스파크", "2구장": "포항야구장"},
#     },
#     {
#         "구단명": "두산",
#         "마스코트": "베어스",
#         "구장": {"1구장": "잠실야구장", "2구장": "베어스파크"},
#     },
# ]

# # 쉽게 리스트 안에 딕셔너리 안에 딕셔너리 접근하기

# print(kbo[0]["구장"]["1구장"])  # 접근하기
# print(kbo[0]["구장"]["2구장"])

# # 딕셔너리 안에 딕셔너리 접근하기

# plant = {
#     "1번모터": {"온도": 78, "상태": "정상"},
#     "2번펌프": {"압력": 95, "상태": "경고"},
# }
# print(plant["2번펌프"]["압력"])
