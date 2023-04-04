#전역변수
str = "Not Class Member"
class GString:
    def __init__(self):
        #인스턴스 멤버 변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #약간의 버그 아닌 버그 수정(?)
        print(self.str)

#인스턴스 생성
g = GString()
g.set("First Message")
g.print()
