# 재색인 (Reindexing): 기존 데이터를 유지하며 새로운 인덱스 구조로 재배치하는 기능
from pandas import Series, DataFrame

# Series의 재색인
data = Series([1, 3, 2], index = (1, 4, 2))
print(data)
# reindex는 기존 인덱스와 데이터의 '짝'을 기억한 상태에서 새로운 순서(1->2->4)로 나열합니다.
data2 = data.reindex((1,2,4)) # 원래 (1, 4, 2) 순서를 (1, 2, 4) 순서로 변경
print(data2)

print('\n재색인할 때 값 채워넣기')
# [인덱스 확장] 기존에 없던 번호(0, 3, 5)를 넣으면 판다스는 "가져올 값이 없다"고 판단해 NaN을 넣습니다.
data3 = data2.reindex([0,1,2,3,4,5])    # 0, 3, 5번째는 결측치
print(data3)

# 대응값이 없는 index(결측치)에는 특정값으로 채움
# 데이터의 성격에 따라 0이나 특정 숫자로 초기화해야 할 때 fill_value가 유용합니다.
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
# ffill(forward fill): 데이터가 시간 순서일 때 "가장 최근의 유효한 값"을 그대로 유지하려는 논리입니다.
data3 = data2.reindex([0,1,2,3,4,5], method='ffill') 
print(data3)
data3 = data2.reindex([0,1,2,3,4,5], method='pad')   
print(data3)
# 0    NaN => 0번 인덱스 앞에 참고할 '과거 데이터'가 없으므로 채울 수 없음
# 1    1.0
# 2    2.0
# 3    2.0 => 직전 인덱스인 2번의 값(2.0)을 복사해서 채움
# 4    3.0
# 5    3.0 => 직전 인덱스인 4번의 값(3.0)을 복사해서 채움

# [보간법: 뒤의 값으로 채우기]
# bfill(backward fill): 비어있는 자리를 "미래에 나타날 값"으로 미리 채우는 논리입니다.
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
# [조건식 추출] 비교 연산자를 사용하면 요소별로 True/False를 판별한 Series를 만듭니다.
print(df['강남'] > 3)
# [필터링] 대괄호 안에 True/False Series를 넣으면 True인 행만 필터링되어 출력됩니다.
print(df[df['강남']>3])

# [데이터 일괄 수정] 전체 표에서 특정 조건(3 미만)을 만족하는 모든 칸을 0으로 덮어씁니다.
print(df < 3)
df[df < 3]=0 # 이상치 제어나 특정 기준치 이하를 제거할 때 매우 효율적임
print(df)

print("\n 슬라이싱 관련 메소드 : loc() => 라벨 지원, iloc() => 숫자지원")
# [loc: 명칭 기반] 사람이 보고 읽는 인덱스/컬럼 이름을 그대로 사용합니다.
print(df.loc['3월', :]) # '3월' 행의 모든 열 선택
print(df.loc[:'2월'])   # 처음부터 '2월'까지 (이름 기반 슬라이싱은 마지막 항목을 '포함'함)
print(df.loc[:'2월', ['서초']]) # 행 범위와 특정 컬럼명을 조합

print()
# [iloc: 위치 기반] 이름이 무엇이든 상관없이 컴퓨터가 매긴 '순서 번호'로 접근합니다.
print(df.iloc[2])    # 3번째 줄(index 2) 데이터 추출
print(df.iloc[2,:])  # 위와 동일 (행 전체 의미)

# [iloc 슬라이싱 주의점] 파이썬 리스트 규칙을 따르므로 마지막 번호는 '포함하지 않음'
print(df.iloc[:3])      # 0, 1, 2번 행만 출력 (3번 행 제외)
print(df.iloc[:3, 2])   # 0~2번 행의 3번째 열(index 2) 데이터 추출
print(df.iloc[:3, 1:3]) # 0~2번 행의 2번째(index 1)부터 3번째(index 2) 열까지 추출