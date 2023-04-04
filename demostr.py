#demostr.py

# print(dir(str))

strA="python is powerful"
strB="파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("e",7))
print(strA.startswith("python"))
print(strA.endswith("ful"))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

print("------문자열 공백 제거--------")
u="<<< spam and ham >>>"
result=u.strip("<> ")
print(u)
print(result)
result=result.replace('spam', 'spam, egg')
print(result)
lst=result.split()
print(lst)
print('---하나로 합치기-----')
print(":)".join(lst))
