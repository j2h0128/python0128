#부모 클래스 정의(Super Class)
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

#자식 클래스 정의(Sub Class): 대학생
class Student(Person):
    #상속받은 매서드 덮어쓰기(재정의, overfide)
    def __init__(self, name, phoneNumber, subject, studentID):
        #부모 생성자 호출
        #self.name = name
        #self.phoneNumber = phoneNumber
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID

    #상속받고 덮어쓰기
    def printInfo(self):
        print("Info(이름:{0}, 전공:{1}, 학번: {2})".format(self.name, self.subject, self.studentID))
        print("Info(이름:{0}, 전공:{1}, 학번: {2})".format(self.name, self.subject, self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
#print(p.__dict__)
#print(s.__dict__)

p.printInfo()
s.printInfo()

