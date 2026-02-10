# 함수 장식자(Function Decorator)
# 기존 함수 코드를 고치지 않고 함수의 앞/뒤 동작을 추가하기 
# 함수를 받아서 기능을 덧붙인 새 함수로 바꿔치는 것
# meta 기능이 있음

def make2(fn):
    return lambda:"안녕 " + fn() # fn이 함수인 것을 알 수 있음

def make1(fn):
    return lambda:"반가워 " + fn() # fn이 함수인 것을 알 수 있음

def hello():
    return "홍길동"

hi = make2(make1(hello)) #hi에 make2에서 나온 결과의 주소를 넘겨줌
print(hi())
print()

@make2
@make1
def hello2():
    return "신기해"
print(hello2()) # 안녕 반가워 신기해

print('*'*30)
def traceFunc(func):
    def wrapperFunc(a, b):
        r = func(a, b)
        print(f'함수명:{func.__name__} (a={a}, b={b} -> {r})')
        return r    # 함수의 반환값을 반환
    return wrapperFunc  # wrapperFunc 함수 주소 반환

@traceFunc    # 밑에 있는 함수를 traceFunc로 감싸라
def addFunc(a, b):
    return a + b

print(addFunc(10, 20))

def print_num(n):
    if n == 0:
        return
    print(n)
    print_num(n-1)
print('*'*50)
print_num(5)
