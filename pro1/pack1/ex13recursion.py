# 재귀함수 : 함수가 자기 자신을 호출 - 반복 처리
def countDown(n):
    if n == 0:
        print('완료')
        # return 
    else: 
        print(n, end=' ') 
        countDown(n-1) # 재귀

countDown(5)
print('--------1부터 n까지 합--------')

# 재귀함수 : 함수가 자기 자신을 호출 - 반복 처리
def totFunc(n):
    if n == 0: 
        print('탈출')
        return 0
    return n + totFunc(n-1) # 재귀

result = totFunc(5) # 서로 다른 function 5개가 생김 -> 수가 많아질수록 메모리 많이 잡아먹음
print('result : ', result)

print('--------5 Factorial(계승)--------')

def factorialFunc(a):
    if a==1:
        print('탈출')
        return 1
    return a * factorialFunc(a-1)

print(factorialFunc(5))

print('end')
