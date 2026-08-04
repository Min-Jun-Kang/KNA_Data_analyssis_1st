# # 실습 1 / 답안
# def start_CheckLog():
#     print("점검을 시작합니다.")

# start_CheckLog()
# start_CheckLog()


# 실습 2 /  다중 매개변수로 센서값 계산하기
# ① def 괄호 안에 매개변수 두 개를 쉼표로 정의
def report_one(name, temp):
    # ② 함수 안에서 두 매개변수를 함께 활용
    print(f"{name} {temp}도")


# ③ 인자 두 개를 순서대로 전달해 호출
report_one("펌프A", 78)
# ④ 인자 순서를 바꾸면 결과가 어떻게 달라지는지 확인
report_one(78, "펌프A")

# 실습 3 / 키워드 인자로 함수 호출하기


# ① 매개변수 두 개를 가진 함수를 정의
def report_two(name, temp):
    print(f"{name} {temp}")


# ② 호출할 때 매개변수 이름을 지정해 값을 전달
report_two(name="펌프A", temp=78)
# ③ 키워드로 전달하면 순서를 바꿔도 같은 결과인지 확인
report_two(temp=89, name="펌프B")
# ④ 위치 인자와 키워드 인자를 섞을 때는 위치가 먼저임을 확인
report_two("펌프A", temp=78)
# report_two(temp=78, "펌프A") # SyntaxError: positional argument follows keyword argument

# 실습 4 / 반환값으로 간단 계산기 만들기


# ① 값을 받아 계산하는 함수를 정의
def compute_one(num1, num2):
    # ② 계산 결과를 print가 아니라 return으로 돌려주기
    return num1 + num2


# ③ 호출 결과를 변수에 담기
sum = compute_one(3, 4)
# ④ 담은 값을 다음 계산·출력에 이어 쓰기
print(sum)
print(sum + 10)

# 실습 5 / 센서 통계 함수 만들기


# ① 센서값 목록을 매개변수로 받는 함수를 정의
def report_three(value):

    # ② min·max·합÷개수로 최소·최대·평균을 계산
    # ③ 세 값을 쉼표로 함께 return
    return min(value), max(value), round(sum(value) / len(value), 1)


# ④ 돌려받은 값을 세 변수로 언패킹해 출력
min_val, max_val, avg_val = report_three([80, 90, 100])
print(f"최소값: {min_val}, 최대값: {max_val}, 평균: {avg_val}")


# 실습 6 / 처리 흐름 만들기


# ① 값을 받아 계산해 return하는 함수를 정의
def comute_two(value):
    return round(sum(value) / len(value), 2)  # 평균 구하는 함수


# ② 계산 결과를 받아 판정해 출력하는 함수를 정의
def over_avg(avg):
    if avg > 90:
        return "위험"
    return "정상"


# ③ 첫 함수의 반환값을 변수에 담아 둘째 함수에 전달
result = comute_two([80, 100, 110])
num_status = over_avg(result)
# ④ 실행해 입력-처리-출력 흐름이 이어지는지 확인
print(f"평균 {result} -> {num_status}")  # 85.0 -> 정상

# 실습 7 / 센서 분석 함수 세트 만들기


# ① 센서값 목록을 받아 평균을 return하는 함수를 정의
def comute_three(value):
    return round(sum(value) / len(value), 2)


# ② 평균과 기준값(기본값 있음)을 받아 상태를 판정해 return하는 함수를 정의
def avg_status(avg, limit=80):
    if avg > limit:
        return "위험"
    return "정상"


# ③ 두 함수를 순서대로 연결해 목록에서 상태까지 구하기
sensor_avg = comute_three([80, 90, 100])
sensor_status = avg_status(sensor_avg)

# ④ 실행해 흐름과 결과를 확인
print(f"{sensor_avg} {sensor_status}")
