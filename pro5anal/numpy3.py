print("####################################################################################################################################")
print("                                    numpy 배열 연산")
print("####################################################################################################################################")

# 배열에 행, 열 추가

import numpy as np

aa = np.eye(3) # 3x3 단위 행렬 생성
print(aa)

# 열 추가 (Column stack)
# np.c_는 두 배열을 '열' 방향으로 붙여줍니다. 
bb = np.c_[aa, aa[2]]       # aa 행렬 옆에 aa의 3번째 행(index 2) 데이터를 새로운 '열'로 추가
print(bb)

# 행 추가 (Row stack)
# np.r_은 두 배열을 '행' 방향으로 쌓아줍니다. 대괄호 [aa[2]]를 사용해 차원을 맞춰줍니다.
cc = np.r_[aa, [aa[2]]]     # aa 행렬 아래에 aa의 3번째 행과 동일한 데이터를 새로운 '행'으로 추가
print(cc)

print("##################################################################")
print("           --- 1차원 : append, insert, delete ---")
print("##################################################################")

a = np.array([1,2,3])
print(a)

# append: 배열의 끝에 요소를 추가합니다.
# axis=0은 1차원 배열에서 유일한 축이므로 생략 가능합니다.
b = np.append(a, [4,5], axis=0)     # 행 기준 (끝에 추가)
print(b)

# insert: 특정 위치(인덱스)에 요소를 삽입합니다.
c = np.insert(a, 0, [6, 7]) # 0번 인덱스 위치에 6, 7을 삽입
print(c)

# delete: 특정 위치(인덱스)의 요소를 삭제합니다.
d = np.delete(a, 1) # 1번 인덱스(값 2)를 삭제
print(d)
print(c)

print("##################################################################")
print("           --- 2차원 : append, insert, delete ---")
print("##################################################################")
aa = np.arange(1, 10).reshape(3,3)
print(aa)
print()
# 축(axis)을 지정하지 않으면 2차원 배열을 1차원으로 펴서(flatten) 작업한 뒤 반환합니다.
print(np.insert(aa, 1, 99))                 # 모든 데이터를 1차원으로 축소 후 삽입
print()
# axis=0: 행(Row) 방향으로 삽입합니다. (결과적으로 행이 늘어남)
print(np.insert(aa, 1, 99, axis=0))         # 2차원 유지 / 1번 행 위치에 99가 채워진 행 삽입
print()
# axis=1: 열(Column) 방향으로 삽입합니다. (결과적으로 열이 늘어남)
print(np.insert(aa, 1, 99, axis=1))         # 2차원 유지 / 1번 열 위치에 99가 채워진 열 삽입
print()


print("##################################################################")
print("           조건 연산 where(조건, 참, 거짓)")
print("##################################################################")
x = np.array([1,2,3])
y = np.array([4,5,6])
conditionData = np.array([True, False, True])
# 엑셀의 IF 함수처럼 조건이 True면 x에서, False면 y에서 값을 가져옵니다.
result = np.where(conditionData, x, y)
print(result)
print()

# 인자가 '조건' 하나만 있으면 해당 조건을 만족하는 데이터의 '인덱스'를 반환합니다.
aa = np.where(x >= 2)
print(aa)               # (array([1, 2]),) : 인덱스 1과 2가 조건을 만족함
print(a[aa])            # 반환된 인덱스를 이용해 실제 값(2, 3)을 추출
print()

print("##################################################################")
print("                          배열 결합 / 분할")
print("##################################################################")

# 배열 결합: 두 배열을 하나로 이어 붙입니다.
kbs = np.concatenate([x, y])
print(kbs)
print()

# 1차원 배열 분할: 데이터를 지정한 개수만큼 등분합니다.
mbc, sbs = np.split(kbs, 2)
print(mbc)
print(sbs)
print()

# 2차원 배열 분할
a = np.arange(1, 17).reshape(4,4)       # 4x4 행렬 생성
print(a)
# hsplit (Horizontal split): 수평 방향으로 자름 (왼쪽/오른쪽으로 나뉨)
x1, x2 = np.hsplit(a, 2)
print(x1)
print(x2)
print()
# vsplit (Vertical split): 수직 방향으로 자름 (위/아래로 나뉨)
print(np.vsplit(a, 2))


print("##################################################################")
print("                 표본 추출(sampling) - 복원, 비복원")
print("##################################################################")
li = np.array([1,2,3,4,5,6,7])

# [복원 추출] 한번 뽑힌 값도 주머니에 다시 넣으므로 또 뽑힐 수 있습니다.
# randint를 이용해 인덱스를 무작위로 생성하여 추출합니다.
for _ in range(5):
    print(li[np.random.randint(0, len(li)-1)], end = " ")
print()

# [비복원 추출] 한번 뽑은 값은 주머니에서 제외하여 중복이 발생하지 않습니다.
import random
# 파이썬 기본 random.sample은 리스트 타입을 입력받아야 하므로 tolist()로 변환합니다.
print(random.sample(li.tolist(), 5))        # 중복 없는 5개 추출
print()

# [np.random.choice] NumPy에서 제공하는 매우 유용한 샘플링 함수입니다.
print(np.random.choice(range(1, 46), 6)) # 기본값은 replace=True (복원)
# replace=True: 뽑은 걸 다시 넣음 (복원) -> 로또 번호라면 중복이 나올 수 있음
print(np.random.choice(range(1, 46), 6, replace=True))        # 복원
# replace=False: 뽑은 걸 빼둠 (비복원) -> 로또 번호처럼 중복 없는 추출에 적합
print(np.random.choice(range(1, 46), 6, replace=False))       # 비복원