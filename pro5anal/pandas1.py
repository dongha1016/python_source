# 고수준의 자료구조(Series, DataFrame)와 빠르고 쉬운 데이터 분석용 함수 제공
# 통합된 시계열 연산, 축약연산, 누락 데이터 처리, SQL, 시각화 ... 
# 데이터 랭글링(Data Wrangling), 데이터 먼징(Data Munging)을 효율적으로 처리 가능 

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# Series : 일련의 객체를 담을 수 있는 1차원 배열과 같은 자료구조로 색인(index)을 갖는다.
obj = pd.Series([3, 7, -5, 4])      # dtype: int64
# obj = pd.Series([3, 7, -5, '4'])    # dtype: object
# obj = pd.Series([3, 7, -5, '사'])   # 요소값은 object type 
# obj = pd.Series((3, 7, -5, 4))
# obj = pd.Series({3, 7, -5, 4})  # set타입은 순서가 없기 때문에 불가 => TypeError: 'set' type is unordered


print(obj, type(obj))   # dtype: int64 <class 'pandas.core.series.Series'>

obj2 = pd.Series([3, 7, -5, 4], index = ['a','b','c','d'])
print(obj2)
print(obj2.sum(), ' ', np.sum(obj2), ' ', sum(obj2))
print(obj2.std())

print(obj2.values)      # 리스트의 값
print(obj2.index)       # 리스트의 인덱스
print(obj2['a'])        # 리스트 인덱스 'a'번째 값 출력
print((obj2[['a']]))    # a 인덱스와 값을 출력
print(obj2[['a', 'b']]) 
print(obj2['a':'c'])    # a에서부터 c 인덱스까지 인덱스와 값을 출력
print(obj2[2])          # 인덱스 사용
print(obj2.iloc[2])     
print(obj2[1:4])

print(obj2[[2,1]])
print(obj2.iloc[[2,1]]) # 2 index에서 1개씩

print('a' in obj2)      # True
print('k' in obj2)      # False

print('파이썬 dict 자료를 Series 객체로 생성')
names = {'mouse':5000, 'keyboard':25000, 'monitor':450000}
print(names)
obj3 = Series(names)
print(obj3, ' ', type(obj3))   # <class 'pandas.core.series.Series'>
obj3.index = ['마우스', '키보드', '모니터'] # 인덱스 값 변경
print(obj3, ' ', type(obj3))

obj3.name = "상품가격"          # 시리즈의 이름을 붙임("상품가격")
print(obj3)

print('\nDataFrame 객체----------------------')
df = pd.DataFrame(obj3)
print(df, ' ', type(df))
#        상품가격
# 마우스    5000
# 키보드   25000
# 모니터  450000   <class 'pandas.core.frame.DataFrame'>

data = {
    'irum':['홍길동', '한국인', '신기해', '공기밥', '한가해'],
    'juso':('역삼동', '신당동', '역삼동', '역삼동', '신사동'),
    'nai':[23,25,33,23,35]
}
frame = pd.DataFrame(data)
print(frame)
#   irum juso  nai
# 0  홍길동  역삼동   23
# 1  한국인  신당동   25
# 2  신기해  역삼동   33
# 3  공기밥  역삼동   23
# 4  한가해  신사동   35

# Series가 모여 DataFrame을 구성하는 것
print()
print(frame['irum'])    # 동일 : print(frame.irum)
print(type(frame.irum)) # Series
print(DataFrame(data=data, columns=['juso', 'irum', 'nai']))    
# column의 순서를 바꾼다
#   juso irum  nai
# 0  역삼동  홍길동   23
# 1  신당동  한국인   25
# 2  역삼동  신기해   33
# 3  역삼동  공기밥   23
# 4  신사동  한가해   35

# NaN (결측치)
frame2 = pd.DataFrame(data, columns=['irum', 'nai', 'juso', 'tel']
                      , index=['a','b','c','d','e'])
print(frame2)   # tel의 값은 입력한적이 없기 때문에 NaN
frame2['tel'] = '111-1111'  # tel column에 전체 채워짐
print(frame2)

val = pd.Series(['222-2222','333-3333','444-4444'], index = ['b', 'c', 'e'])
print(val)
frame2['tel'] = val
print(frame2)
#   irum  nai juso       tel
# a  홍길동   23  역삼동       NaN
# b  한국인   25  신당동  222-2222
# c  신기해   33  역삼동  333-3333
# d  공기밥   23  역삼동       NaN
# e  한가해   35  신사동  444-4444

print()
print(frame2.T)         # Transpose => 전치

print()
print(frame2.values)    # 결과는 list type
print(frame2.values[0, 1])  # 0행 1열
print(frame2.values[0:2])   # 0행과 1행

frame3 = frame2.drop('d')           # d행 삭제
frame3 = frame2.drop('d', axis = 0) # 위와 동일한 의미
print(frame3)
frame4 = frame2.drop('tel', axis = 1)
print(frame4)

print('*'*50)
print(frame2)
print(frame2.sort_index(axis=0, ascending=False))    # 행단위로 descending sorting('e'부터 시작)
print(frame2.sort_index(axis=1, ascending=True))     # 열단위로 ascending sorting('irum'부터 시작)

print(frame2.rank(axis=0))      # 행 기준으로 순위(순서)를 적음

counts = frame2['juso'].value_counts()      # 주소의 value값의 개수를 새는 것
print(counts)

# 문자열 자르기 

data = {
    'juso':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon':[23, 25, 15]
}
fr = pd.DataFrame(data)
print(fr)
result1 = Series([x.split()[0] for x in fr.juso])   # 공백을 기준으로 나눈다
result2 = Series([x.split()[1] for x in fr.juso])
print(result1)
print(result2)
print(result1.value_counts())