# =====================================================================
# 종합 실습 3. 교대조 센서 경고 로그 분석
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

# === 교대조 센서 경고 로그 분석 ===
# 오전조 고유 센서 4종: ['TZ_11', 'TZ_13', 'TZ_15', 'TZ_17']
# 오후조 고유 센서 4종: ['TZ_13', 'TZ_15', 'TZ_19', 'TZ_21']
# ----------------------------------------
# 양 교대조 공통 경고 센서: ['TZ_13', 'TZ_15']
# 오전조 전용: ['TZ_11', 'TZ_17']
# 오후조 전용: ['TZ_19', 'TZ_21']
# 전체 경고 센서 6종: ['TZ_11', 'TZ_13', 'TZ_15', 'TZ_17', 'TZ_19', 'TZ_21']
# ----------------------------------------
# 경고 발생 횟수 순위:
#   1위: TZ_13 - 5회
#   2위: TZ_15 - 4회
#   3위: TZ_11 - 4회
#   ...
# ----------------------------------------
# 최다 경고 센서: TZ_13 (5회) → 우선 점검 필요

print("=== 교대조 센서 경고 로그 분석 ===")

morning = ["TZ_11", "TZ_13", "TZ_11", "TZ_15", "TZ_13", "TZ_11", "TZ_11", "TZ_17"]
afternoon = ["TZ_13", "TZ_15", "TZ_13", "TZ_19", "TZ_15", "TZ_21", "TZ_13", "TZ_15"]

# TODO 1. 오전조 / 오후조 각각 고유 센서 종류 수 + 정렬된 목록 출력
#         (set 으로 중복 제거 > sorted 로 정렬)
morning_set = set(morning)
afternoon_set = set(afternoon)
sorted_morning_set = sorted(morning_set)
sorted_afternoon_set = sorted(afternoon_set)
print(f"오전조 고유 센서 4종: {sorted_morning_set}")
print(f"오후조 고유 센서 4종: {sorted_afternoon_set}")

# TODO 2. 교집합 (두 조 모두에서 경고 난 센서) 정렬해서 출력  ( & )
print("----------------------------------------")
inter_set = morning_set.intersection(afternoon_set)
sorted_inter_set = sorted(inter_set)
print(f"양 교대조 공통 경고 센서: {sorted_inter_set}")
# TODO 3. 차집합 (오전 전용 / 오후 전용) 각각 정렬해서 출력  ( - )
#         방향에 따라 결과 다른 것 유의
only_morning = sorted(morning_set.difference(afternoon_set))
only_afternoon = sorted(afternoon_set.difference(morning_set))

print(f"오전조 전용: {only_morning}")
print(f"오후조 전용: {only_afternoon}")
# TODO 4. 합집합 (전체 경고 센서) 종류 수 + 정렬된 목록 출력  ( | )
union_list = sorted(morning_set.union(afternoon_set))

print(f"전체 경고 센서 6종: {union_list}")
print("----------------------------------------")
# TODO 5. 센서마다 (오전 횟수 + 오후 횟수) 구해서
#         (횟수, 센서명) 튜플 리스트 만들고 횟수 많은 순 정렬
#         "N위: 센서명 - X회" 형태로 출력
#         힌트) morning.count("TZ_13") / sorted(리스트, reverse=True)

total_list = []
total_tuple = ()
for i in range(len(union_list)):
    total_tuple = (
        morning.count(union_list[i]) + afternoon.count(union_list[i]),
        union_list[i],
    )
    total_list.append(total_tuple)
total_list.sort(reverse=True)
print(total_list)
print("경고 발생 횟수 순위:")
for idx, value in enumerate(total_list):
    print(f" {idx+1}위: {value[1]} - {value[0]}회")

print("----------------------------------------")
# TODO 6. 가장 경고 많았던 센서 콕 집어서 "우선 점검 필요" 출력
print(f"최다 경고 센서: {total_list[0][1]} ({total_list[0][0]}회) → 우선 점검 필요")

# 도전) 총 3회 이상인 센서만 "집중 관리 대상" 리스트로 만들어 정렬 출력
manage_list = []
for idx, value in enumerate(total_list):
    if value[0] >= 3:
        manage_list.append(value[1])
manage_list.sort()

print(f"집중 관리 대상: {manage_list}")
