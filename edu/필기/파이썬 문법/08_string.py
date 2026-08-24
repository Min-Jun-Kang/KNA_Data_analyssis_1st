# 여러 줄 문자열 > """ """

# notice = """설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검"""

# print(notice)

# notice = """
# 설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검
# """

# print(notice)
# # 코딩 중 보기 편한 방식으로 작성하면 생각과 다른 결과물이 나옴
# # """ """ (삼중 따옴표 사용할 시 그 내부의 모든 줄바꿈이 다 반영되어 출력된다.)

# \n : 줄바꿈, \t : 탭(간격), \\ : "\" 출력하고 싶을 때
# notice = "설비 점검 안내\n1. 전원 확인\n2. 센서 점검"
# print(notice)

# tap = "이름\t상태"
# print(tap)
# print("이름    상태")
# \t는 공백 4번이랑 같다.

# backslash = "이름\\상태"
# print(backslash)  # 이름\상태
# # 첫 번째 \는 이스케이프 문자라는 것을 알리는 용도

# str = "It's me"
# print("\"이름\", '나이'")
# # \", \'을 이용해서 따옴표 표현 가능

# 빈 문자열 vs 공백 문자열
# 빈 문자열("") : 글자가 0개, 길이 0
# 공백 문자열(" ") : 글자가 공백수 만큼, 길이도 공백 수 만큼

# print("" == " ")  # False
# 빈 문자열과 공백 문자열은 컴퓨터에게 다른 값으로 인식됨
# print(len(""))  # 0
# print(len(" "))  # 1


# ================================================

# 인덱싱(indexing) : 위치 번호로 글자를 하나씩 꺼내기
# 문자열[인덱스 번호]
# 문자열의 첫 글자 인덱스 번호는 0이다. > 0부터 시작한다.
# 문자열 첫글자 = word[0]

# word = "Python"
# print(word[0], word[3], word[5])

# abc = "abcdefghijklmnopqrstuvwxyz"
# # 내 이름 출력하기 (성 빼고)
# print(abc[12] + abc[8] + abc[13] + abc[9] + abc[20] + abc[13])
# print(abc[-14] + abc[-18] + abc[-13] + abc[-17] + abc[-6] + abc[-13])

# 음수 인덱스는 뒤에서부터 역순으로 순서 숫자가 붙음
# 주의사항 > 음수 인덱스는 마지막 인덱스가 -1
# IndexError > 문자열 길이보다 큰 index를 호출해서

# 슬라이싱 > 여러 글자를 구간으로 잘라내기
# ex) word[1:4] > 1,2,3번 자리 (시작 포함, 끝 제외)

# ==========================

# 슬라이싱 - 구간으로 잘라내기
# 문자열[시작:끝]
# 시작 인덱스 글자는 포함해서 출력
# 끝 인덱스 글자는 제외하고 출력

# word = "Python"
# print(word[3:5])  # ho
# print(word[3:6])  # hon
# # 슬라이싱은 end가 포함되지 않고 출력하기 때문에 없는 인덱스인 6도 사용할 수 있음

# print(word[6])  # indexing은 정확하게 마지막 index까지만 쓸수 있고 넘어가면 error

# 생략 기능
# word = "Python"
# start 생략 > 0부터 출력 > ex) word[:3] == word[0:3]
# end 생략 > 끝까지 출력 > ex) word[3:] == word[3:6]

# word = "Python"
# print(word[:4] + " 비교 " + word[0:4])
# print(word[3:] + " 비교 " + word[3 : len(word)])
# # index 끝 번호는 결국 문자열의 길이와 같다.

# # 슬라이싱 - 전체 생략
# print(word[:])  # print(word[0:6])과 동일, 전체 문자열 출력

# # 슬라이싱 - 음수 인덱스 사용
# print(word[-3:])  # hon
# # 음수 인덱스 작성 시 입력한 인덱스 부터 정방향으로 출력함
# print(word[:-1])  # Pytho
# # 처음부터 -1(끝 번호)까지 이므로 마지막 문자는 제외하고 출력된다.
# # 역순 아님 주의
# # 음수 인덱스 사용 시 컴퓨터가 알아서 정수 인덱스 치환해서 동작

# # step으로 건너뛰기
# # 문자열[시작:끝:간격(step)]
# word = "Python"
# print(word[0:6:2])  # Pto > 처음부터 끝까지 2칸씩 건너서 출력됨

# # 순서 뒤집기
# print(word[::-1])  # nohtyP
# # step은 index가 아니고, 음수 입력 시 문자열의 순서를 뒤집음

# # 슬라이싱은 범위를 벗어나도 오류가 발생하지 않음
# print("범위를 벗어난 슬라이싱", word[0:100])  # 슬라이싱은 인덱스 번호와 상관없다

# :(콜론)이 있으면 슬라이싱, 없으면 인덱싱!!

# ========================================

# len() > 문자열의 길이 반환
# len(문자열)

# print(len("Hello World!"))  # 문자열의 길이 출력 > 12, 공백도 길이에 포함
# print(len(""))  # 0
# print(len(" "))  # 1

# var = "여러분~! 한 시간만 더 하면 됩니다! 조금만 더 힘을 내주세요!"
# print(len(var))  # 변수에 담긴 문자열의 길이도 출력 가능

# print(len("이것도") - len("가능할까?"))
# # len()은 int를 반환하기 때문에 연산 가능

# print("var 변수의 길이:", len(var), " / 마지막 인덱스 번호:", len(var) - 1)

# 음수 인덱스를 사용하지 않고 마지막 인덱스 문자를 뽑고 싶을 때

# var = "여러분~! 한 시간만 더 하면 됩니다! 조금만 더 힘을 내주세요!"

# print(var[len(var) - 1])

# in - 포함 확인 여부
# not in - 미포함 확인

# ======================================

# in - 특정 문자가 문자열에 포함되었는지 여부 확인
# "여부"를 확인하기 때문에 True 또는 False (bool)로 결과 반환
# # "찾을문자열" in "문자열"
# print("고장" in "설비 고장 발생")  # True 출력
# print("정상" in "설비 고장 발생")  # False 출력
# print("설비에서 고장" in "설비 고장 발생")  # False 출력
# print("설비에서 고장" in "설비에서 고장이 났습니다.")  # True 출력

# # not in - in의 정반대 동작
# print("고장" not in "설비 고장 발생")  # False 출력
# print("정상" not in "설비 고장 발생")  # True 출력
# print("설비에서 고장" not in "설비 고장 발생")  # True 출력
# print("설비에서 고장" not in "설비에서 고장이 났습니다.")  # False 출력

# print(" " in "설비 고장 발생")  # True 출력
# # 공백도 문자열이기 때문에 in으로 포함 여부 확인 가능하다.

# =================================================

# .count() > 특정 문자열에 특정 글자가 몇 번 나오는지 셀 수 있음
# 문자열 전용 매서드(함수) > 문자열에서만 사용 가능
# int로 반환
# 문자열.count("찾을 글자")
# 없다면 0을 반환

# print("banana".count("a"))  # 3
# print("010-1234-1234".count("-"))  # 2
# print("xxx@xxx.com".count("@"))  # 이메일인지 확인하는 방법 # 1


# =========================

# .find() > 특정 글자가 "처음 나오는 위치"(index 번호)
# .count()처럼 문자열 전용 매서드
# 처음 나오는 위치라 뒤에 또 있어도 알려주지 않음
# int를 반환
# 찾지 못하면 -1를 반환

# email = "hong@company.com"

# at = email.find("@")  # @ 위치의 index인 4가 할당 > int형
# user_id = email[:at]  # @ 앞까지 문자열 출력
# print(user_id)

# # SQE-00Q8이라는 설비의 SQE만 뽑아내기 (find와 슬라이싱 사용)
# sqe = "SQE-00Q8"

# sqe_index = sqe.find("SQE")
# print(sqe_index)  # 0 출력


# sqe_index = sqe.find("-")
# print(sqe_index)  # 3 출력
# sqe_fin = sqe[:sqe_index]  # 0~2 문자열 출력
# print(sqe_fin)

# index() - 위치 찾기
# 사용법은 find와 동일, 없을 때 오류 출력(실행이 멈춘다)

# email = "zhfeps123@naver.com"
# at = email.index("@")  # 9 출력
# print(at)

# print(email[0:at])  # @전 부분 출력
# print(email[at])  # @전 부분 출력, 위와 동일
# print(email[at:])  # @포함되어서 출력
# print(email[at + 1 :])  # @다음부터 출력, 도매인부터 출력

# # SQE-00Q8이라는 설비의 SQE만 뽑아내기 (index 사용)
# sqe = "SQE-00Q8"

# sqe_index = sqe.index("-")
# print(sqe_index)  # 3 출력
# sqe_sli = sqe[:sqe_index]  # 0~2 문자열 출력
# print(sqe_sli)
# # index 사용 시 오류가 나면 해당 문자가 문자열에 없다.

# startswith() - 시작 확인
# 특정 문자열로 시작하는지 검사
# True랑 False로 반환 -> boolean 타입

# # EQP로 시작하는지 검사
# print("EQP-001".startswith("EQP"))  # True
# print("SQP-001".startswith("EQP"))  # False

# # 변수 활용해서 검사
# eqp = "EQP"
# print("EQP-001".startswith(eqp))  # True
# print("SQP-001".startswith(eqp))  # False


# # # endswith() - 끝 확인
# # # 특정 문자열로 끝나는지 검사
# # # True랑 False로 반환 -> boolean 타입

# str2 = "월요일입니다! 여러분은 할 수 있어요!"

# print(str2.endswith("!"))  # True
# print(str2.endswith("!"))  # True
# print(str2.endswith("음"))  # False
# print(str2.endswith("월요일입니다! 여러분은 할 수 있어요!"))  # True
# print(str2.endswith("월요일입니다! 여러분은 할 수 있어요! "))  # False
# print(str2.endswith(" 월요일입니다! 여러분은 할 수 있어요!"))  # False
# print(str2.endswith("월요일입니다!\t 여러분은 할 수 있어요!"))  # False

# # 완전히 같아야만 True를 출력한다.


# .으로 연결하면 "매서드", 문자열이나 int, float처럼 특정 자료형(객체) 내부에 포함된 기능
# () -> 함수, 개발자가 직접 선언하지 않았다면 기본으로 제공되는 함수 "내장 함수"

# upper() -> 단어를 대문자로 다 바꾸는 매소드

# alp = "abcdefg"
# print(alp)  # abcdefg
# alp.upper()
# print(alp)  # abcdefg -> 재할당을 하지 않았기에 그대로 출력된다.

# alp = alp.upper()
# print(alp)

# lower() -> 단어를 소문자로 바꾸는 매소드

# capitalize(), title() -> 한 글자만 대문자로 바꾸는 매소드
# capitalize() -> 문자열의 첫 글자만 대문자로 바뀜
# title() -> 문자열에서 공백 기준 첫 단어의 첫 글자가 대문자로 바뀜

# isupper()·islower() -> 모두 대문자/소문자인지 참·거짓으로 확인

# 공백 제거

# strip() -> 앞뒤 공백 제거, 중간에 있는 공백은 제거하지 않음

# lstrip()은 왼쪽, rstrip()은 오른쪽만 공백 제거

# raw = "         정상          "

# print(raw.strip())  # 양쪽 공백 제거
# print(raw.lstrip())  # 왼쪽 공백 제거
# print(raw.rstrip())  # 오른쪽 공백 제거

# # strip()으로 문자 제거

# word = " ===정 상=== "
# print(word.strip("= "))

# # 갯수 상관없이 지정한 문자 삭제
# # strip 자체가 공백을 지우는 것
# # 결국 기억해야할 것은 문자열 앞 뒤만 제거한다는 것
# # strip("?"), ?는 문자열 -> 이 때 만약 ?가 문자열 양 쪽 끝에 없다면 실행되지않고 문자열 자체가 출력된다.

# # 메서드연결해서쓰기(체이닝) -> 여러 작업을 매서드 연결로 진행하는 것
# # -> 대신 순서가 중요함

# raw = "   ADFASDddfdf    "

# # 체이닝 x

# raw1 = raw.strip()
# raw2 = raw1.lower()
# print(raw2)

# # 체이닝 o

# chain = raw.strip().lower()
# print(chain)

# # 변수에 할당 안하고 가능
# print(raw.strip().lower())

# # 기존 변수에도 재할당 가능
# raw = raw.strip().lower()
# print(raw)


# # 단어 치환

# # 특정 문자열을 제거하거나 치환할 때 사용
# # 제거할 때는 인자의 두 번째를 ""(빈 문자열)로 작성
# print(
#     "정 상 가 동".replace(" ", "")
# )  # 정상가동 출력 -> 첫번째 인자(바꾸고 싶은 문자열), 두번째 인자(바꿀 내용 문자열)
# print(
#     "  정 상 가 동  ".replace(" ", "")
# )  # 정상가동 출력 -> 문자열 안에서의 공백을 다 바꾼다.
# print("정 상 가 동".replace("  ", ""))  # 정 상 가 동, 공백이 두칸인 경우만 바꾼다.

# word = "설비 정상 가동"
# print(word.replace("정상", "점검"))

# # replace() 체이닝
# num = "       010-2232-2213    "
# num = num.replace(" ", "").replace("-", "")  # 공백과 - 제거
# print(num)

# # List -> 리스트 : 여러 값을 순서대로 담는 그릇
# # split() -> 공백을 기준으로 나눠서 리스트로 출력

# # print("에스프레소 아메리카노 카페라테".split())

# # # 구분자를 정하고 싶은 경우 -> split("?") : 해당 구분자를 적으면 된다.

# fruits = "딸기, 거봉, 키위, 수박"
# # print(fruits.split(","))

# # 리스트의 인덱스
# # fruits_list = fruits.split(",")
# # print(fruits_list[1])  # 인덱스는 0번 부터 시작
# # print(fruits_list[3])
# # print(fruits_list[-1])  # -1을 쓰면 마지막 리스트의 마지막 값 출력

# # split 횟수 제한
# fruits_list1 = fruits.split(",", 1)

# print(fruits_list1)

# join() : 리스트를 하나의 문자열로 합치는 기능
# "구분자".join(리스트)으로 작성해야함

# fruits_list = ["딸기", "거봉", "키위", "사쿠란보"]

# print("-".join(fruits_list))  # 딸기-거봉-키위-사쿠란보
# print(",".join(fruits_list))  # 딸기,거봉,키위,사쿠란보
# print(" ".join(fruits_list))  # 딸기 거봉 키위 사쿠란보

# # print함수의 sep, end 매소드

# print("2026", "07", "27")  # 2026 07 27

# # sep 속성을 사용하면 구분을 공백이 아닌 특정 문자열로 가능
# print("2026", "07", "27", sep="사랑해")  # 2026사랑해07사랑해27

# # end 속성 사용 시 출력문 마지막에 해당 문자열 삽입
# print("안녕", "하세")  # 안녕 하세
# print("안녕", "하세", end="요")  # 안녕 하세요

# print("안녕", "하세", end="요" + "이렇게")  # + 연산자를 이용하면 이어쓰기 가능

# # print()문은 기본적으로 sep = " ", end = "\n"

# f-string
# 한 줄에서 문자열 정수형 등 다른 타입을 쉽게 연결해서 쓰는 용도
# 따옴표 밖에 f 작성하기
# 변수 명은 꼭 중괄호 안에 감싸기

# name = "김도진"
# age = 24

# print(f"안녕하세요 저는 {name}이고 나이는 {age}살 입니다.")

# # f-string 연산

# hour = 8

# # 우리는 하루에 8시간 수업을 듣고, 이는 480분 입니다.
# print(f"우리는 하루에 {hour*60}분 수업을 듣고 {hour}시간 입니다.")

# 텍스트정리순서정리
# 정리는 보통 공백 제거 → 통일·치환 → 나누기 → 정리 → 합치기
# 지저분함이 가장 흔한 공백부터 떼어 냄
# 필요한 단계만 골라 쓰면 됨 (다 거치진 않음)
# 어떤 데이터를 만나도 당황하지 않는 흐름
