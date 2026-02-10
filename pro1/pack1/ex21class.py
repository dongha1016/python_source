kor = 100              # 모듈의 전역변수

def abc():
    kor = 0            # 함수 내의 지역변수
    print('모듈의 멤버 함수')

class My:
    kor = 80           # My 멤버 변수(필드)
    def abc(self):
        print('My 멤버 메소드')

    def show(self):
        kor = 77       # 메소드 내의 지역변수
        print(kor)
        print(self.kor)
        self.abc()     # My 멤버 메소드
        abc()          # 모듈의 멤버 함수

my = My()
my.show()

print('*'*50)
print(My.kor)          # 80
tom = My()
print(tom.kor)         # 80
tom.kor = 88    
print(tom.kor)         # 88

oscar = My()
print(oscar.kor)       # 80

