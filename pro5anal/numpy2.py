# 배열 연산
import numpy as np

# [데이터 타입 지정] 
# np.float32를 통해 32비트 부동소수점 타입으로 배열을 생성합니다.
x = np.array([[1,2], [3,4]], dtype = np.float32)
print(x, ' ', x.dtype)

# [차원 재구성 및 타입 변환]
# arange(5, 9)는 [5,6,7,8] 1차원 배열을 만듭니다.
# reshape((2,2))를 통해 이를 2행 2열의 2차원 배열로 구조를 바꿉니다.
y = np.arange(5, 9).reshape((2,2))  # reshape : 차원을 재설정 => 1차원을 2차원으로 변경
# astype은 기존 배열의 데이터를 유지하면서 타입을 변경(정수->실수)할 때 사용합니다.
y = y.astype(np.float32)
print(y, ' ', y.dtype)

print()

# [요소별 산술 연산 (Element-wise Operations)]
# +, -, *, / 기호는 두 배열의 같은 위치에 있는 원소끼리 계산합니다.
print(x + y)    # 파이썬 연산자 오버로딩을 이용한 간편한 방식
print(np.add(x, y))  # numpy 전용 함수 (유니버셜 함수: ufunc) - 대량 데이터에서 더 효율적일 수 있음
# 둘이 같은 의미

print(x - y)
print(np.subtract(x, y))

print(x * y)
print(np.multiply(x, y))

print(x / y)
print(np.divide(x, y))

print('\ndot은 numpy 모듈의 함수나 배열 객체의 인스턴트 ' \
        '메소드를 사용이 가능')
v = np.array([9, 10])
w = np.array([11,12])

# 일반 곱셈(*)은 위치가 같은 요소끼리만 곱합니다. ([9*11, 10*12])
print(v * w)    # 행렬의 요소별 곱셈

# [벡터의 내적(Dot Product)]
# 두 벡터의 대응하는 성분끼리 곱한 뒤 모두 더하는 연산입니다.
print(v.dot(w)) # 내적의 결과는 스칼라(크기만 있고 방향은 없음)
print(np.dot(v, w)) # 계산식: (9*11) + (10*12) = 99 + 120 = 219
# 행렬(2x2)과 벡터(1x2)의 곱도 가능합니다.
print(np.dot(x, v))

print()
# [집합 연산 (Set Operations)]
names1 = np.array(['tom', 'james', 'tom', 'oscar'])
names2 = np.array(['tom', 'page', 'john'])

print(np.unique(names1))    # 중복을 제거하고 유일한 값들만 정렬하여 반환
print(np.intersect1d(names1, names2))   # 교집합: 공통된 요소 추출
# assume_unique=True는 입력 배열에 중복이 없다고 가정하여 연산 속도를 높일 때 사용합니다.
print(np.intersect1d(names1, names2, assume_unique=True))  # 교집합(중복 허용 여부 옵션)
print(np.union1d(names1, names2))   # 합집합: 두 배열의 모든 요소를 합치고 중복 제거

print('\n전치(Transpose) - 2차원 배열에서 행과 열의 위치를 바꿈')
# (i, j) 위치의 원소를 (j, i)로 옮깁니다. 1행 2열 요소가 2행 1열이 됩니다.
print(x)
print(x.T)
print(x.transpose())
# swapaxes(0, 1)은 0번 축(행)과 1번 축(열)을 서로 맞바꾸는 더 포괄적인 개념입니다.
print(x.swapaxes(0, 1))

print('\nBroadcasting : 크기가 다른 배열 간의 연산 - 작은 배열을' \
        ' 여러번 반복해 큰 배열과 연산')
# x는 (3x3) 행렬이고 y는 (1x3) 벡터입니다. 원래는 모양이 달라 연산이 안 되지만,
# NumPy가 y를 자동으로 아래로 3번 복사해서 (3x3)처럼 취급하여 x와 더해줍니다.
x = np.arange(1, 10).reshape(3,3)
y = np.array([1,0,1]) 
print(x)
print(y)
print(x+y)

# [데이터 파일 입출력]
# 현재 배열 x의 수치 데이터를 'my.txt'라는 텍스트 파일로 저장합니다.
np.savetxt("my.txt", x) # 배열 file i/o 저장 (나중에 np.loadtxt()로 다시 읽어올 수 있음)