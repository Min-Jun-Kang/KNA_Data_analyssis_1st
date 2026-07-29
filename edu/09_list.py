# list는 python의 자료형 중 하나
# 여러 개의 값을 [대괄호]에 감싸서 순서대로 저장
# 나열된 값들은 자동으로 각자의 인덱스 번호를 순서대로 가진다


# temps = [35, 36, 37, 38]  # int 리스트
# float_temps = [36.4, 36.5, 36.6, 36.7]  # float 리스트
# machines = ["펌프", "압축기", "모터"]  # string 리스트

# # 자료형이 달라도 한 리스트에 담을 수 있음
# mixed = ["펌프", 78, True]

# # 리스트에 자동으로 순서 인덱스가 붙는다면?

# print(temps[2])  # 37 > 인덱스로 해당 순서에 위치한 요소 뽑아내기
# print(temps[-1])  # 마지막 요소 뽑기

# # 빈 리스트

# empty = []

# # 리스트에 담긴 값의 갯수 세기
# # len() 내장함수 사용
# print(len(temps))  # 4
# print(len(empty))  # 0

# # 리스트에 담긴 값의 갯수 변수에 저장

# temps_length = len(temps)
# print(temps_length)  # 4

# # 리스트의 인덱스

# print(temps[0], temps[-1])  # 가장 첫 번째 요소, 가장 마지막 요소
# print(temps[-1])
# print(temps[len(temps) - 1])
# -1을 사용하는 이유는 최신 값은 대체로 뒤에 추가가 됨
# 가장 최신 값은 결국 마지막 인덱스의 요소
# len 함수를 사용해서 리스트 길이 -1로 계산이 가능하지만
# 이 작업이 번거로워 -1을 가장 많이 사용한다

# 없는 인덱스 호출
# 인덱스 오류가 난다.(범위 밖 호출)
# 인덱스 범위를 벗어나지 않도록 유의해야한다.

# 리스트의 자로형

# # temps라는 리스트 자체
# print(f"temps: {temps}")  # 리스트 전체
# print(f"type(temps): {type(temps)}")  # list 타입

# # temps라는 리스트의 인덱스 요소
# print(f"temps[0]: {temps[0]}")  # 리스트 0번째 요소
# print(f"type(temps[0]): {type(temps[0])}")  # 리스트 0번째 요소 타입

# 다른 자료형의 값이 들어있는 리스트의 요소 타입

# # float 값이 들어있는 경우
# float_temps = [36.4, 36.5, 36.6, 36.7]
# print(type(float_temps[0]))

# # string 값이 들어있는 경우
# machines = ["펌프", "압축기", "모터"]
# print(type(machines[0]))


# # 리스트 슬라이싱
# # 리스트명[시작:끝:간격]
# # 시작, 끝, 간격 인덱스는 모두 생략 가능(문자열과 동일)

# temps = [35, 36, 37, 38]
# print(type(temps[1:3]))  # 리스트로 출력된다.
# print(type(temps[1:2]))  # 리스트로 출력된다.
# print(temps[:2])  # [35, 36]
# print(temps[:2], temps[3:])  # [35,36], [38]
# print(temps[::1])  # [35, 36, 37, 38]
# print(temps[::3])  # [35, 38]
# print(temps[100:999])  # [] > 슬라이싱은 없는 인덱스를 넣으면 빈 값을 출력

# # 인덱싱 vs 슬라이싱
# # 인덱싱 temps[0]은 값 하나(35)
# # 슬라이싱 temps[0:2]은 리스트 ([35, 36])
# # 슬라이싱은 영역을 잘라내는 역할이기 때문에 리스트를 반환한다

# 리스트 값 바꾸기 > 문자열과는 다른 방식, 문자열은 replace 사용

# temps = [25, 26, 24, 28, 27]
# temps[2] = 99  # 인덱스 2의 값 교체
# print(temps)  # [25, 26, 99, 28, 27]

# # in (존 재 확 인) > 문자열과 같은 방식

# machines = ["펌프", "모터", "압축기"]
# print("모터" in machines)  # True
# print("모터" not in machines)  # False
# print("프레스" in machines)  # False
# print("프레스" not in machines)  # True

# # 특정 값의 index 찾기

# machines = ["펌프", "모터", "압축기"]

# # 리스트 이름.index(원하는 값)
# i = machines.index("압축기")
# print(f"압축기의 인덱스: {i}")
# # .index() 매서드는 리스트에서 가장 처음 등장하는 인덱스만 반환
# # 계속 찾으려면 반복해서 슬라이싱해서 찾아야함

# 리스트 값 추가

# append() > 리스트 끝에 값 추가
# nums = [1, 2, 3, 4, 5]
# nums.append(999)
# # print(nums)  # [1, 2, 3, 4, 5, 999] > 마지막에 추가, 재할당을 하지 않아도 추가 된다.

# new_nums = nums  # 스스로의 메모리를 할당받지 않고, 주소만 복사
# # 복사한 메모리 주소에 append를 했기 때문에 원본까지 영향을 받음
# new_nums1 = nums.copy()  # 메모리를 할당받음
# # 이를 해결하기 위해 .copy() 매서드 사용, 새로운 메모리에 nums 저장
# new_nums.append(111)
# new_nums1.append(222)

# print(f"nums리스트: {nums}")
# print(f"new_nums리스트: {new_nums}")
# print(f"new_nums1리스트: {new_nums1}")

# # insert() > 원하는 위치에 삽입, 인자를 2개 전달해야 한다
# # insert(위치, 값)
# # 리스트에서 원하는 위치에 값을 삽입
# nums.insert(2, 999)
# print(f"insert후 리스트: {nums}")

# # extend() > 2개의 리스트 합치기
# # 머리가 될 리스트.extend(꼬리가 될 리스트)

# morning = [1, 2, 3, 4, 5]
# afternoon = [6, 7, 8, 9]

# morning.extend(afternoon)

# print(morning)
# print(afternoon)

# after = afternoon.extend(afternoon)  # extend는 실행만 진행하기 때문에 반환할 값이 따로 없다.

# print(afternoon)
# print(after)  # extend는 실행만 진행하기 때문에 반환할 값이 따로 없다.

# 꼭 알아야 하는 개념
# append(), insert(), extend()
# .append(추가할 값) : 리스트 마지막에 값 추가
# .insert(위치, 값) : 첫 번째 인자인 위치 인덱스에 값을 삽입
# .extend(합칠 리스트) : 두 리스트를 하나의 리스트로 합체
# 위 세가지 매서드들은 원본 리스트 자체를 수정

# # remove(값) > 값으로 제거, 위치는 모르고 삭제할 "값"만 알 때 사용하는 요소 삭제 매서드

# list1 = [1, 2, 3, 4, 5, 6]
# list1.remove(5)
# print(list1)

# # pop(위치) > 그 위치의 값을 꺼내 돌려준다
# # 삭제한 인덱스의 값을 출력
# print(list1.pop(0))  # 값이 존재한다
# print(list1)

# # del 리스트[인덱스 번호] > 값을 돌려주지 않는다, 구간 삭제도 가능

# del list1[0]
# print(list1)

# del list1[:]
# print(list1)  # [] > 빈 리스트가 된다.


# # sort() > 정렬, 작은 값부터(오름차순), reverse = True면 큰 값부터
# n = [37, 2, 8, 100, 1004, -1, 22]
# print("n 리스트 원본:", n)
# # 오름차순 정렬
# n.sort()  # 원본 리스트 수정
# print("n 오름차순 정렬:", n)
# # 내림차순 정렬
# n.sort(reverse=True)
# print("n 내림차순 정렬:", n)

# # reverse() > 리스트의 순서를 그대로 뒤집음
# # 정렬은 해주지 않는다.
# # 뒤로 계쏙 쌓인 결과(최신)를 앞에서부터 보고싶을 때 사용
# n = [37, 2, 8, 100, 1004, -1, 22]
# n.reverse()
# print("리버스 된 n:", n)

# # count(), index() > 몇 번 나오는지, 값이 처음 나오는 위치

# # .count(찾을 값)

# f = [
#     "일회용컵",
#     "텀블러",
#     "텀블러",
#     "일회용컵",
#     "텀블러",
#     "일회용컵",
#     "텀블러",
#     "텀블러",
#     "일회용컵",
# ]

# print(f.count("일회용컵"))
# print(f)  # 원본에 영향을 주지 않는다.

# # 특정 값의 위치 찾기
# # .index(위치를 찾을 값)
# # 리스트에서 가장 첫 위치만 찾아줌

# print(f.index("일회용컵"))
# print(f)  # 원본에 영향 없음
