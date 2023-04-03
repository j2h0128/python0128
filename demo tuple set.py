#demo tuple set.py

a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(type(a))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#tuple은 입력한 순서로 출력(read-only)

tp=(1,2,3)
print(type(tp))
print(tp.index(2))


#함수를 정의
def calc(a,b):
    return a+b, a*b

#함수를 호출
#디버깅 중단점
result=calc(3,4)
print(result)

#형식 변환
a=set((1,2,3))
print(a)
b=list(a)
b.append(4)
print(type(b))
print(b)

print("--------dict-----------")
color={"apple":"red", "banana":"yellow"}
print(color["apple"])
#입력
color["kiwi"]="green"
#삭제
del color["apple"]
print(color)


phone={'kim':'010-111','lee':'010-222','park':'010-567'}
for item in phone.items():
    print(item)

for k,v in phone.items():
    print(k,v)

    print('park' in phone)
    print('kang' not in phone)

p=phone
p['kang']='010-4678'
print(p)
print(phone)
print(id(phone), id(p))

