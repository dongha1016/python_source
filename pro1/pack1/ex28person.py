# 상속

class Person:
    say = '난 사람이야~~'   # 접근권한 : public
    nai = '20'
    __msg = 'good : private 멤버'   # __(name) => private member

    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai

    def printInfo(self):
        print(f'나이: {self.nai}, 이야기: {self.say}')
    
    def helloMethod(self):
        print('안녕')
        print('hello : ', self.say, self.nai, self.__msg)

print(Person.say, Person.nai)
print('-'*50)
class Employee(Person):
    subject = '근로자'
    say = '일하는 동물'    # hiding(shadowing) 
    def __init__(self):
        print('Employee 생성자')
    
    def printInfo(self):    # 접근권한 : public
        print('Employe 클래스의 printInfo 호출됨')

    def ePrintInfo(self):
        print(self.subject, self.say, self.nai)
        # print(self.__msg)   # __msg : private 멤버이기 때문에 사용 불가
        self.helloMethod()
        self.printInfo()
        print(super().say)
        super().printInfo()

emp = Employee()
print(emp.subject, emp.nai, emp.say)    
# Employee 클래스에서는 nai, say가 없기 때문에 부모 클래스에서 불러옴
emp.ePrintInfo()

print('*'*100)

class Worker(Person):
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai)   # 부모 클래스의 생성자 호출

    def wPrintInfo(self):
        print('Worker - wPrintInfo 처리')
        super().printInfo()

wor = Worker('30')
print(wor.say, wor.nai)
wor.wPrintInfo()

print('*'*100)

class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        super().__init__(nai) # == Worker.__inin__(self, nai)
    
    def pPrintInfo(self):
        print('Programmer - pPrintInfo 처리')

    def wPrintInfo(self):   # 부모 메소드(Worker에도 있음)와 동일 메소드 선언
        print('Programmer에서 overriding')
    
pro = Programmer('35')
print(pro.say, pro.nai)    # super를 2번 타고 올라가서 Person까지 올라감
pro.pPrintInfo()
pro.wPrintInfo()

print('\n클래스 타입 확인')
a = 3; print(type(a))
print(type(pro)) # <class '__main__.Programmer'>
print(type(wor)) # <class '__main__.Worker'>
print(Person.__bases__) # Peson의 부모 클래스 => (<class 'object'>,)
print(Employee.__bases__)
print(Worker.__bases__)
print(Programmer.__bases__)
    