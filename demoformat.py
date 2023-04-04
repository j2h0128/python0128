#demoformat.py

# strURL="www.credu.com/?page="+1
# print(strURL)

strURL="www.credu.com/?page="+str(1)
print(strURL)

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---- 정렬 -------")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).rjust(3))

print("{0:x}".format(10))
print("{0:x}".format(10))
print("{0:x}".format(10))
print("{0:x}".format(10))


#파일에 쓰기
f=open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("처음에는\n두번째라인\n세번째라인")
f.close

#파일 읽기
f=open("c:\\work\\demo.txt", "rt", encoding="utf-8")
result=f.read()
print(result)
print(f.tell())
#다시 처음으로 파일포인터를 이동
f.seek(0)
lst=f.readlines()
print(lst)
f.seek(0)
#코드로 보정
print(f.readline(), end="")
print(f.readline(), end="")
f.close

# Open the file for writing
with open('example.txt', 'w') as f:
    f.write('Hello, world!\n')
    f.write('This is an example file.\n')

# Open the file for reading
with open('example.txt', 'r') as f:
    # Read the whole file
    contents = f.read()
    print(contents)

    # Read line by line
    f.seek(0)  # Reset the file pointer
    for line in f:
        print(line.strip())