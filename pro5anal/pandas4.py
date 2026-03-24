# Dataframe 재구조화(열을 행으로, 행을 열로 이동)

import pandas as pd
import numpy as np

# 2행 3열의 샘플 데이터프레임 생성
df = pd.DataFrame(1000 + np.arange(6).reshape(2,3), 
                index = ['대전', '서울'], columns=['2020', '2021', '2022'])
print(df)

# [stack, unstack]
# stack: 컬럼(열) 인덱스를 로우(행) 인덱스로 내려서 '길게' 만듭니다. (세로로 쌓임)
print()
df_row = df.stack()     # 열을 행으로 변경
print(df_row)

# unstack: 로우 인덱스를 컬럼 인덱스로 올려서 '넓게' 만듭니다. (가로로 펼쳐짐)
df_col = df_row.unstack() # 행을 열로 이동
print(df_col)

print('\n범주화==================')
# 많은 데이터들을 특정 구간(Bin)별로 나누어 그룹화할 때 사용합니다.
price = [10.3, 5.5, 7.8, 3.6]
cut = [3, 7, 9, 11]                 # 구간 경계값 설정
# pd.cut: 값의 크기를 기준으로 구간을 나눕니다. (절대평가 방식)
result_cut = pd.cut(price, cut)     # 연속형 데이터를 범주형(Category)으로 변환
# (3, 7] => 3 < x <= 7 (3 초과 7 이하)를 의미하는 수학적 기호입니다.

print(result_cut)
print(pd.Series(result_cut).value_counts()) # 각 구간에 몇 개의 데이터가 포함되었는지 확인

print()
datas = pd.Series(np.arange(1, 1001))
print(datas.head(3))                # 상위 데이터 미리보기
print(datas.tail(2))                # 하위 데이터 미리보기

# pd.qcut: 데이터의 개수를 기준으로 구간을 나눕니다. (상대평가/분위수 방식)
result_cut2 = pd.qcut(datas, 3)     # 데이터를 개수가 동일하게 3개 그룹으로 쪼갬
print(result_cut2) 
print(pd.Series(result_cut2).value_counts())

print('\nagg함수 : 범주의 그룹별 연산==============')

# groupby: 특정 기준(여기서는 범주화된 구간)으로 데이터를 그룹 묶음
group_col = datas.groupby(result_cut2, observed=True)  
# .agg(): 여러 개의 통계 함수를 리스트 형태로 전달하여 한꺼번에 계산함
print(group_col.agg(['count', 'mean', 'std', 'min'])) 

print("=========agg 대신 사용자 함수를 작성=========")
# 사용자가 직접 정의한 함수를 통해 그룹별 요약 통계를 커스텀할 수 있습니다.
def summaryFunc(gr):
    return {'count':gr.count(),
            'mean':gr.mean(),
            'std':gr.std(),
            'min':gr.min(),}

# .apply(): 그룹별로 사용자 정의 함수를 적용함
print(group_col.apply(summaryFunc))
print()
# apply 결과가 딕셔너리 형태일 때 unstack()을 하면 표 형태로 깔끔하게 정리됩니다.
print(group_col.apply(summaryFunc).unstack())


print('\nmerge : 데이터프레임 객체 병합')
# SQL의 JOIN과 유사하게 특정 '키(Key)'를 기준으로 두 표를 합칩니다.
df1 = pd.DataFrame({'data1':range(7), 'key':['b','b','a','c','a','a','b']})
print(df1)
df2 = pd.DataFrame({'key':['a','b','d'], 'data2':range(3)})
print(df2)
print()
# how='inner': 양쪽 표에 모두 존재하는 키값만 합침 (교집합)
print(pd.merge(df1, df2, on='key')) 
print(pd.merge(df1, df2, on='key', how='inner')) 
# how='outer': 한쪽에만 있어도 모두 합치고, 없는 값은 NaN 처리 (합집합)
print(pd.merge(df1, df2, on='key', how='outer')) 

# how='left': 왼쪽 표(df1)를 기준으로 합침
print(pd.merge(df1, df2, on='key', how='left')) 
# how='right': 오른쪽 표(df2)를 기준으로 합침
print(pd.merge(df1, df2, on='key', how='right')) 

print()
print("\n 공통 컬럼명이 없는 경우 : df1 vs df3")
df3 = pd.DataFrame({'key2':['a', 'b', 'd'], 'data2':range(3)})
print(df3)
print(df1)
# 컬럼명이 다를 때는 left_on과 right_on으로 매칭될 기준을 각각 지정합니다.
print(pd.merge(df1, df3, left_on='key', right_on='key2'))   # inner join

print('====================concat===================')
# merge가 '키' 중심의 병합이라면, concat은 단순히 물리적으로 '이어 붙이기'입니다.
print(pd.concat([df1, df3], axis=0))                        # 위+아래로 붙이기 (행단위)
print(pd.concat([df1, df3], axis=1))                        # 왼쪽+오른쪽으로 붙이기 (열단위)

print('\n\npivot_table : pivot과 groupby 명령의 중간적 성격')
# pivot: 중복된 키가 없는 경우 데이터를 재구조화할 때 사용
data = {
        'city':['강남', '강북', '강남', '강북'],
        'year':[2000, 2001, 2002, 2002],
        "pop":[3.3, 2.5, 3.0, 2.0]
    }
df = pd.DataFrame(data)
print(df)
print()
print(df.pivot(index='city', columns='year', values='pop'))
print(df.pivot(index='year', columns='city', values='pop'))
print()
# set_index와 unstack을 조합하면 pivot과 동일한 효과를 낼 수 있습니다.
print(df.set_index(['city', 'year']).unstack()) 

print()
print(df['pop'].describe()) # 기본적인 기술 통계값 확인
print("여기서부터 볼까나")
# pivot_table: 데이터에 중복된 키가 있어도 통계치(aggfunc)를 내며 요약할 수 있습니다.
print(df.pivot_table(index=['city'], aggfunc='mean'))  # 도시별 인구 평균
print(df.pivot_table(index=['city', 'year'], aggfunc=[len, 'mean'])) # 빈도와 평균 동시 계산
print(df.pivot_table(values='pop', index='city'))  
print(df.pivot_table(values='pop', index='city', aggfunc=len)) # aggfunc=len은 개수 확인
print()
# margins=True: 행과 열의 총합(All)을 추가해주는 편리한 옵션입니다.
print(df.pivot_table(values='pop', index=['year'], columns=['city'], margins=True, fill_value=0))  

print()
# groupby 연산: 특정 컬럼을 기준으로 그룹을 나누고 집계함수를 적용합니다.
hap = df.groupby(['city'])
print(hap)
print(hap.sum()) # 도시별 합계
print(df.groupby(['city']).sum())
print(df.groupby(['city']).mean()) # 도시별 평균