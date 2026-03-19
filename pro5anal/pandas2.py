# 재색인
from pandas import Series, DataFrame

# Series의 재색인
data = Series([1, 3, 2], index = (1, 4, 2))
print(data)
data2 = data.reindex((1,2,4))
print(data2)

print('\n재색인할 때 값 채워넣기')
data3 = data2.reindex([0,1,2,3,4,5])    # 0, 3, 5번째는 결측치
print(data3)

# 대응값이 없는 index(결측치)에는 특정값으로 채움
data3 = data2.reindex([0,1,2,3,4,5], fill_value=777)    # 결측치를 777로 채워넣기
print(data3)

# 0    NaN
# 1    1.0
# 2    2.0
# 3    NaN
# 4    3.0
# 5    NaN

print()
# NaN 앞 값으로 NaN을 채움
data3 = data2.reindex([0,1,2,3,4,5], method='ffill') 
print(data3)
data3 = data2.reindex([0,1,2,3,4,5], method='pad')   
print(data3)
# 0    NaN => 앞에 참고할 것이 없기 때문에 NaN
# 1    1.0
# 2    2.0
# 3    2.0
# 4    3.0
# 5    3.0

# NaN 뒤(다음) 값으로 NaN을 채움
data3 = data2.reindex([0,1,2,3,4,5], method='bfill') 
print(data3)
data3 = data2.reindex([0,1,2,3,4,5], method='backfill')   
print(data3)

import numpy as np
print('\nDataFrame : bool 처리')
df = DataFrame(np.arange(12).reshape(4,3),
                index = ['1월', '2월', '3월', '4월'],
                columns = ['강남', '강북', '서초'])
print(df['강남'])
print(df['강남'] > 3)
print(df[df['강남']>3])

print(df < 3)
df[df < 3]=0
print(df)

print("\n 슬라이싱 관련 메소드 : loc() => 라벨 지원, iloc() => 숫자지원")
print(df.loc['3월', :])
print(df.loc[:'2월'])
print(df.loc[:'2월', ['서초']])

print()
print(df.iloc[2])
print(df.iloc[2,:]) # 2행의 모든 열

print(df.iloc[:3])
print(df.iloc[:3, 2]) # 2열에 대해서만
print(df.iloc[:3, 1:3]) # 2열에 대해서만