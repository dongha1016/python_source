# 표준편차(Standard Deviation)와 분산(Variance)의 중요성 이해
# - 두 집단의 평균이 같더라도 데이터가 퍼진 정도(산포도)에 따라 집단의 특성이 완전히 다를 수 있음을 확인
# - 분산: 관측값에서 평균을 뺀 값을 제곱하고, 그것을 모두 더한 후 전체 개수로 나눈 값
# - 표준편차: 분산의 제곱근 (원래 데이터와 단위가 일치하여 해석이 용이함)

# 가설 검정의 기초:
# - 귀무가설(H0): 차이가 없다 (기존의 상태 유지)
# - 대립가설(H1): 차이가 있다 (새로운 주장, 증명하고 싶은 내용)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

np.random.seed(42)

# 목표 평균
target_mean = 60
std_dev_small = 10
std_dev_large = 20

# 데이터 생성
# np.random.normal(평균, 표준편차, 개수): 정규분포를 따르는 난수 생성
class1_raw = np.random.normal(loc = target_mean, scale = std_dev_small, size = 100) 
class2_raw = np.random.normal(loc = target_mean, scale = std_dev_large, size = 100) 

print(class1_raw[:5])
# 평균 보정: 난수 생성 시 발생하는 미세한 평균 차이를 제거하여 두 집단의 평균을 정확히 target_mean으로 맞춤
class1_adj = class1_raw - np.mean(class1_raw) + target_mean
print(class1_adj[:5])
class2_adj = class2_raw - np.mean(class2_raw) + target_mean
print(class2_adj[:5])

# 정수화
# np.clip(배열, 최소값, 최대값): 범위를 벗어나는 값을 최소/최대값으로 제한 (점수이므로 10~100점 사이로 제한)
class1 = np.clip(np.round(class1_adj), 10, 100).astype(int)
print(class1[:10])
class2 = np.clip(np.round(class2_adj), 10, 100).astype(int)
print(class2[:10])

# 통계 계산
mean1, mean2 = np.mean(class1), np.mean(class2)
std1, std2 = np.std(class1), np.std(class2)
var1, var2 = np.var(class1), np.var(class2)

print("1반(성적 편차가 작음)")
print(f"평균 : {mean1}, 표준편차 : {std1}, 분산 : {var1}")
print("2반(성적 편차가 큼)")
print(f"평균 : {mean2}, 표준편차 : {std2}, 분산 : {var2}")

# 분석용 DataFrame 생성 및 CSV 저장
df = pd.DataFrame({
    'class':['1반'] * 100 + ['2반'] * 100,
    'score':np.concatenate([class1, class2])
})
print(df.head())
df.to_csv('test1vari.csv', index = False, encoding = 'utf-8-sig')


print("====================시각화====================")
x1 = np.random.normal(1, 0.05, size = 100)
x2 = np.random.normal(2, 0.05, size = 100)
plt.figure(figsize=(10, 6))
plt.scatter(x1, class1, alpha = 0.8, label = f'1반(평균={mean1:.2f}, 표준편차={std1:.2f}, 분산={var1:.2f})')
plt.scatter(x2, class2, alpha = 0.8, label = f'2반(평균={mean2:.2f}, 표준편차={std2:.2f}, 분산={var2:.2f})')
plt.hlines(target_mean, 0.5, 2.5, colors='red', 
            linestyles='dashed', label=f'공통 평균={target_mean}')
plt.xticks([1,2], ['1반', '2반'])
plt.ylabel('시험 점수')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 박스플롯: 데이터의 사분위수와 이상치를 한눈에 파악 (상자의 세로 길이가 길수록 편차가 큼)
plt.figure(figsize=(8,5))
plt.boxplot([class1, class2], labels = ['1반', '2반'])
plt.grid(True)
plt.show()

# 히스토그램: 데이터의 분포 모양 확인 (1반은 평균에 밀집, 2반은 넓게 퍼진 형태)
plt.figure(figsize=(10,6))
plt.hist(class1, bins=15, label='1반', alpha=0.6, edgecolor='black')
plt.hist(class2, bins=15, label='2반', alpha=0.6, edgecolor='blue')
plt.axvline(target_mean, color='red', 
            linestyle='dotted', linewidth=2, label=f'공통 평균: {target_mean}')
plt.xlabel('시험 점수')
plt.ylabel('빈도')
plt.legend()
plt.grid(True)
plt.show()

# 국어 선생님 입장 
# 귀무가설(전통적 주장) : 두 반의 국어 점수의 표준편차(평균)는 차이가 없다
# 누군가가 실험을 통해 데이터 수집 후 두 반의 점수에 통계 계싼 후 새로운 주장(의견)
# 대립가설 : 두 반의 국어 점수의 표준편차(평균)는 차이가 있다
