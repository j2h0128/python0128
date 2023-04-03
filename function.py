#function.py

# 1. 함수 정의
def setValue(newValue):
    x=newValue
    print("내부:", x)

# 2. 함수 호출
retValue=setValue(5)
print(retValue)


def swap(x,y):
    return y,x

#호출
retValue=swap(4,5)
print(retValue)
print(retValue[0], retValue[1])


#디버깅을 위한 함수(교집합)
def intersect(prelist, postlist):
    #지역변수로 리스트에 글자를 모아두기
    result=[]
    #H(0) | A(1) | M(2)
    for x in prelist:
        #어떤 글자가 postlist에 있고 x가 result에 없으면
        if x in postlist and x not in result:
            result.append(x)
    return result
#호출
print(intersect("HAM", "SPAM"))