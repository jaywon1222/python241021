#파일을 쓰기
f=open("test.txt", "wt", encoding="utf-8")
f.write("Hello, World\n")
f.close()

#파일을 읽기
f=open("test.txt", "rt", encoding="utf-8")
text = f.read()
print(text)
f.close

#str클래스 연습
# print(dir(str))

data = "<<< spam and ham >>>"
result = data.strip("<>")
print(result)
print(data)
result2 = result.replace("spam","spam and egg")
print(result2)
lst = result2.split()
print(lst)
print(":)".join(lst))

print("MBC2580".isalnum())
print("MBC2580".isalpha())
print("2580".isdecimal())

print(len("문자열길이"))


