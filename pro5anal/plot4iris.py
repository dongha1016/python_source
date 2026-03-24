# iris dataset : 150행, 3가지 종류, 4개의 특성
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline    # Jupyter Notebook 환경에서 그래프를 즉시 출력하기 위한 매직 명령어

# [데이터 로드] 웹상에 저장된 CSV 파일을 pandas DataFrame으로 읽어오기
iris_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/iris.csv")
print(iris_data.info())     # 데이터프레임의 요약 정보(데이터 타입, 결측치 등) 확인
print(iris_data.head(3))    # 상위 3개 행 출력
print(iris_data.tail(3))    # 하위 3개 행 출력

# --- 1. 기본 산점도 (Scatter Plot) ---
# 두 변수(꽃받침 길이, 꽃잎 길이) 사이의 관계를 점으로 표시
plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'])
plt.xlabel('Sepal.Length')
plt.ylabel('Petal.Length')
plt.title('iris data')
plt.show()

print()
# iris_data['Species'].unique(): 중복을 제거한 꽃의 종류 확인
print(iris_data['Species'].unique())        # ['setosa' 'versicolor' 'virginica']
print(set(iris_data['Species']))            # 파이썬 기본 자료구조 set을 활용한 중복 제거

# --- 2. 범주별 색상 할당 산점도 ---
cols = []       # 꽃의 종류에 따라 서로 다른 숫자(색상 코드)를 저장할 리스트

# 반복문을 통해 꽃의 종(Species)에 따라 1, 2, 3의 값을 할당
for s in iris_data['Species']:
    choice = 0
    if s == 'setosa': choice = 1
    elif s == 'versicolor': choice = 2
    elif s == 'virginica': choice = 3
    cols.append(choice)

# c=cols: 위에서 생성한 리스트를 기반으로 점들의 색상을 다르게 지정
plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'], c=cols)
plt.xlabel('Sepal.Length')
plt.ylabel('Petal.Length')
plt.title('iris data')
plt.show()

print("==========Pandas의 시각화 기능===========")
from pandas.plotting import scatter_matrix
# .loc을 사용하여 수치형 데이터가 들어있는 컬럼들만 슬라이싱 추출
iris_col = iris_data.loc[:, 'Sepal.Length':'Petal.Width']

# scatter_matrix: 모든 변수 쌍 사이의 산점도를 행렬 형태로 그림
# diagonal='kde': 대각선 영역(자기 자신과의 관계)에 밀도 추정 곡선(Kernel Density Estimation)을 표시
scatter_matrix(iris_col, diagonal='kde')
plt.show()

# --- 3. Seaborn을 활용한 정밀 시각화 ---
import seaborn as sns 
# sns.pairplot: 모든 변수의 조합에 대한 산점도를 그리며, hue 옵션으로 데이터의 종별 색상을 자동 지정
# height=2: 각 서브플롯의 크기(인치) 설정
sns.pairplot(iris_data, hue='Species', height=2)
plt.show()