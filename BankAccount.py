# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #사고의 빌미
        #self.id = id
        #self.name = name 
        #self.balance = balance 

        #사고 방지
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    #내가 출력한 형태를 문자열로 return
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
#사고
#account1.balance=15000000000000 --> 이러면 사고남
account1.balance=2500000000 #사고 안 남 ^^
print(account1)
