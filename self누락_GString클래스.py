#전역변수
str = "Not Class Member"


#클래스 정의
class GString:
    #초기화매서드(인스턴스 초기화)
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #버그(가능하면 self를 명시)
        print(self.str)

#인스턴스 생성
g = GString()
g.set("First Message")
g.print()
