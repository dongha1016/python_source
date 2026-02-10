# 사용자 정의 함수
"""
def 함수명(가인수,,,):
    #...
    return 반환값  # 1개만 반환, return이 없으면 return None

함수명(실인수,,,)  # 함수 호출
"""

def doFunc1():
    print('doFunc1 수행')

def doFunc2(name):
    print('name : ', name)
    # return None (원래는 이렇게 쓰는게 정석이지만 굳이 명시하지 않아도 됨)

def doFunc3(arg1, arg2):
    re = arg1 + arg2
    return re

def doFunc4(a1, a2):
    imsi = a1 + a2
    if imsi % 2 == 1:
        return
    else: 
        return imsi

doFunc1() # 함수 호출
print('함수 주소는 ', doFunc1) # <function doFunc1 at 0x000001FA9E221440> => 주소를 찍음
print('함수 주소는 ', id(doFunc1)) # 해시코드: 2339754415168
imsi = doFunc1 # 함수의 주소를 넘겨줌
print(doFunc1()) # doFunc1 수행 출력 후 None

print()

doFunc2(7)
doFunc2('길동')
print(doFunc3("대한", "민국") )
print(doFunc3(5,6)) # 정수끼리 더함

print(doFunc4(3, 4))
print(doFunc4(3, 5))

print('---------------')
def triArea(a, b):
    c = a * b * 0.5
    triAreaPrint(c)

def triAreaPrint(cc):
    print('삼각형의 면적은: ', cc)

triArea(4, 5)

print('---------------')
def passResult(kor, eng):
    ss = kor + eng
    if ss >= 50:
        return True
    else: return False
passResult(20, 50)

if passResult(20, 50):
    print('합격')
else: 
    print('불합격')

print('*'*20)
def swapFunc(a, b):
    return b, a      # return (b, a)

a= 10; b = 20
print(a, ' ', b)
print(swapFunc(a, b))

print('*'*30)

def funcTest():
    print('funcTest 멤버 처리')
    def funcInner():
        print('내부 함수') # 내부 함수 정의
    funcInner()

funcTest()

# if 조건식 안에 함수 사용
def isOdd(para):
    return para % 2 == 1 # 홀수: true / 짝수 : False

mydict = {x:x*x for x in range(11) if isOdd(x)}
print(mydict)

print('변수의 생존 범위 (scope rule) ----')
# 변수가 저장되는 이름공간은 변수가 어디서 선언 되었는가에 따라 생존 시간이 다름
# 전역, 지역 변수

player = '전국대표' # 전역변수 * 현재 모듈 어디서든 호출 가능
name = '한국인' # 전역변수

def funcSoccer(): 
    name = '홍길동' # 지역변수 * 현재 함수 내에서만 호출 가능
    player = '지역대표' # 지역변수
    city = '서울'
    print(f'이름은 {name}, 수준은 {player}') 
    print(f'지역은 {city}') 

funcSoccer()
print(f'이름은 {name}, 수준은 {player}')

print('*'*30+'\n')
a = 10 ; b = 20 ; c = 30
def Foo():
    a = 7 # Foo 한정
    b = 100
    def Bar():
        global c 
        # Bar 함수의 멤버가 아니라 모듈(현재 파일)의 멤버가 됨 => 전역변수
        nonlocal b # Bar의 바깥쪽 b를 사용하겠다
        b = 8
        # global로 정의된 변수와는 다르다
        print(f'Bar 수행 후 a:{a}, b:{b}, c:{c}')
        c = 9 # global c 선언 없으면 에러 발생
        b = 200
    Bar()
    print(f'Foo 수행 후 a:{a}, b:{b}, c:{c}') 
    # Foo는 자신의 함수 내에 b, c값이 없기 때문에 global에서 찾음
    
Foo()

print(f'함수 수행 후 a:{a}, b:{b}, c:{c}') # Global만 바라봄(함수는 탐색 안함)


print('*'*30 + '\n')

g = 1
print('g : ', g)
def func():
    global g
    a = g # 1을 넘겨줌
    g = 2 # 지역변수로 선언했지만 a 는 지역변수의 값을 못가져서 에러 발생    
    return a

print(func())
print('g : ', g)