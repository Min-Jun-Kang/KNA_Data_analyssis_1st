# # 실습 1 : 이름 입력받아 인사 출력

# name = input("이름: ")
# print("안녕하세요 " + name + "님!")


# # 실습 2 : 숫자 입력받아 계산하기

# year = int(input("태어난 해를 입력하세요 > "))
# age = 2026 - year
# print("당신의 나이는 " + str(age + 1) + "살 입니다.")

# # 실습 3 여러 개의 값 입력받기
# country = input("거주하는 국가를 입력하세요 > ")
# city = input("거주하는 도시를 입력하세요 > ")

# print(country + "의 " + city + "에서 거주하시는 군요!")

# # 실습 4 두 수 입력받아 사칙연산

# num1 = int(input("첫 번째 수를 입력하세요 > "))
# num2 = int(input("두 번째 수를 입력하세요 > "))

# print("두 수의 합은", str(num1 + num2) + "입니다.")
# print("두 수의 차는", str(num1 - num2) + "입니다.")
# print("두 수의 곱은", str(num1 * num2) + "입니다.")
# print("두 수의 나눗셈은", str(num1 / num2) + "입니다.")

# # 실습 5 온도를 받아 기준 비교

# temp = float(input("온도를 입력하세요 > "))

# print("온도가 80℃ 초과하나요?", temp > 80)
# print("온도가 0℃ 이상인가요?", temp >= 0)

# # 실습 6 세 점수 받아 평균 구하고 기준(60점) 비교

# score_1 = int(input("첫 번째 점수를 입력하세요 > "))
# score_2 = int(input("두 번째 점수를 입력하세요 > "))
# score_3 = int(input("세 번째 점수를 입력하세요 > "))

# score_avg = round((score_1 + score_2 + score_3) / 3, 2)
# score_stand = 60

# print("세 점수의 평균은 " + str(score_avg) + "점 입니다.")
# print("기준 60점을 넘었나요?", score_avg > score_stand)
