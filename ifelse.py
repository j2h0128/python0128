#ifelse.py

score=int(input("점수를 입력:"))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 90:
    grade = "B"
elif 71 <= score <= 80:
    grade = "C"
elif 60 <= score <= 70:
    grade = "D"
print('등급은', grade)



#반복구문
value=5
while value > 0:
    print(value)
    value -= 1
