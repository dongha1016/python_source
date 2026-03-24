print("=============seaborn : Matplotlib의 기능 보충용=============")

# [환경 설정] koreanize-matplotlib: 한글 폰트 설정을 단 한 줄로 해결해주는 라이브러리
# pip install koreanize-matplotlib
import koreanize_matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn 내장 예제 데이터셋 'titanic' 로드
titanic = sns.load_dataset("titanic")

# 데이터 구조 확인 (max_cols=None은 모든 컬럼 정보를 생략 없이 출력함)
print(titanic.info(max_cols=None))

# sns.displot: 데이터의 분포(Distribution)를 시각화 (히스토그램 등)
sns.displot(titanic['age'])
plt.title("나이차트")
plt.show()

# sns.boxplot: y축 기준으로 'age' 데이터의 분포와 이상치 확인
# palette: 그래프의 색상 테마 설정
sns.boxplot(y='age', data=titanic, palette="Paired")
plt.show()

# sns.relplot: 관계형(Relationship) 그래프, 성별(x)과 나이(y)의 분포 확인
sns.relplot(x='sex', y ='age', data=titanic)
plt.show()

# 히트맵(Heatmap)을 그리기 위한 데이터 재구성 (피벗 테이블 생성)
# index: 행, columns: 열, aggfunc='size': 각 그룹별 데이터 개수 산출
titanic_pivot = titanic.pivot_table(index='class', columns='sex', aggfunc='size')
print(titanic_pivot)

# sns.heatmap: 수치 데이터를 색상으로 시각화
# cmap: 색상 지도, annot=True: 칸 안에 숫자 표시, fmt="d": 정수형 포맷
sns.heatmap(titanic_pivot, cmap=sns.light_palette("gray"), annot=True, fmt="d")
plt.show()


import pandas as pd

print("=============# 1. 데이터 정의=============")
# 100이라는 극단적인 이상치가 포함된 리스트 데이터
data = [10, 12, 13, 15, 14, 12, 11, 100]
df = pd.DataFrame({'score': data})

print("=============# 2. IQR 기반 이상치 탐지=============")
# IQR(Interquartile Range) 방식: 사분위수를 이용한 통계적 이상치 판별
Q1 = df['score'].quantile(0.25) # 1사분위수 (25% 지점)
Q3 = df['score'].quantile(0.75) # 3사분위수 (75% 지점)
IQR = Q3 - Q1                   # 사분위 범위 (가운데 50%의 폭)

# 정상 범위를 결정하는 경계값 산출 (일반적으로 1.5배수 적용)
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("=============# 3. 이상치, 정상치 분리=============")
# 불리언 인덱싱을 활용하여 이상치와 정상 데이터를 각각 추출
outliers = df[(df['score'] < lower_bound) | (df['score'] > upper_bound)]
filtered_df = df[(df['score'] >= lower_bound) & (df['score'] <= upper_bound)]

print("=============# 4. 이상치 출력=============")
print("이상치 값:")
print(outliers)

print("=============# 5. 박스플롯 시각화: 제거 전/후 비교=============")
# 1행 2열 구조의 서브플롯 생성
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# [왼쪽 그래프] 이상치 포함 전체 데이터
# ax=axes[0]: 첫 번째 영역에 그림 지정
sns.boxplot(y=df['score'], ax=axes[0], color='salmon')
axes[0].set_title('이상치 포함 데이터')
axes[0].set_ylabel('Score')
axes[0].grid(True)

# [오른쪽 그래프] 이상치가 제거된 필터링 데이터
# ax=axes[1]: 두 번째 영역에 그림 지정
sns.boxplot(y=filtered_df['score'], ax=axes[1], color='lightblue')
axes[1].set_title('이상치 제거 후')
axes[1].set_ylabel('Score')
axes[1].grid(True)

# plt.tight_layout(): 그래프 간의 겹침을 방지하고 여백 조정
plt.tight_layout()
plt.show()