class Car:
    handle = 1 
    speed = 0 

    def __init__(self, name, speed): # 생성자
        self.name = name    # 현재 객체의 name에게 name 인자값 치환
        self.speed = speed   # 현재 객체의 speed에게 speed 인자값 치환

    def showData(self): # 메소드
        km = "킬로미터"
        msg = "속도" + str(self.speed) + km
        return msg
    
    def printHandle(self):
        return self.handle

print(Car.handle) # 원형(prototype) 클래스의 멤버 호출
car1 = Car('tom', 10) 
# 생성자 호출 후 객체(Object) 생성(=>인스턴스화)
print('car1 객체 주소: ', car1) # car1의 주소가 self로 들어감
print('car1 : ', car1.name, ' ', car1.speed, ' ', car1.handle)
# handle의 경우 car1에 없기 때문에 원형 Class(Car)에서 handle(공유멤버)을 찾는다

car2 = Car('john', 20) 
print('car2 객체 주소: ', car2)
print('car2 : ', car2.name, ' ', car2.speed, ' ', car2.handle)
car1.color = '파랑' # 원형 클래스에는 없음 -> car1에만 존재하는 변수
print('car1.color : ', car1.color)
# print('Car.color', ' ', 'car2.color') # 에러
print(id(Car), id(car1), id(car2))
print(car1.__dict__) # 각각의 멤버를 확인
print(car2.__dict__)

print('---------메소드----------')
print('car1 speed : ', car1.showData()) 
# showData 괄호에는 객체(car1 : self)가 들어간다
print('car2 speed : ', car2.showData())

print()
car1.speed = 80 
car2.speed = 110

print('car1 speed : ', car1.showData())
print('car1 speed : ', car1.showData())
print()

print('car1 handle : ', car1.printHandle())
print('car2 handle : ', car2.printHandle())