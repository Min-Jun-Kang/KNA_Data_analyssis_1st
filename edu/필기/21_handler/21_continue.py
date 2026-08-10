# 반복문 안에서 예외처리

my_list = ["123", "456", "영크크", "32", "53"]

# 문제 발생 경로 카운트 하기
problems = 0

for text in my_list:
    # 반복을 하는 중에 문제가 생긴 경우만 건너뛰고
    try:
        my_number = int(text)
    # 계속 반복을 이어서 진행시키기
    except:
        print("숫자만 와라")
        problems += 1
        # 문제가 생겼다면 더 이상 반복문 안의 출력까지 이어가면 안된다.
        # 그래서 여기서 끊고 다음 내용 처리하게 반복문 넘기기
        continue
    print(my_number)

print(f"문제 발생한 친구들: {problems}개")
