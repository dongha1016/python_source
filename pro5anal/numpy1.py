# numpy의 ndarray는 단순한 배열이라기 보다,
# 벡터/행렬 연산도 가능한 다차원 수치 데이터 구조다

import numpy as np

# [파이썬 리스트의 특징]
# 리스트는 서로 다른 타입(문자, 숫자, 불리언)을 섞어서 담을 수 있는 유연한 바구니입니다.
ss = ['tom', 'james', 'oscar', 1, True]
print(ss, ' ', type(ss))    # 리스트 타입

# [NumPy ndarray의 특징]
# np.array는 내부의 모든 요소를 '동일한 타입'으로 강제 변환합니다.
# 여기서는 숫자와 불리언이 모두 문자열('1', 'True')로 변환되어 저장되었습니다.
ss2 = np.array(ss)          # 같은 타입의 자료로만 구성(문자열)
print(ss2, ' ', type(ss2))  # numpy.ndarray

# [리스트 연산의 한계]
li = list(range(1, 10))
print(li)
print(li[0], ' ', id(li[0]))
# 리스트에 곱하기 10을 하면 요소값이 커지는 게 아니라, 리스트 자체가 10번 반복되어 길어집니다.
print(li * 10)

print("---" * 10)

# 리스트 안의 숫자를 10배로 만들려면 이처럼 반복문을 돌려야 하는 번거로움이 있습니다.
for i in li:
    print(i * 10, end=' ')

# [배열 연산(Vectorization)의 강력함]
num_arr = np.array(li)
# 배열 요소들의 메모리 주소를 확인해보면 연속적으로 배치되어 처리 효율이 높음을 알 수 있습니다.
print(num_arr[0], ' ', num_arr[1], ' ', id(num_arr[0]), ' ', id(num_arr[1]))
# 배열에 곱하기 10을 하면 모든 요소에 각각 10이 곱해지는 '브로드캐스팅' 연산이 일어납니다.
print(num_arr * 10)

print()
# [데이터 타입 우선순위]
# 하나의 배열에는 하나의 타입만 존재해야 하므로, 정수(1, 2)가 실수(3.5)를 만나 모두 실수로 변환됩니다.
a = np.array([1, 2, 3.5], dtype='float32')
print(a, type(a))   # ndarray는 동일 타입만 취급
# 여러 타입의 자료가 입력되면 상위 타입으로 자동변환 // int => float => complex => str..

print()
# [다차원 배열의 구조]
b = np.array([[1, 2, 3], [4, 5, 6]])
# shape는 (행, 열)의 크기를 나타내며, 인덱싱을 통해 특정 위치나 행 전체를 추출할 수 있습니다.
print(b.shape, ' ', b[0, 0], b[[0]])
# b.shape => 2행 3열임을 의미

# [특수 행렬 생성 함수들]
# 0과 1로 이루어진 2행 2열로 만들어줌 (초기화 시 자주 사용)
print()
c = np.zeros((2,2))
print(c)
d = np.ones((2,2))
print(d)
# 주대각 성분이 1인 3 * 3 행렬 (단위 행렬: Identity Matrix)
e = np.eye(3)
print(e)

print("여기보자")
# [난수 생성]
print(np.random.rand(5))    # 0~1 사이에서 균일하게 뽑는 '균등 분포'
print(np.random.randn(5))   # 평균 0, 표준편차 1인 '표준 정규 분포'

# [시드(Seed) 설정]
np.random.seed(0)               
# 난수 생성 알고리즘의 시작점을 고정하여, 실행할 때마다 항상 같은 난수가 나오게 합니다. (실험 재현용)
print(np.random.randn(2, 3))    # 2행 3열 난수 행렬 나옴

# [연속된 수 생성 비교]
print(list(range(0, 10))) # 파이썬 기본 리스트 범위 생성
print(np.arange(10))      # NumPy 전용 범위 생성 (더 빠르고 연산 가능함)

print()
# 인덱싱/슬라이싱

a = np.array([1,2,3,4,5])
print(a, ' ', a[1])
print(a[1:4])   # 시작은 포함, 끝은 포함하지 않음 [2 3 4]
print(a[1:])    # 1번 인덱스부터 끝까지 [2 3 4 5]
print(a[1:5:2]) # 1번부터 5번 미만까지 2칸 간격으로 [2 4]
print(a[-2:])   # 뒤에서 두 번째부터 끝까지 [4 5]

# [얕은 복사 vs 깊은 복사]
b = a   # 주소값만 전달 (얕은 복사): b를 바꾸면 원본 a도 바뀝니다.  => 메모리 주소를 공유함
print(a[0], ' ', b[0])
b[0] = 88
print(a[0], ' ', b[0])

c = np.copy(a)     # 데이터 자체를 완전히 새로 복제 (깊은 복사): c를 바꿔도 a는 안전합니다.
print(a[0], ' ', c[0])
b[0] = 33
print(a[0], ' ', c[0])