# 배열에 행, 열 추가

import numpy as np

aa = np.eye(3)
print(aa)

bb = np.c_[aa, aa[2]]   # 2열과 동일한 열 추가
print(bb)

cc = np.r_[aa, [aa[2]]]
print(cc)

print('--append, insert, delete--')
a = np.array([1,2,3])
print(a)
b = np.append(a, [4, 5], axis=0)    # 행 기준
print(b)
c = np.insert(a, 0, [6, 7]) # 0번 index에 추가
print(c)
d = np.delete(a, 1) # index가 1인 값을 삭제
print(d)

print()
aa = np.arange(1,10).reshape(3,3)
print(aa)
print(np.insert(aa, 1, 99))
print(np.insert(aa, 1, 99, axis = 0)) # 행기준(axis=0)
print(np.insert(aa, 1, 99, axis = 1)) # 열기준(axis=1)

print()
# 조건 연산 where(조건, 참, 거짓)
x = np.array([1,2,3])
y = np.array([4,5,6])
conditionData = np.array([True, False, True])
result = np.where(conditionData, x, y)
print(result)

print()
aa = np.where(x >= 2)   # (array([1, 2]),) 인덱스
print(aa)
print(a[aa])

print()
# 배열 결합
kbs = np.concatenate([x,y])
print(kbs)
# 배열 분할
mbc, sbs = np.split(kbs, 2)
print(mbc)
print(sbs)

print()
a = np.arange(1, 17).reshape(4,4)
print(a)
# 배열 좌우로 분할
x1, x2 = np.hsplit(a, 2)
print(x1)
print(x2)
print()
print(np.vsplit(a,2))

print('\n표본 추출(sampling) - 복원, 비복원')
li = np.array([1,2,3,4,5,6,7])

# 복원
for _ in range(5):
    print(li[np.random.randint(0, len(li) - 1)], end = ' ')

print()
# 비복원
import random   # random.sample()은 대상이 list type
print(random.sample(li.tolist(), 5))

print()
# choice
print(np.random.choice(range(1, 46), 6))
print(np.random.choice(range(1, 46), 6, replace=True))    # 복원 
print(np.random.choice(range(1, 46), 6, replace=False))   # 비복원
