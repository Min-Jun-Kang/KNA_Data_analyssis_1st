# # 산술 연산자
# # +(더하기) -(빼기) /(나누기) *(곱하기) //(몫) %(나머지) **(제곱)

# print(3 + 5)  # 8
# print(10 - 4)  # 6
# print(4 * 5)  # 20
# print(20 / 4)  # 5.0 > 나눗셈 결과는 항상 float
# print(7 // 2)  # 3
# print(7 % 3)  # 1
# print(2**4)  # 16

# # =====================
# # 연산 우선순위
# # ** > *, /, //, & > +, -

# print(2 + 8 * 3)  # 26
# print((2 + 8) * 3)  # 30

# # =====================
# # 복합연산자

# result = 3 * 5
# print(result)  # 15

# # += : 기존 값에서 오른쪽 값을 더한 뒤 재할당
# # -= : 기존 값에서 오른쪽 값을 뺀 뒤 재할당
# # *= : 기존 값에서 오른쪽 값을 곱한 뒤 재할당
# # /= : 기존 값에서 오른쪽 값을 나눈 뒤 재할당

# result += 10  # 25
# result -= 5  # 20
# result *= 3  # 60
# result /= 2  # 30.0

# # ======================
# # 문자열 연산
# print("안녕" + "하세요")  # 안녕하세요

# print("안녕 " + "하세요")  # 안녕 하세요
# print("안녕" + " " + "하세요")  # 안녕 하세요
# print("안녕", "하세요")  # 안녕 하세요

# # 문자열 곱하기
# print("안녕" * 5)  # 안녕안녕안녕안녕안녕

# # 문자열에 연산자를 사용할 경우 모두 이어져서 나옴


# # =================================

# print("=== 비교 연산자 ===")

# # < 미만 > 초과 <= 이하 >= 이상 == 같다 != 다르다
# # 비교 결과는 무조건 True or Fasle

# print(7 < 16)  # True
# print(7 > 16)  # False
# print(7 <= 7)  # True
# print(7 >= 7)  # True
# print(7 == 7)  # True
# print(7 != 7)  # False

# # 비교연산자는 문자열 비교도 가능
# print("hello" == "hello")  # True
# print("정상" == "정상")  # True

# # 비교연산자를 사용해 문자열을 비교할 때 주의사항

# # 1. 대소문자 구분
# print("hello" == "Hello")  # False

# # 2. 공백이 있어도 다르다고 판단
# print("정상" == "정상 ")  # False

# # 부정연산자 != (not)
# # 두 값이 동일한데 !로 인해서 값이 반대로 출력됨
# print("hello" != "hello")  # False
# print("hello" != "hello ")  # True
# print("hello" != "Hello")  # True

# # 변수에 문자열을 할당하고, 변수로 문자열 비교
# hello = "hi"
# print(hello == "hi")  # True

# # 위 비교에서 hello는 따옴표로 감싸지지 않아서 "변수"로 취급
# # 만약 hello를 "hello"와 같이 따옴표로 감싸면
# # string(문자열)로 인식해서 변수 취급을 하지 않음
# # ex) : "hello"와 "hi"를 비교하는 것

# 변수로 비교연산자 사용
num1 = 123
num2 = 456

print(num1 > num2)  # False
print(num1 > "num2")
# TypeError: '>' not supported between instances of 'int' and 'str'
# int랑 str은 비교연산자로 비교 불가
