# Dataframe 재구조화(열을 행으로, 행을 열로 이동)

import pandas as pd
import numpy as np

df = pd.DataFrame(1000 + np.arange(6).reshape(2,3), 
                index = ['대전', '서울'], columns=['2020', '2021', '2022'])
print(df)

# stack, unstack
print()
df_row = df.stack()     # 열을 행으로 변경
print(df_row)

df_col = df_row.unstack() # 행을 열로 이동
print(df_col)

print('\n범주화==================')
# 많은 데이터들을 구간별로 나누기 위함
price = [10.3, 5.5, 7.8, 3.6]
cut = [3, 7, 9, 11]                 # 구간 기준값
result_cut = pd.cut(price, cut)     # 연속형 데이터를 범주화 하는 것
# [(9, 11], (3, 7], (7, 9], (3, 7]]
# (3, 7] => 3초과 7이하인 값임을 의미
# Categories (3, interval[int64, right]): [(3, 7] < (7, 9] < (9, 11]]

print(result_cut)
print(pd.Series(result_cut).value_counts())
# (3, 7]     2
# (7, 9]     1
# (9, 11]    1

print()
datas = pd.Series(np.arange(1, 1001))
print(datas.head(3))                # 앞에 3개만 보기
print(datas.tail(2))                # 뒤에서 2개만 보기

result_cut2 = pd.qcut(datas, 3)     # 3개로 쪼개줘
print(result_cut2) 
print(pd.Series(result_cut2).value_counts())
# (667.0, 1000.0]    334
# (0.999, 334.0]     333
# (334.0, 667.0]     333

print('\nagg함수 : 범주의 그룹별 연산==============')

group_col = datas.groupby(result_cut2, observed=True)  # 3개의 범주
# print(group_col)
print(group_col.agg(['count', 'mean', 'std', 'min'])) # 범주를 만들고 원하는 함수를 넣어줌

print("=========agg 대신 사용자 함수를 작성=========")
def summaryFunc(gr):
    return {'count':gr.count(),
            'mean':gr.mean(),
            'std':gr.std(),
            'min':gr.min(),}
print(group_col.apply(summaryFunc))
print()
print(group_col.apply(summaryFunc).unstack())
#                  count   mean        std    min
# (0.999, 334.0]   333.0  167.0  96.273049    1.0
# (334.0, 667.0]   333.0  500.0  96.273049  334.0
# (667.0, 1000.0]  334.0  833.5  96.561725  667.0


print('\nmerge : 데이터프레임 객체 병합')
df1 = pd.DataFrame({'data1':range(7), 'key':['b','b','a','c','a','a','b']})
print(df1)
df2 = pd.DataFrame({'key':['a','b','d'], 'data2':range(3)})
print(df2)
print()
print(pd.merge(df1, df2, on='key')) # 'key'를 기준으로 교집합(inner join)
print(pd.merge(df1, df2, on='key', how='inner')) # 'key'를 기준으로 교집합(inner join)
print(pd.merge(df1, df2, on='key', how='outer')) 
# 'key'를 기준으로 교집합(full outer join)
#    data1 key  data2
# 0    2.0   a    0.0
# 1    4.0   a    0.0
# 2    5.0   a    0.0
# 3    0.0   b    1.0
# 4    1.0   b    1.0
# 5    6.0   b    1.0
# 6    3.0   c    NaN

print(pd.merge(df1, df2, on='key', how='left')) # left outer join
print(pd.merge(df1, df2, on='key', how='right')) # right outer join

print()
print("\n 공통 컬럼명이 없는 경우 : df1 vs df3")
df3 = pd.DataFrame({'key2':['a', 'b', 'd'], 'data2':range(3)})
print(df3)
print(df1)
#  공통 컬럼명이 없는 경우 : df1 vs df3
#   key2  data2
# 0    a      0
# 1    b      1
# 2    d      2
#    data1 key
# 0      0   b
# 1      1   b
# 2      2   a
# 3      3   c
# 4      4   a
# 5      5   a
# 6      6   b
print(pd.merge(df1, df3, left_on='key', right_on='key2'))   # inner join
print('====================concat===================')
print(pd.concat([df1, df3], axis=0))                        # 행단위
print(pd.concat([df1, df3], axis=1))                        # 열단위

print('\n\npivot_table : pivot과 groupby 명령의 중간적 성격')
# pivot : 데이터 열 중에서 두 개의 열(key)을 사용해 데이터의 행렬을 재구성
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
print(df.set_index(['city', 'year']).unstack())     # set_index : 기존 행 인덱스를 제거하고 첫번째 열 인덱스 설정

print()
print(df['pop'].describe())
print("여기서부터 볼까나")
print(df.pivot_table(index=['city'], aggfunc='mean'))  # aggfunc를 안쓰면 default는 mean
print(df.pivot_table(index=['city', 'year'], aggfunc=[len, 'mean']))  
print(df.pivot_table(values='pop', index='city'))  
print(df.pivot_table(values='pop', index='city', aggfunc=len))  
print()
print(df.pivot_table(values='pop', index=['year'], columns=['city']))  
print(df.pivot_table(values='pop', index=['year'], columns=['city'], margins=True, fill_value=0))  
# 행에 대한 평균
print()
hap = df.groupby(['city'])
print(hap)
print(hap.sum())
print(df.groupby(['city']).sum())
print(df.groupby(['city']).mean())