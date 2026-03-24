# 재색인 (Reindexing): 기존 데이터를 유지하며 새로운 인덱스 구조로 재배치하는 기능
from pandas import Series, DataFrame

# Series의 재색인
data = Series([1, 3, 2], index = (1, 4, 2))
print(data)
# reindex는 데이터를 삭제하는 것이 아니라, 새로운 순서로 인덱스를 '재배열'합니다.
data2 = data.reindex((1,2,4)) # 원래 (1, 4, 2) 순서를 (1, 2, 4) 순서로 변경
print(data2)

print('\n재색인할 때 값 채워넣기')
# 기존에 없던 인덱스(0, 3, 5)를 추가하면 해당 칸은 기본적으로 NaN(결측치)이 됩니다.
data3 = data2.reindex([0,1,2,3,4,5])    # 0, 3, 5번째는 결측치
print(data3)

# 대응값이 없는 index(결측치)에는 특정값으로 채움
# fill_value 옵션을 사용하면 NaN 대신 지정한 상수로 초기화할 수 있습니다.
data3 = data2.reindex([0,1,2,3,4,5], fill_value=777)    # 결측치를 777로 채워넣기
print(data3)

# 0    NaN
# 1    1.0
# 2    2.0
# 3    NaN
# 4    3.0
# 5    NaN

print()
# [보간법: 앞의 값으로 채우기]
# ffill (forward fill) 또는 pad는 비어있는 칸을 바로 '직전'에 위치한 유효한 값으로 채웁니다.
data3 = data2.reindex([0,1,2,3,4,5], method='ffill') 
print(data3)
data3 = data2.reindex([0,1,2,3,4,5], method='pad')   
print(data3)
# 0    NaN => 0번 인덱스 앞에는 참고할 데이터가 전혀 없기 때문에 그대로 NaN
# 1    1.0
# 2    2.0
# 3    2.0 => 2번 인덱스의 값인 2.0을 끌어와서 채움
# 4    3.0
# 5    3.0 => 4번 인덱스의 값인 3.0을 끌어와서 채움

# [보간법: 뒤의 값으로 채우기]
# bfill (backward fill) 또는 backfill은 비어있는 칸을 바로 '다음'에 올 유효한 값으로 미리 채웁니다.
data3 = data2.reindex([0,1,2,3,4,5], method='bfill') 
print(data3)
data3 = data2.reindex([0,1,2,3,4,5], method='backfill')   
print(data3)

import numpy as np
print('\nDataFrame : bool 처리 (필터링)')
# 4행 3열의 0~11 숫자가 담긴 데이터프레임 생성
df = DataFrame(np.arange(12).reshape(4,3),
                index = ['1월', '2월', '3월', '4월'],
                columns = ['강남', '강북', '서초'])
print(df['강남'])
# 불리언 마스크 생성: 조건에 맞으면 True, 아니면 False인 표를 만듭니다.
print(df['강남'] > 3)
# 불리럭 인덱싱: True인 행들만 골라내어 새로운 데이터프레임을 반환합니다.
print(df[df['강남']>3])

# 데이터프레임 전체에 조건을 걸어 특정값 이하인 요소를 한꺼번에 변경할 수 있습니다.
print(df < 3)
df[df < 3]=0 # 3보다 작은 값(0, 1, 2)을 모두 0으로 일괄 수정
print(df)

print("\n 슬라이싱 관련 메소드 : loc() => 라벨 지원, iloc() => 숫자지원")
# loc[행 이름, 열 이름] 방식
print(df.loc['3월', :]) # '3월' 행의 모든 열 데이터 출력
print(df.loc[:'2월'])   # 처음부터 '2월' 행까지 출력 (라벨 슬라이싱은 '2월'을 포함함)
print(df.loc[:'2월', ['서초']]) # 처음부터 '2월'까지 중 '서초' 컬럼만 출력

print()
# iloc[행 번호, 열 번호] 방식 (0부터 시작하는 순서 기반)
print(df.iloc[2])    # 3번째 행(인덱스 2) 출력
print(df.iloc[2,:])  # 2행의 모든 열 (위와 동일한 결과)

# 숫자 기반 슬라이싱은 파이썬 리스트처럼 마지막 번호를 '포함하지 않음'
print(df.iloc[:3])      # 0, 1, 2번 행 출력 (3번은 제외)
print(df.iloc[:3, 2])   # 0~2번 행의 2번 열(서초) 데이터만 출력
print(df.iloc[:3, 1:3]) # 0~2번 행의 1번(강북)부터 2번(서초) 열까지 출력