# 고수준의 자료구조(Series, DataFrame)와 빠르고 쉬운 데이터 분석용 함수 제공
# 통합된 시계열 연산, 축약연산, 누락 데이터 처리, SQL, 시각화 ... 
# 데이터 랭글링(Data Wrangling), 데이터 먼징(Data Munging)을 효율적으로 처리 가능 

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# Series : 일련의 객체를 담을 수 있는 1차원 배열과 같은 자료구조로 색인(index)을 갖는다.
# [데이터 타입의 일관성]
# 리스트와 달리 Series는 보통 하나의 데이터 타입으로 통일됩니다. 
obj = pd.Series([3, 7, -5, 4])      # 정수들만 있으므로 dtype: int64
# obj = pd.Series([3, 7, -5, '4'])    # 문자가 섞이면 전체가 object(문자열) 타입이 됨
# obj = pd.Series([3, 7, -5, '사'])   
# obj = pd.Series((3, 7, -5, 4))
# obj = pd.Series({3, 7, -5, 4})  # set타입은 순서가 없기 때문에 불가 => TypeError: 'set' type is unordered

print(obj, type(obj))   # dtype: int64 <class 'pandas.core.series.Series'>

# [인덱스 커스텀 설정]
obj2 = pd.Series([3, 7, -5, 4], index = ['a','b','c','d'])
print(obj2)
# 판다스 객체는 sum, std(표준편차) 등 통계 함수를 내장하고 있습니다.
print(obj2.sum(), ' ', np.sum(obj2), ' ', sum(obj2))
print(obj2.std())

print(obj2.values)      # 실제 값들만 추출 (결과는 NumPy 배열 형태)
print(obj2.index)       # 인덱스(색인) 정보만 추출
print(obj2['a'])        # 라벨 인덱싱: 'a'라는 이름으로 값을 찾음
print((obj2[['a']]))    # 팬시 인덱싱: 리스트 형태로 넘기면 시리즈 형태로 반환
print(obj2[['a', 'b']]) 
print(obj2['a':'c'])    # 슬라이싱: 'a'부터 'c'까지 (loc 방식처럼 'c'를 포함함)
print(obj2[2])          # 위치 기반 인덱싱 (0부터 시작하는 순서)
print(obj2.iloc[2])     # iloc를 사용하여 명확하게 위치(정수)로 접근
print(obj2[1:4])

print(obj2[[2,1]])      # 위치 번호로 여러 개 선택
print(obj2.iloc[[2,1]]) # iloc 팬시 인덱싱

# [멤버십 확인] 인덱스 명칭이 존재하는지 확인 (값 존재 여부가 아님)
print('a' in obj2)      # True
print('k' in obj2)      # False

print('파이썬 dict 자료를 Series 객체로 생성')
# 딕셔너리의 Key는 인덱스가 되고, Value는 데이터가 됩니다.
names = {'mouse':5000, 'keyboard':25000, 'monitor':450000}
print(names)
obj3 = Series(names)
print(obj3, ' ', type(obj3))   # <class 'pandas.core.series.Series'>
# .index 속성에 리스트를 대입하여 인덱스 이름을 한꺼번에 바꿀 수 있습니다.
obj3.index = ['마우스', '키보드', '모니터'] 
print(obj3, ' ', type(obj3))

# Series 객체 자체에 이름을 부여할 수 있으며, 이는 나중에 DataFrame의 컬럼명이 됩니다.
obj3.name = "상품가격"          
print(obj3)

print('\nDataFrame 객체----------------------')
# Series를 DataFrame으로 변환하면 1개의 컬럼을 가진 표가 됩니다.
df = pd.DataFrame(obj3)
print(df, ' ', type(df))

# [딕셔너리를 이용한 DataFrame 생성]
data = {
    'irum':['홍길동', '한국인', '신기해', '공기밥', '한가해'],
    'juso':('역삼동', '신당동', '역삼동', '역삼동', '신사동'),
    'nai':[23,25,33,23,35]
}
frame = pd.DataFrame(data)
print(frame)

# [컬럼 추출] DataFrame의 각 컬럼은 Series 객체입니다.
print()
print(frame['irum'])    # 딕셔너리 방식으로 컬럼 추출
print(type(frame.irum)) # 속성(Dot) 방식으로 추출 가능

# 생성 시 columns 인자를 주어 컬럼의 배치 순서를 결정할 수 있습니다.
print(DataFrame(data=data, columns=['juso', 'irum', 'nai']))    

# [NaN (결측치) 처리]
# 데이터에 없는 컬럼('tel')을 지정하면 해당 컬럼은 NaN(Not a Number)으로 채워집니다.
frame2 = pd.DataFrame(data, columns=['irum', 'nai', 'juso', 'tel']
                      , index=['a','b','c','d','e'])
print(frame2)   
frame2['tel'] = '111-1111'  # 스칼라 값을 대입하면 모든 행에 동일하게 적용(Broadcasting)
print(frame2)

# 특정 인덱스에만 값을 넣고 싶을 때는 Series를 만들어 대입합니다.
val = pd.Series(['222-2222','333-3333','444-4444'], index = ['b', 'c', 'e'])
print(val)
# 인덱스가 일치하는 'b', 'c', 'e'만 값이 바뀌고 나머지는 NaN이 됩니다.
frame2['tel'] = val
print(frame2)

print()
print(frame2.T)         # .T : 행과 열을 뒤바꿈 (전치)

print()
# .values를 쓰면 순수 데이터(NumPy 배열)만 추출됩니다.
print(frame2.values)    
print(frame2.values[0, 1])  # 2차원 배열 인덱싱으로 접근
print(frame2.values[0:2])   

# [데이터 삭제] 
# .drop()은 원본을 직접 수정하지 않고 삭제된 '복사본'을 반환합니다.
frame3 = frame2.drop('d')           # 기본값 axis=0 (행 삭제)
frame3 = frame2.drop('d', axis = 0) 
print(frame3)
# axis=1을 주면 컬럼(열)을 삭제합니다.
frame4 = frame2.drop('tel', axis = 1)
print(frame4)

print('*'*50)
print(frame2)
# [정렬]
print(frame2.sort_index(axis=0, ascending=False))    # 인덱스(행 이름) 기준 내림차순 정렬
print(frame2.sort_index(axis=1, ascending=True))     # 컬럼(열 이름) 기준 오름차순 정렬

# [순위 매기기]
print(frame2.rank(axis=0))      # 각 컬럼 내에서 값의 크기에 따라 순위를 부여

# [빈도수 계산] 범주형 데이터의 개수를 파악할 때 유용합니다.
counts = frame2['juso'].value_counts()  
print(counts)

# [문자열 데이터 가공] 
# 리스트 컴프리헨션을 사용하여 문자열 컬럼의 내용을 분리(split)하고 재구성합니다.
data = {
    'juso':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon':[23, 25, 15]
}
fr = pd.DataFrame(data)
print(fr)
# 행정구역 정보를 공백 기준 앞부분(시/구)과 뒷부분(동)으로 나누어 새로운 Series 생성
result1 = Series([x.split()[0] for x in fr.juso])   
result2 = Series([x.split()[1] for x in fr.juso])
print(result1)
print(result2)
print(result1.value_counts()) # 분리된 데이터의 빈도수 확인