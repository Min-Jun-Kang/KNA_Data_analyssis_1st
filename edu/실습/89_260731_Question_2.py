# =====================================================================
# 종합 실습 2. 실시간 측정값 입력 시스템
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

# === 실시간 측정값 입력 시스템 ===
# 측정값을 입력하세요. 종료하려면 q 입력.
# 측정값: 85
# 측정값: 120
#   🚨 임계값(100) 초과! 현재까지 초과 1회
# 측정값: 60
# 측정값: q
# ----------------------------------------
# 총 입력 개수: 3개
# 최댓값: 120.0 / 최솟값: 60.0
# 평균값: 88.33
# 임계값 초과 개수: 1개
# 평균 초과 개수: 1개
# 상위 3개 값: [120.0, 85.0, 60.0]

# 이 실습은 사용자한테 입력받는 거라 미리 주는 데이터 없음
# while로 계속 입력받다가 q 입력하면 종료 > 통계 출력

print("=== 실시간 측정값 입력 시스템 ===")

LIMIT = 100  # 임계값 (100 초과 시 즉시 경고)
empty_list = []
LIMIT_TIME = 0
total = 0
big_avg = 0
big_list = []
# TODO 1. while로 "측정값: " 계속 입력받기, q면 break
#         (입력값은 숫자 아니면 q 라고 가정)
#         값은 리스트에 .append() 로 모으기
while True:
    user_input = input("측정값: ")
    if user_input == "q":
        break
    # 도전) q 대신 그냥 Enter(빈 입력 "") 치면 무시하고 다시 받기
    elif user_input == "":
        continue
    else:
        empty_list.append(float(user_input))

    # TODO 2. 입력값이 LIMIT 초과하면 즉시 경고 + 지금까지 초과 횟수 출력
    if int(user_input) > LIMIT:
        LIMIT_TIME += 1
        print(f" 🚨 임계값(100) 초과! 현재까지 초과 {LIMIT_TIME}회")


# TODO 3. q로 끝난 뒤:
#   - 입력값이 하나도 없으면 "입력된 측정값이 없습니다." 출력하고 끝
#   - 값이 있으면 아래 출력
#       · 총 입력 개수 (len)
#       · 최댓값 / 최솟값 (반복문으로 직접 찾기)
#       · 평균값 (round, 소수 둘째 자리)
#       · 임계값 초과 개수
#       · 평균보다 큰 값의 개수  > 평균 먼저 구한 뒤 리스트 다시 돌기
#       · 상위 3개 값 (.sort(reverse=True) 후 슬라이싱 [:3])
if len(empty_list) == 0:
    print("입력된 측정값이 없습니다.")
else:
    sorted_list = sorted(empty_list, reverse=True)
    # ----------------------------------------
    print("----------------------------------------")
    # 총 입력 개수: 3개
    print(f"총 입력 개수: {len(sorted_list)}개")
    # 최댓값: 120.0 / 최솟값: 60.0
    print(f"최댓값: {sorted_list[0]} / 최솟값: {sorted_list[-1]}")
    # 평균값: 88.33
    for i in range(len(sorted_list)):
        total += sorted_list[i]
    print(f"평균값: {round(total/len(sorted_list), 2)}")
    # 임계값 초과 개수: 1개
    print(f"임계값 초과 개수: {LIMIT_TIME}개")
    # 평균 초과 개수: 1개
    for i in range(len(sorted_list)):
        if sorted_list[i] > round(total / len(sorted_list), 2):
            big_avg += 1
    print(f"평균 초과 개수: {big_avg}개")
    # 상위 3개 값: [120.0, 85.0, 60.0]
    for i in range(3):
        big_list.append(sorted_list[i])
    print(f"상위 3개 값: {big_list}")
