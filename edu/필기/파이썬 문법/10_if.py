# 조건문 - if
# 항상 실행되지 않고 조건에 따라서
# 실행되는 코드가 달랐으면 할 때 사용
# 코드의 분기라고도 표현
# 조건문의 조건은 True와 False로 결과가 나와야 한다

# if 조건식:
#   실행할 코드 (한 칸 들여쓰기(\t))

# if문의 :은 그 다음 올 코드가 if문 조건식의 결과가 True 일때만 실행하라는 의미
# 즉, 여기서부터 이 조건에 속한다는 신호
# 조건에 속하는 코드는 모두 들여쓰기가 적용되어있어야 함

# temp = 89

# if temp > 80:
#     print("temp 변수의 값이 80보다 크다!!")
#     print("👍")
# print("이건 항상 실행되는 코드")

# temp = 77

# if temp > 80:
#     print("temp 변수의 값이 80보다 크다!!")
#     print("👍")
# print("이건 항상 실행되는 코드")

# temp 변수의 값이 80보다 크다면 "경고" 출력
# temp 변수의 값이 80이하라면 "정상" 출력
# 동시에 하고 싶은 경우

# temp = int(input("온도를 입력하세요 > "))

# if temp > 80:
#     print("경고")
# else:
#     print("정상")

# # if문의 조건이 False 일때 else 블럭이 실행된다.
# # 즉, 2개의 블럭이 동시에 실행될 수는 없다.

# # 사람 체온 정상 범위 : 36.2 ~ 36.9

# user = float(input("온도를 입력해주세요 > "))

# if user >= 36.2 and user <= 36.9:
#     print("당신은 정상체온입니다.")
# else:
#     if user > 36.9:
#         print("당신은 열이 납니다.")
#     else:
#         print("당신은 저체온입니다.")
# print("체온 판단 완료")

# # 위의 체온 판단 if문을 안에서 열나는지 저체온인지 판단하도록 수정

# if user > 36.9 or user < 36.2:
#     if user > 36.9:
#         print("당신은 열이 납니다.")
#     else:
#         print("당신은 저체온입니다.")
# else:
#     print("당신은 정상체온입니다.")
# print("체온 판단 완료")

# elif
# else와 if만으로 분기하기에는 불편하고
# if 중첩이 너무 많아져서 생김

# user = float(input("온도를 입력해주세요 > "))

# if user <= 36.2:
#     print("저체온증입니다.")
# elif user >= 36.9 and user < 37.8:
#     print("당신은 미열입니다. 주의하세요")
# elif user >= 37.8:
#     print("당신은 고열입니다. 병원가세요")
# else:
#     print("당신은 정상입니다.")

# # elif 순서
# # elif 순서 주의
# # 코드는 위에서 부터 진행되기 때문에 순서를 잘 지키지 않으면 원하는 값이 안 나올수도 있다.
# # 가장 작은 범위부터 위에서부터 적는 것이 좋다.

# score = 70

# if score >= 90:
#     print("우수")
# elif score >= 50:
#     print("미흡")
# elif score >= 70:
#     print("보통")
# else:
#     print("비상")


# # not 연산자
# # 괄호로 감싸서 사용
# if not (3 == 5):
#     print("출력됩니다.")
# # 3과 5는 같지 않으니 False가 되지만
# # 앞에 not이 있어서 False를 True로 뒤집어 if가 인식
