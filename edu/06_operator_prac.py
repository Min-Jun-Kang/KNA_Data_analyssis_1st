# # 실습 1번

# a = 17
# b = 5

# print(a + b, a - b, a * b, a / b, a // b, a % b, a**b)


# # 실습 2번

# score_1 = 95
# score_2 = 80
# score_3 = 88

# print("평균:", round((score_1 + score_2 + score_3) / 3, 2))

# length = 8  # 정사각형 한 변의 길이
# print("정사각형 넓이:", length**2)

# width = 7  # 가로
# length = 6  # 세로
# height = 8  # 높이
# print("직육면체의 부피:", width * length * height)

# # 실습 3

# num1 = 10
# num2 = 20

# print(num1 == num2)  # False
# print(num1 != num2)  # True
# print(num1 > num2)  # False
# print(num1 < num2)  # True
# print(num1 >= num2)  # False
# print(num1 <= num2)  # True

# str1 = "hi"
# str2 = "hello"

# print(str1 == str2)
# print(str1 != str2)
# print(str1 > str2)
# print(str1 < str2)
# print(str1 >= str2)
# print(str1 <= str2)

# 문자열 비교는 빠른 순서
# 즉, 위에서는 알파벳 순서로 비교해서 i가 e보다 뒷 순서이기 때문에 str1이 크다고 나온다

# # 실습 4

# temp = 85
# pres = 5

# temp_ok = temp >= 60 and temp <= 90
# pres_ok = pres >= 3 and pres <= 7

# print("온도 정상:", temp_ok)
# print("압력 정상:", pres_ok)
# print("모두 정상:", temp_ok and pres_ok)

# # 실습 5 복합 할당으로 재고 추적 기초

# stock = 100
# print("재고량:", stock)
# stock += 50  # 입고
# print("재고량:", stock)
# stock -= 30  # 출고
# print("재고량:", stock)
# stock += 5  # 반품
# print("재고량:", stock)

# # 실습 6 설비 지표 계산

# total = 500
# error = 23

# print("불량률:", error / total * 100, "%")

# total_time = 24
# action_time = 21

# print("가동률:", action_time / total_time * 100, "%")

# 실습 7 총 가동분을 시:분으로 표현

action_time = 500

print("가동 시간(시:분):", 500 // 60, "시", 500 % 60, "분")
print("가동 시간(시:분):", str(500 // 60) + "시", str(500 % 60) + "분")
