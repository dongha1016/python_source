# 차트 영역 객체 선언시 인터페이스 유형 두가지

import numpy as np
import matplotlib.pyplot as plt

print("=========== 1) Matplotlib 스타일의 인터페이스 ============")
# 상태 기반(State-based) 인터페이스: plt 함수를 직접 호출하여 현재 활성화된 '상태'에 그림을 그림
x = np.arange(10)
plt.figure()
plt.subplot(2,1,1)          # row, column, panel number (2행 1열의 첫 번째 영역)
plt.plot(x, np.sin(x))
plt.subplot(2,1,2)          # 2행 1열의 두 번째 영역
plt.plot(x, np.cos(x))
plt.show()

print("=========== 2) 객체 지향 인터페이스 ============")
# 객체 지향(Object-oriented) 인터페이스: Figure와 Axes 객체를 명시적으로 생성하고 변수에 할당하여 제어
fig, ax = plt.subplots(nrows=2, ncols=1) # fig(전체 도화지), ax(각 개별 그래프 영역 리스트) 생성
ax[0].plot(x, np.sin(x))                 # 첫 번째(0번 인덱스) 영역에 그림
ax[1].plot(x, np.cos(x))                 # 두 번째(1번 인덱스) 영역에 그림
plt.show()

# 차트의 종류 일부 확인
fig = plt.figure()
# add_subplot을 통해 수동으로 Axes(그래프 영역) 추가
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

# 히스토그램 그리기
# bins: 데이터를 나누는 구간의 개수, alpha: 투명도(0~1 사이 값)
ax1.hist(np.random.randn(10000), bins=100, alpha=0.4)  
# 일반 선 그래프
ax2.plot(np.random.rand(1000))  
plt.show()

print("============막대그래프===========")
data = [50, 80, 100, 90, 70]
# plt.bar(x축 위치, 데이터 값): 세로 막대 그래프 생성
plt.bar(range(len(data)), data, alpha = 0.3) 
plt.show()

# 세로 막대 그래프 / 가로막대 그래프 => barh
err = np.random.rand(len(data))
# plt.barh: 가로(Horizontal) 막대 그래프, xerr: x축 방향의 오차 막대(error bar) 표시
plt.barh(range(len(data)), data, alpha = 0.3, xerr=err) 
plt.show()

print("============원===========")
# plt.pie(데이터): 파이 차트 생성
# explode: 특정 조각을 중심에서 분리하여 강조 (0은 붙어있음, 수치가 클수록 멀어짐)
plt.pie(data, colors=['yellow', 'blue', 'red'], explode=(0, 0.2, 0, 0.1, 0))
plt.title('Pie Chart')
plt.show()

print("============박스 플롯===========")
print("============전체 데이터의 분포, 이상치 확인하기 효과적===========")
data = [1, 50, 80, 100, 90, 70, 300]
# plt.boxplot: 데이터의 5개 요약 수치(최솟값, Q1, 중앙값, Q3, 최댓값)와 이상치(Outlier) 시각화
plt.boxplot(data)
plt.show()

print("============Bubble Chart===========")
print("============산점도 차트에 점의 크기를 동적으로 표시===========")
n = 30
np.random.seed(0) # 난수 생성을 고정하여 실행시마다 동일한 결과를 얻음
x = np.random.rand(n)
y = np.random.rand(n)
color = np.random.rand(n) # 각 점의 색상을 무작위로 설정
# scale: 점의 크기를 설정 (반지름의 제곱에 비례하게 면적 계산)
scale = np.pi * (np.random.rand(n) * 15) ** 2
plt.scatter(x, y, c=color, s=scale)             # c=색상, s=크기(size)
plt.show()

print("============시계열 데이터로 선그래프 ===========")
import pandas as pd
# 1000행 4열의 표준정규분포 난수 생성, 인덱스는 2000년 1월 1일부터 시작하는 날짜 데이터
fdata = pd.DataFrame(np.random.randn(1000, 4),
                    index=pd.date_range('1/1/2000', periods=1000),
                    columns=list('abcd'))
print(fdata.head(3)) # 상위 3개 행 확인
print(fdata.tail(3)) # 하위 3개 행 확인
# cumsum(): 누적합 계산 (시계열 데이터의 추세를 보기 위해 주로 사용)
fdata = fdata.cumsum()
print(fdata.head(3))
plt.plot(fdata) # Pandas DataFrame을 Matplotlib으로 직접 전달하여 그래프 생성
plt.show()

print("============Pandas의 plot 기능===========")
# Pandas 내부적으로 Matplotlib을 호출하여 더 간편하게 시각화
fdata.plot()            # 선 그래프가 기본값
fdata.plot(kind='bar')  # kind 옵션을 통해 막대 그래프 등 종류 변경 가능
plt.xlabel("time")
plt.ylabel("data")      # 기존 코드의 오타(xlabel 중복)를 ylabel로 수정하여 보실 수 있습니다.
plt.show()