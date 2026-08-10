# else와 finally 코드

# text = "999.99"

text = "영크크"

temp = 0

try:
    temp = float(text)  # ValueError: could not convert string to float: '영크크'
except ValueError:
    print("ValueError 발생")
except NameError:
    print("NameError 발생")
finally:
    # 오류가 있던 없던 finally의 코드를 실행해 마무리
    print(temp * 2)
