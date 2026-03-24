# 자전거 공유 시스템 분석용
# : kaggle 사이트의 Bike Sharing in Washington D.C. Dataset를 편의상 조금 변경한 dataset을 사용함

# [주요 컬럼 정보]
# 'datetime': 날짜와 시간
# 'season': 사계절(1:봄, 2:여름, 3:가을, 4:겨울)
# 'holiday': 공휴일(1), 평일(0)
# 'workingday': 근무일(1), 주말/휴일(0)
# 'weather': 날씨 상태(1:맑음 ~ 4:폭우/폭설)
# 'temp': 섭씨온도, 'atemp': 체감온도, 'humidity': 습도, 'windspeed': 풍속
# 'casual': 비회원 대여량, 'registered': 회원 대여량, 'count': 총 대여량(타겟 변수)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
from scipy import stats

# plt.style.use('ggplot'): 그래프의 스타일을 R의 ggplot 라이브러리 형식으로 설정 (격자와 배경색 등)
plt.style.use('ggplot')

# [데이터 로드] parse_dates: 특정 컬럼('datetime')을 문자열이 아닌 날짜 시간(datetime) 타입으로 읽어옴
train = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/data/train.csv", parse_dates=['datetime'])

# EDA : 탐색적 분석 (데이터의 특징을 파악하는 과정)
# pd.set_option('display.width', None): 데이터 출력 시 줄바꿈 없이 한 줄에 모든 컬럼이 보이도록 설정
pd.set_option('display.width', None)

print(train.info())             # 데이터 타입 및 결측치 여부 요약
print(train.dtypes)             # 각 컬럼의 데이터 타입 확인
print(train.shape)              # (행, 열) 크기 확인 -> (10886, 12)
print(train.columns)            # 컬럼명 리스트 확인
print(train.head(3))            # 데이터 상단 3개 행 확인
print(train.temp.describe())    # 온도(temp) 컬럼의 기초 통계량(평균, 편차, 사분위수 등) 확인
print(train.isnull().sum())     # 데이터 내에 비어있는 값(결측치)이 있는지 확인 (현재 모두 0)

# --- 1. 날짜 데이터 분해 (Feature Engineering) ---
# .dt 연산자: datetime 타입 컬럼에서 연, 월, 일, 시 등을 개별적으로 추출하여 새로운 컬럼 생성
train['year'] = train['datetime'].dt.year 
train['month'] = train['datetime'].dt.month    
train['day'] = train['datetime'].dt.day       
train['hour'] = train['datetime'].dt.hour     
train['minute'] = train['datetime'].dt.minute 
train['second'] = train['datetime'].dt.second 

print(train.head(1))
print(train.columns)

print("=============== 2. 대여량 시각화 (Bar Plot) ===============")
# 1행 4열 구조의 서브플롯 생성
figure, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=4)
figure.set_size_inches(15, 5) # 전체 도화지 크기 설정

# sns.barplot: x축 범주에 따른 y축 값의 평균과 신뢰구간을 막대 그래프로 표시
sns.barplot(data=train, x='year', y='count', ax=ax1)        # 연도별 평균 대여수
sns.barplot(data=train, x='month', y='count', ax=ax2)       # 월별 평균 대여수
sns.barplot(data=train, x='day', y='count', ax=ax3)         # 일별 평균 대여수 (19일까지 데이터만 있음을 확인 가능)
sns.barplot(data=train, x='hour', y='count', ax=ax4)        # 시간별 평균 대여수 (출퇴근 시간대 증가 확인)

# 각 그래프의 제목과 축 레이블 설정
ax1.set(ylabel='대여수', title = '연도별 대여')
ax2.set(ylabel='월', title = '월별 대여')
ax3.set(ylabel='일', title = '일별 대여')
ax4.set(ylabel='시간', title = '시간별 대여')
plt.show()

print("=============== 3. 분포와 범주별 차이 시각화 (Box Plot) ===============")
# 2행 2열 구조로 데이터의 분포와 이상치 확인
fig, axes = plt.subplots(nrows=2, ncols=2)
# 주의: 앞에서 figure를 선언했으므로 fig 또는 plt.gcf().set_size_inches()를 사용하거나 새로 설정 필요
plt.gcf().set_size_inches(12, 10) 

# sns.boxplot: 데이터의 중앙값, 사분위수 및 이상치 시각화
# orient="v": 세로(Vertical) 방향으로 그림
sns.boxplot(data=train, y="count", orient="v", ax = axes[0][0])                # 전체 대여량 분포
sns.boxplot(data=train, y="count", x="season", orient="v", ax = axes[0][1])   # 계절별 차이
sns.boxplot(data=train, y="count", x="hour", orient="v", ax = axes[1][0])     # 시간대별 차이
sns.boxplot(data=train, y="count", x="workingday", orient="v", ax = axes[1][1]) # 근무일 여부별 차이

axes[0][0].set(ylabel='대여수', title='전체 대여량 분포')
axes[0][1].set(xlabel='계절', ylabel ='대여수', title='계절별 대여량')
axes[1][0].set(xlabel='시간', ylabel ='대여수', title='시간별 대여량')
axes[1][1].set(xlabel='근무일', ylabel ='대여수', title='근무일에 따른 대여량')
plt.show()

print("=============== 4. 연속형 변수와의 상관관계 (Regplot) ===============")
# sns.regplot: 산점도에 회귀선(Regression line)을 함께 그려 변수 간의 선형적 관계 파악
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3)
plt.gcf().set_size_inches(12, 5)

sns.regplot(x='temp', y='count', data=train, ax=ax1)       # 온도가 높을수록 대여량 증가 경향
sns.regplot(x='humidity', y='count', data=train, ax=ax2)   # 습도가 낮을수록 대여량 증가 경향
sns.regplot(x='windspeed', y='count', data=train, ax=ax3)  # 풍속과 대여량의 관계 (0에 몰린 데이터 확인 필요)
plt.show()