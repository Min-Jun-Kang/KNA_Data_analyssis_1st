# 실습 1 / 딕셔너리 만들고 다루기

# 1) 센서명을 키(key), 측정값을 값(value)로 딕셔너리 저장
sensors_one = {"모터온도": 78, "진동": 0.5}

# 2) 키(key)로 값을 꺼내고 새 키로 추가, 기존 키로 수정
print(sensors_one["모터온도"])  # 값 꺼내기
print(sensors_one.get("진동", 0))  # 값 더 안전하게 꺼내기

sensors_one["압력"] = 95  # 없던 키를 언급하면 추가
sensors_one["진동"] = 0.8  # 기존 키를 언급하면 수정

# 3) get으로 없는 키를 기본값으로 조회, in으로 키 존재 확인
print(sensors_one.get("면적", -1))
print("모터온도" in sensors_one)
print("면적" in sensors_one)

# 실습 2 / update로 여러 값 한 번에 갱신하기

# 1) 센서 딕셔너리와 새 데이터 딕셔너리를 각각 저장
sensors_two = {"모터온도": 78, "진동": 0.5, "압력": 95}
new_datas = {"모터온도": 90, "면적": 100}
# 2) update로 새 데이터를 한 번에 반영(있으면 수정, 없으면 추가)
sensors_two.update(new_datas)
print(f"갱신된 딕셔너리: {sensors_two}")
# 3) del로 특정 키를 삭제하고 len으로 개수 확인
del sensors_two["면적"]
print(f"삭제한 딕셔너리: {sensors_two}, 센서 수: {len(sensors_two)}")

# 실습 3 / 딕셔너리로 통계 내기

# 1) 센서명-측정값 딕셔너리 저장
sensors_three = {"모터온도": 78, "진동": 10, "압력": 95, "면적": 100}
# 2) values의 합을 개수로 나눠 평균 구하기
print(f"값의 평균 구하기 : {sum(sensors_three.values())/len(sensors_three)}")
# 3) items로 순회하며 가장 큰 값과 그 센서명을 찾아 출력
max_value = 0
max_key = ""
for name, value in sensors_three.items():
    if max_value < value:
        max_value = value
        max_key = name
print(f"value의 최댓값: {max_value}, 센서명: {max_key}")

# 실습 4 /  zip으로 센서명-값 매핑하기

# 1) 센서명 리스트와 측정값 리스트를 각각 저장
# zip할 리스트 요소의 개수는 동일하게
sensor_name = ["모터온도", "진동", "압력", "면적"]
sensor_value = [78, 20, 90, 80]
# 2) zip으로 두 리스트를 짝지어 dict로 변환
sensors_four = dict(zip(sensor_name, sensor_value))
# 3) items로 순회하며 이름-값 쌍 출력
for name, value in sensors_four.items():
    print(f"이름 : {name}, 값 : {value}")

# 실습 5 / 임계값으로 경고 센서 분류하기
# 1) 측정값 딕셔너리와 임계값 딕셔너리를 각각 저장
data_value = {"모터온도": 87, "진동": 20, "압력": 90, "면적": 100}
limit_value = {"모터온도": 80, "진동": 30, "압력": 100, "면적": 90}
over_sensor = []
# 2) items로 순회하며 각 센서 값이 같은 이름의 임계값을 넘는지 비교
for name, value in data_value.items():
    if value > limit_value.get(name, 0):
        # 3) 넘는 센서 이름을 빈 리스트에 모아 출력
        over_sensor.append(name)
print(f"임계값 초과 센서 : {over_sensor}")

# 실습 6 / 중첩 딕셔너리로 설비 관리하기

# 1) 설비명을 키로, 각 설비 정보(딕셔너리)를 값으로 하는 중첩 딕셔너리 저장
sensor_six = {
    "1번설비": {"모터온도": 80, "상태": "경고"},
    "2번설비": {"모터온도": 70, "상태": "정상"},
    "3번설비": {"모터온도": 90, "상태": "정상"},
    "4번설비": {"모터온도": 100, "상태": "경고"},
    "5번설비": {"모터온도": 60, "상태": "경고"},
}
# 2) 중첩 키로 특정 설비의 특정 값을 꺼내기
print(f"1번설비의 모터온도 : {sensor_six['1번설비']["모터온도"]}")
# 3) items 순회로 상태가 "경고"인 설비만 찾아 출력
for name, dic in sensor_six.items():
    for key, value in dic.items():
        if value == "경고":
            print(f"{name} 점검필요")

# 실습 7 / 표 데이터를 딕셔너리로 변환하기

# 1) 한 줄에 "센서명,측정값" 형태인 행 문자열들을 리스트로 저장
sensor_seven = ["모터온도,80", "진동,10", "압력,30"]
# 2) for로 각 행을 쉼표로 split해 이름과 값으로 나누기
new_dict = {}
for i in sensor_seven:
    name = i.split(",")
    # 3) 이름을 키, 값을 숫자로 바꿔 딕셔너리에 추가
    new_dict[name[0]] = int(name[1])
print(f"새 딕셔너리 : {new_dict}")

# 실습 8 / 센서 데이터 통합 정리

# 1) 센서 측정값 딕셔너리와 임계값 딕셔너리 저장
sensor_eight = {"온도": 90, "진동": 20, "압력": 80}
limit_eight = {"온도": 80, "진동": 30, "압력": 70}
new_set = set()

# 2) values로 전체 평균 구하기
print(f"센서의 평균 : {round(sum(sensor_eight.values())/len(sensor_eight), 2)}")

# 3) items 순회로 임계값 초과 센서를 셋에 모으기
for name, value in sensor_eight.items():
    if value > limit_eight[name]:
        new_set.add(name)

# 4) 셋을 정렬해 출력
sorted_set = sorted(new_set)
print(f"정렬한 set : {sorted_set}")
