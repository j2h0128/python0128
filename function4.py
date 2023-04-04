#function4.py

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
