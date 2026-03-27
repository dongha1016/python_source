# 교차분석 (Chi-Square Test, 카이제곱 검정) 가설검정

# 1. 정의:
#    - 범주형(명목/서열) 변수들 간의 연관성이나 분포의 차이를 분석하는 기법
#    - 관찰된 빈도(Observed Frequency)가 기대 빈도(Expected Frequency)와 의미있게 다른지 검증

# 2. 주요 특징:
#    - 변수는 범주형 자료(Categorical Data)를 대상으로 교차빈도에 대한 기술통계량을 제공
#    - 교차빈도에 대한 통계적 유의성(두 변수 간의 독립성 등)을 검증해 주는 분석기법
#    - 분산이 퍼져 있는 모습을 분포로 만든 것이 카이제곱 분포임

# 3. 수식:
#    - X² = ∑ [ (관측값 - 기대값)² / 기대값 ]
#    - 관측값과 기대값의 차이가 클수록 X² 값이 커지며, 이는 통계적으로 유의할 확률이 높아짐을 의미

# 4. 분석의 종류:
#    - 적합도 검정 (Goodness of Fit): 표본 집단의 분포가 특정 이론적 분포를 따르는지 검정 (일원 카이제곱)
#    - 독립성 검정 (Test of Independence): 두 범주형 변수 사이에 관계가 있는지 검정 (이원 카이제곱)
#    - 동질성 검정 (Test of Homogeneity): 여러 모집단의 범주별 비율이 서로 동일한지 검정 (이원 카이제곱)

# 가설을 채택하는 두가지 방법 연습
import pandas as pd
data = pd.read_csv("pass_cross.csv", encoding="euc-kr")
print(data.head())
print(data.shape)   #(50,4)
print(data.shape[0])
print(data.shape[1])
print()
# 귀무가설(H0) : 벼락치기 공부하는 것과 합격여부는 관계가 없다.
# 대립가설(H1) : 벼락치기 공부하는 것과 합격여부는 관계가 있다.

print(data[(data['공부함']==1) & (data['합격']==1)].shape[0]) 
print(data[(data['공부함']==1) & (data['불합격']==1)].shape[0]) 

print("===============빈도표 작성==================")
ctab = pd.crosstab(index=data['공부안함'], columns=data['불합격'], margins=True) 
ctab.columns = ['합격', '불합격', '행합']
ctab.index = ['공부함', '공부안함', '열합']
print(ctab)
# 기대도수 = (각행의 주변합) * 각열의 주변합 / 총합<전체표본수>

print((18-15) **2 / 15 + (7-10)**2 / 10 + 10 +(12-15)**2 / 15 +(13-10)**2/10)
# chi2 = 3.0
# df = 2 - 1 = 1
# 유의수준 : 0.05
# 임계값 : 3.84
# 판정 : 카이제곱 검정통계량: 3 < 임계값(3.84)이므로 귀무 채택역 내에 있으므로 귀무가설 채택!
# 그러므로 벼락치기 공부하는 것과 합격여부는 관계가 없다. 는 의견 유지

# 검정방법2 : p-value 사용
import scipy.stats as stats 
chi2, p, dof, expected = stats.chi2_contingency(ctab)
print('카이제곱 :', chi2)   # 카이제곱 : 3.0
print('p-value :', p)       # p-value : 0.5578254003710748
print('자유도 :', dof)
print('기대도수 :\n', expected)
# 판정 : 유의수준 0.05 < p:0.557825 이므로 귀무채택
# 검정에 사용된 자료는 우연히 발생한 자료라고 할 수 있다

# chi2 검정 정식명칭 : Pearson's chi-square test
# 두 개의 불연속변수