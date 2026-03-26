# 알고리즘은 특정 문제를 해결하기 위한 명확하고 단계적인 절차나 규칙의 집합입니다. 
# 입력값을 받아 유한한 시간 내에 정해진 논리적 순서에 따라 문제를 해결하고 결과물을 도출하는 과정으로, 
# 컴퓨터 프로그래밍 및 일상생활의 문제 해결(예: 요리법)에 모두 적용됩니다.
# (예: 요리법)에 적용된다.

# 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘

def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s

print(sum_n(10))
print(sum_n(100))

print("가우스의 합 공식으로 n까지의 합")
def sum_n2(n):
    return n * (n + 1) // 2

print(sum_n2(10))
print(sum_n2(100))
# 알고리즘 - 계산복잡도(시간), 공간복잡도(메모리)

print("최대값 구하기 알고리즘")

d = [17, 92, 18, 33, 58, 7, 32, 42]
def find_max(a):
    n = len(a)
    maxv = a[0]
    for i in range(1, n):
        if a[i] > maxv:
            maxv = a[i]
    return maxv

print(find_max(d))

print('\n최대 공약수 구하기======')
def gcdFunc(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1

print(gcdFunc(4, 6))
print(gcdFunc(16, 24))
print(gcdFunc(81, 27))

print('\n 최대 공약수 구하기2 (유클리드 방식) --- ')
def gcdFunc2(a, b):
    if b == 0:
        return a
    return gcdFunc2(b, a % b)       # 좀 더 작은 값으로 재귀호출

print(gcdFunc2(4, 6))
print(gcdFunc(16, 24))
print(gcdFunc(81, 27))
