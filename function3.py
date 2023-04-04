#function3.py

lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i>5:
        break
    print("Item:{0}".format(i))

print("---continue---")
for i in lst:
    if i%2==0:
        continue
    print("Item{0}".format(i))

print("----수열함수-------")
print(list(range(10)))
print(list(range(10,0,-1)))
print(list(range(2000,2024)))
for i in range(5):
    print(i)

print("---리스트컴프리헨션-------")
list=list(range(1,11))
print([i**2 for i in lst if i>5])
tp=("apple","orange","kiwi")
print([len(i) for i in tp])
d={100:"apple",200:"kiwi",300:"banana"}
print([v.upper() for v in d.values()])

print("------filtering Func-------")
lst=[10,25,30]

def getBiggerThan20(i):
    return i>20

iterL=filter(getBiggerThan20, lst)
for i in iterL:
    print(i)

print("----람다함수 활용 filtering Func---------")
iterL=filter(lambda x:x>20, lst)
for i in iterL:
    print(i)
