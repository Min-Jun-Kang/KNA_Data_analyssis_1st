# # if문 실습
# # 사용자에게 나이를 입력받아 성인인지 출력하는 조건문 작성

# age = int(input("나이를 입력하세요 > "))

# if age > 19:
#     print("성인입니다.")
# else:
#     print("미성년자입니다.")

# # if문 실습2
# # 숫자 맞추기 게임
# # 정답은 임의로 지정
# # 정답을 맞추면 맞았습니다, 틀리면 틀렸습니다 출력
# # 마지막에 무조건 게임이 종료되었습니다 출력

# answer = 20  # 정답 숫자 정하기

# say = int(input("숫자를 입력해주세요 > "))  # 숫자 입력받기

# if say == answer:  # 입력 받은 숫자랑 정답이 같은 경우
#     print("맞았습니다.")
# else:  # 숫자랑 정답이 다른 경우
#     print("틀렸습니다.")
# print("게임이 종료되었습니다.")  # 항상 출력되야 하는 문

# 신호등 색을 입력받아서
# "초록색"이라면 "건너세요" 출력
# "빨간색"이라면 "기다리세요" 출력
# 입력값이 초록색이나 빨간색이어야만 정상 작동
# 이상한 값 입력 시 "다시 입력하세요"

# color = input("색을 입력해주세요 > ")
# if color == "초록색" or color == "빨간색":
#     if color == "초록색":
#         print("건너세요")
#     else:
#         print("기다리세요")
# else:
#     print("다시 입력하세요")


# # 실습 / 설비 온도 상태 판정하기

# temp = int(input("온도를 입력하세요 > "))

# if temp > 80:
#     print("위험")
# elif temp > 60:
#     print("주의")
# else:
#     print("정상")

# # 실습 / 두 조건을 모두 만족하는 검증

# user_ID = "admin"
# user_PW = "1234"

# input_ID = input("아이디를 입력하세요 > ")
# input_PW = input("비밀번호를 입력하세요 > ")

# if input_ID == user_ID and input_PW == user_PW:
#     print("로그인 성공!")
# else:
#     print("로그인 실패")

# # 실습 / 세 값으로 설비 종합 상태 판정하기

# temp = int(input("온도를 입력하세요 > "))
# vibe = float(input("진동을 입력하세요 > "))
# volt = int(input("전류를 입력하세요 > "))

# if temp > 80 or vibe > 4.0:
#     print("위험 : 즉시 정지!")
# elif volt > 60 and temp > 70:
#     print("주의 : 부하 점검")
# elif vibe > 2.5:
#     print("주의 : 진동 관찰")
# else:
#     print("정상")
