# Function1.py
#함수를
def setValue(a):
    x=a
    print(x)

#함수 호출
result = setValue(5)
print(result)

def swap(x,y):
    return  y,x

#호출

print(swap(5,6))

print("----불변형식과 가변형식----")
a = 1.2
print(id(a))
a = 2.3
print(id(a))
lst=[1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

#기본값이 있는경우
def times(a=10,b=20):
    return a*b

#call
print(times())
print(times(5))
print(times(5,6))

#keyword
def connectURI(sever,port):
    strURL = "http://"+sever+":"+port
    return strURL
#call
print(connectURI("credu.com", "80"))
print(connectURI(port="80", sever="credu.com"))

def union(*ar):
    result = []
    #단어 슬라이싱
    for item in ar :
        #각 글자를 슬라이싱
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))