# 연산
from pandas import Series, DataFrame
import numpy as np

s1 = Series([1, 2, 3], index = ['a', 'b', 'c'])
s2 = Series([4, 5, 6, 7], index = ['a', 'b', 'd', 'c'])
print(s1, '\n', s2)

print(s1 + s2)  
# 같은 index끼리 연산, 불일치 시 NaN
# a     5.0
# b     7.0
# c    10.0
# d     NaN
print(s1.add(s2))   # numpy 함수를 계승
print(s1.mul(s2))

print()
df1 = DataFrame(np.arange(9).reshape(3,3), columns=list('kbs'), index=['서울', '대전', '부산'])
df2 = DataFrame(np.arange(12).reshape(4,3), columns=list('kbs'), 
                index=['서울', '대전', '제주', '광주'])
print(df1)
print(df2)
#       k  b  s
# 서울  0  1  2
# 대전  3  4  5
# 부산  6  7  8
#     k   b   s
# 서울  0   1   2
# 대전  3   4   5
# 제주  6   7   8
# 광주  9  10  11

print(df1 + df2)
#       k    b     s
# 광주  NaN  NaN   NaN
# 대전  6.0  8.0  10.0
# 부산  NaN  NaN   NaN
# 서울  0.0  2.0   4.0
# 제주  NaN  NaN   NaN
# 대응되는 요소끼리는 연산을 수행하지만 대응이 없으면 NaN

print(df1.add(df2, fill_value=0))   # NaN은 0으로 채운 후 연산에 참여
# sub, mul, div도 가능

print('NaN(결측값) 처리---')
df = DataFrame([[1.4, np.nan], [7, -4.5], [np.nan, np.nan], [0.5, -1]],
                 columns=['one', 'two'])
print(df)
print('\n\n')
print(df.isnull())  # null 값을 탐지하여 True/False로 반환
print(df.notnull())
print(df.dropna())             # 결측값이 하나라도 들어있는 행은 삭제
print(df.dropna(how = 'any'))  # 위와 동일
print()
print(df.dropna(how = 'all'))  # 한 행의 모든 요소가 결측값일 경우에만 삭제
print()
print(df.dropna(subset=['one']))    # 'one'열에 결측값이 있는 행 삭제
print(df.dropna(subset=['two']))    # 'two'열에 결측값이 있는 행 삭제
print()
print(df.dropna(axis='rows'))       # 결측값이 포함된 행은 삭제
print()
print()
print(df.dropna(axis='columns'))    # 결측값이 포함된 열은 삭제

print("원본 처리하는곳")
print(df)
imsi = df.drop(1)   # 원본은 삭제 안됨. 삭제된 결과가 새로운 dataFrame으로 생성됨
print(imsi)
print(df)

print()
df.drop(1, inplace=True)    # 원본 삭제됨
print()
print(df)

# 계산 관련 메소드
print(df.sum())         # 열의 합 - NaN은 연산에서 제외
print(df.sum(axis=0, skipna=True))   # skipna: NaN은 연산에서 제외(생략가능)
print(df.sum(axis=1))   # 행의 합

print()
print(df.describe())    # 요약 통계량 출력
print(df.info())

#   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   one     3 non-null      float64
#  1   two     2 non-null      float64

print()
words = Series(['봄', '여름', '가을', '겨울'])
print(words.describe())

# count     4
# unique    4
# top       봄
# freq      1