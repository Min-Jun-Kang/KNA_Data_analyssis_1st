# # 실습 / range로 숫자 흐름 출력하기

# num = int(input("숫자를 입력해주세요 > "))

# for i in range(1, num + 1):
#     print(i, end=" ")
# print()

# for i in range(2, num + 1, 2):
#     print(i, end=" ")
# print()

# for i in range(num, 0, -1):
#     print(i, end=" ")

# # 3의 배수 출력하기
# # 사용자에게 범위를 입력받아 3의 배수 출력하기

# num = int(input("숫자를 입력해주세요 > "))

# for i in range(1, num + 1):
#     if i % 3 == 0:
#         print(i, end=" ")

# 369 게임
# 숫자에 3이나 6이나 9가 있으면 당첨, 문자열

num = input("숫자를 입력하세요 > ")
count = 0

for i in range(1, int(num) + 1):
    if str(i).find("3") != -1 or str(i).find("6") != -1 or str(i).find("9") != -1:
        count = str(i).count("3") + str(i).count("6") + str(i).count("9")
        print("👏" * count, end=" ")
        count = 0
    else:
        print(i, end=" ")
    if i % 10 == 0:
        print()
