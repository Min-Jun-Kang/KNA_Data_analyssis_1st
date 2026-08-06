# f = open("sample.txt", "r", encoding="utf-8")

# # print(type(f).__name__)  # 타입의 이름 : TextIOWrapper

# # 텍스트파일 파일 한 줄씩 문자열을 만들어서 리스트로 저장

# lines = f.readlines()

# print(lines)

# f.close()  # 열었다면 꼭 닫기

# # 만약 신경써서 파일 닫기(close)를 까먹었을 때
# # with open ... as 문법을 쓰는 것이 좋다.

# with open("sample.txt", "r", encoding="utf-8") as f:
#     # 앞으로 들여쓰기 된 코드가 끝나면
#     # 파일 접근을 닫습니다.(close)

#     # 텍스트파일 파일 한 줄씩 문자열을 만들어서 리스트로 저장
#     lines = f.readlines()
# print(lines)

# # 쓰기모드로 파일 새롭게 만들기
# f = open("hello.txt", "w", encoding="utf-8")

# # 파일 쓰기에 줄바꿈을 표현하려면 \n을 포함시킨다.
# f.write("안녕하세요\n")
# # 파일 쓰기에 탭 들여쓰기를 포함하려면
# f.write("\t반갑습니다\n")

# f.close()

# # 이어쓰기 모드(append)로 파일에 내용을 추가하기

# f = open("hello.txt", "a", encoding="utf-8")

# f.write("맛점하세요!!")

# f.close()
