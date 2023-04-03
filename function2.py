#function2.py

#기본값 설정
def times(a=10,b=20):
    return a*b

#호출
print(times())
print(times(b=5))
print(times(5,6))

#키워드 인자
def connectURI(server, port):
    strURL="http://" + server + ":" + port
    return strURL

#호출
print(connectURI("naver.com", "80"))
print(connectURI(port="80", server="credu.com"))


#가변인자사용(* tuple 의미)
def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print(union('HAM','EGG'))
print(union('HAM','EGG','SPAM'))

#람다함수(간결하게 함수를 정의, 익명함수)
g=lambda x,y:x*y
print(g(3,4))
print(g(5,7))
print((lambda x:x*x)(3))
print(globals())

