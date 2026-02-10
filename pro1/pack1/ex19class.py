# oop(객체 중심 프로그래밍 가능): 새로운 타입 생성, 포함, 상속, 다형성 등을 구사
# Class(설계도)로 인스턴스 해서 객체를 생성(별도의 이름 공간을 갖음)
# 객체는 멤버필드(변수)와 메소드로 구성
# 자바와 달리 접근 지정자가 없다. 메소드 오버로딩 없다.
# 모듈의 멤버 : 변수, 명령문, 함수, 모듈, 클래스

print('객체 만들기')

class TestClass:
    aa = 1 # 멤버 변수(멤버 필드). 현재 클래스 내에서 전역

    def __init__(self): # 특별한 메소드
        print('생성자 : 객체 생성 시 가장 먼저 1회만 호출 - 초기화 담당')
    # 메소드는 함수와 다르게 무조건 argument가 있어야 하고 
    # 이는 self가 그 역할을 함
    # 생성자를 만들어주지 않더라도 자동으로 만들어주기도 함

    def __del__(self): 
        print('소멸자 : 프로그램 종료 사 자동실행. 마무리 작업')

    def printMsg(self): # 일반 메소드
        name = '한국인' # 지역변수 : printMsg에서만 유효
        print(name)

print(TestClass) # 출력 : <class '__main__.TestClass'>
test = TestClass() # 생성자 호출하며 객체 생성
print('test 객체의 멤버 aa : ', test.aa) # => 소멸자가 마지막으로 출력됨

# method call
test.printMsg()   
# 1. Bound Method Call => 객체변수(test)를 printMsg에 넣은 것으로 취급
TestClass.printMsg(test) 
# 2. UnBound Method Call 
# 괄호에 argument가 없을 경우 error

print(type(1))
print(type(1.0))
print(type(test)) # TestClass라는 새로운 타입
print(id(test))
print(id(TestClass)) 
# test는 TestClass의 객체이면서 주소는 다름  
# test = 객체 변수

test2 = TestClass() # 객체 생성 한개 더
print(id(test2))