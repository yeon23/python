
#parent class
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

#son class
class Student(Person):
    #기존 초기화 매서드를 덮어쓰기
    def __init__(self, name, phoneNumber, subject, studentID):
 #       self.name = name
 #       self.phoneNumber = phoneNumber
        #부모의 생성자 호출        
        Person.__init__(self,name,phoneNumber) 
        self.subject = subject
        self.studentID = studentID
    #재정의(덮어쓰기,override)
    def printInfo(self):
        print("Info(이름:{0}, 전화번호: {1})".format(self.name, self.phoneNumber))
        print("Info(학과:{0}, 학번: {1})".format(self.subject, self.studentID))

#인스턴스 생성
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")

#내부의 멤버를 딕셔너리 형태로 보기
#print(p.__dict__)
#print(s.__dict__)

p.printInfo()
s.printInfo()
