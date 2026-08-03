# 실습 1번

# (설비명, 온도, 진동)

# 판정 기준
#   온도 > 90 또는 진동 > 5.0  > "위험"
#   온도 >= 80 또는 진동 >= 3.0 > "주의"
#   그 외                      > "정상"

# TODO 1. 각 설비 상태 판정해서 번호 붙여 한 줄씩 출력 (for + enumerate + if/elif/else)


# TODO 2. 정상 / 주의 / 위험 각각 몇 대인지 세서 출력 (누적변수)


# TODO 3. 이상 설비(주의 + 위험) 비율 % 출력 (round)


# TODO 4. 전체 평균 온도 출력 (round)


# TODO 5. 온도 가장 높은 설비 이름 + 온도 출력 (반복문으로 직접 찾기)


# TODO 6. "위험" 설비 이름만 모아서 정렬해 리스트로 출력 (.append() + .sort())


# 도전) 위험 1대라도 있으면 "⚠ 즉시 점검 요망", 없으면 "✅ 전 설비 안정"

# ========================================
#         설비 종합 모니터링 리포트
# ========================================
# 1. 컨베이어_01 | 온도 78℃ | 진동 2.1mm/s | 정상 ✅
# 2. 용접기_02 | 온도 92℃ | 진동 5.4mm/s | 위험 🚨
# ...
# ----------------------------------------
# 총 설비: 7대
# 정상: 2 / 주의: 3 / 위험: 2
# 이상 설비 비율: 71.4%
# 평균 온도: 85.9℃
# 최고 온도 설비: 건조로_04 (101℃)
# 위험 설비 목록: ['건조로_04', '용접기_02']
# ========================================

sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]
danger = 0
caution = 0
normal = 0
i = 0
total_temp = 0
danger_list = []
highest_temp = 0


print("========================================")
print("\t설비 종합 모니터링 리포트\t")
print("========================================")
for name, temp, vibe in sensors:
    i += 1
    if temp > highest_temp:
        highest_temp = temp
        highest_name = name
    if temp > 90 or vibe > 5.0:
        print(f"{i}. {name} | 온도 {temp}℃ | 진동 {vibe}mm/s | 위험 🚨")
        danger_list.append(name)
        danger += 1
        total_temp += temp
    elif temp >= 80 or vibe >= 3.0:
        print(f"{i}. {name} | 온도 {temp}℃ | 진동 {vibe}mm/s | 주의 ⚠️")
        caution += 1
        total_temp += temp
    else:
        print(f"{i}. {name} | 온도 {temp}℃ | 진동 {vibe}mm/s | 정상 ✅")
        normal += 1
        total_temp += temp
print("----------------------------------------")
print(f"총 설비 : {len(sensors)}")
print(f"정상: {normal} / 주의: {caution} / 위험: {danger}")
print(f"이상 설비 비율: {round((danger+caution)/len(sensors)*100, 1)}%")
print(f"평균 온도: {round(total_temp/len(sensors), 1)}℃")
print(f"최고 온도 설비: {highest_name} ({highest_temp})℃")
print(f"위험 설비 목록: {sorted(danger_list)}")
print("========================================")
