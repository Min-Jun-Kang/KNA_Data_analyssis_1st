# # print(NameError 만들기)  # SyntaxError 발생
# # print(NameError만들기)  # NameError 발생 > 문법적인 오류가 있는지 확인하고 변수에 오류가 있는지 확인
# print("NameError만들기")  # ""감싸주면 에러 발생 X

# print("=====SyntaxError 만들기=====")
# print("온도) # SyntaxError: unterminated string literal (detected at line 6) > ""가 없어서 문자열 끝이 어딘지 몰라서 생기는 오류
# print("진동" # SyntaxError: '(' was never closed > ()가 닫기지 않아서 나오는 오류

# print("온도", 75)
# # NameError: name '온도' is not defined > 온도 변수가 없어서 생기는 오류, 온도 변수를 만들거나 문자열로 바꾸기 > "온도"
# print("진동", 2, 3)
# # SyntaxError: '(' was never closed > 괄호가 닫기지 않아서 생기는 오류, 괄호를 마저 닫는다.
# print("압력", 4.0)
# # SyntaxError: invalid syntax > :가 뭔지 알수가 없어서 생기는 오류? > ,로 바꾼다.

# print("=====", "1번", "설비", "점검", "=====")
# # ,를 이용하면 띄어쓰기가 되면서 이어서 적을 수 있다.
# print("온도(℃):", 40 + 42)
# # 정상 온도 : 71℃
# print("온도 " + "상승량: " + "11")
# # 갑작스런 온도 상승을 보임 (+ 연산자 이용 시 숫자를 문자로 바꿔야함)
