# pandas 문제 1)
#   a) 표준정규분포를 따르는 9 X 4 형태의 DataFrame을 생성하시오. 
#      np.random.randn(9, 4)

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

print("========================문제 1-a))======================")
df = pd.DataFrame(np.random.randn(9, 4))
print(df)

#   b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No3, No4로 지정하시오
print("========================문제 1-b))======================")
df.columns = ['No1', 'No2', 'No3', 'No4']
print(df)
#   c) 각 컬럼의 평균을 구하시오. mean() 함수와 axis 속성 사용
print("========================문제 1-c))======================")
sum = df.mean(axis = 0)
print(sum)

# pandas 문제 2)
# a) DataFrame으로 위와 같은 자료를 만드시오. colume(열) name은 numbers, row(행) name은 a~d이고 값은 10~40.

data = {'numbers':[10, 20, 30, 40]}
df = pd.DataFrame(data, index = ['a', 'b', 'c', 'd'])

print(df)
# b) c row의 값을 가져오시오.

print(df.loc['c'])

# c) a, d row들의 값을 가져오시오.

print(df.loc[['a', 'd']])

# d) numbers의 합을 구하시오.

sum = df.sum()
print(sum)
# e) numbers의 값들을 각각 제곱하시오. 아래 결과가 나와야 함.

print(df.mul(df))

# f) floats 라는 이름의 칼럼을 추가하시오. 값은 1.5, 2.5, 3.5, 4.5    아래 결과가 나와야 함.

df.loc[:, 'floats'] = [1.5, 2.5, 3.5, 4.5]
print(df)

# g) names라는 이름의 다음과 같은 칼럼을 위의 결과에 또 추가하시오. Series 클래스 사용.
print("========================문제 1-g))======================")
s1 = pd.Series(['길동', '오정', '팔계', '오공'], index = ['d', 'a', 'b', 'c'])

s2 = pd.DataFrame(s1, columns=['names'])
gg = s2.sort_index(axis=0, ascending=True)
df['names'] = gg
print(df)

# pandas 문제 3)
# 1) 5 x 3 형태의 랜덤 정수형 DataFrame을 생성하시오. (범위: 1 이상 20 이하, 난수)

ss = np.random.randint(1, 20, 15).reshape(5,3)
df = pd.DataFrame(ss)
print(df)

# 2) 생성된 DataFrame의 컬럼 이름을 A, B, C로 설정하고, 행 인덱스를 r1, r2, r3, r4, r5로 설정하시오.

df = pd.DataFrame(ss, index = ['r1', 'r2', 'r3', 'r4', 'r5'], columns = ['A', 'B', 'C'])
print(df)

# 3) A 컬럼의 값이 10보다 큰 행만 출력하시오.
ss = df[df['A']>10]
print(ss)

# 4) 새로 D라는 컬럼을 추가하여, A와 B의 합을 저장하시오.
ss = df['A'] + df['B']
df['D'] = ss
print(df)

# 5) 행 인덱스가 r3인 행을 제거하되, 원본 DataFrame이 실제로 바뀌도록 하시오.
print("문제 5번")
# df.drop('r3', inplace=True)
# print(df)
# 6) 아래와 같은 정보를 가진 새로운 행(r6)을 DataFrame 끝에 추가하시오.
#          A     B    C     D
#   r6   15   10    2   (A+B)

# df6 = DataFrame(data, np.arange(4).reshape(1,4), index = ['r6'], columns = ['A', 'B', 'C', 'D'])
# df = pd.concat([df, df6], ignore_index=True)
# print(df)


# pandas 문제 4)
# 다음과 같은 재고 정보를 가지고 있는 딕셔너리 data가 있다고 하자.
# data = {
#     'product': ['Mouse', 'Keyboard', 'Monitor', 'Laptop'],
#     'price':   [12000,     25000,      150000,    900000],
#     'stock':   [  10,         5,          2,          3 ]
# }
# 1) 위 딕셔너리로부터 DataFrame을 생성하시오. 단, 행 인덱스는 p1, p2, p3, p4가 되도록 하시오.

data = {
    'product': ['Mouse', 'Keyboard', 'Monitor', 'Laptop'],
    'price':   [12000,     25000,      150000,    900000],
    'stock':   [  10,         5,          2,          3 ]
}

df = DataFrame(data, index=['p1', 'p2', 'p3', 'p4'])

# 2) price와 stock을 이용하여 'total'이라는 새로운 컬럼을 추가하고, 값은 'price x stock'이 되도록 하시오.

df['total'] = df['price']*df['stock']
print(df)

# 3) 컬럼 이름을 다음과 같이 변경하시오. 원본 갱신
#    product → 상품명,  price → 가격,  stock → 재고,  total → 총가격

df.columns = ['상품명', '가격', '재고', '총가격']
print(df)

# 4) 재고(재고 컬럼)가 3 이하인 행의 정보를 추출하시오.
print(df[df['재고']<=3])

# 5) 인덱스가 p2인 행을 추출하는 두 가지 방법(loc, iloc)을 코드로 작성하시오.



# 6) 인덱스가 p3인 행을 삭제한 뒤, 그 결과를 확인하시오. (원본이 실제로 바뀌지 않도록, 즉 drop()의 기본 동작으로)
# 7) 위 DataFrame에 아래와 같은 행(p5)을 추가하시오.
#             상품명             가격     재고    총가격
#  p5       USB메모리    15000     10    가격*재고