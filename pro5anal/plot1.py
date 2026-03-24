# matplotlib : 플로팅 라이브러리. 그래프 생성을 위한 다양한 함수를 제공
# 시각화의 중요성

import numpy as np
import matplotlib.pyplot as plt

# [환경 설정] 한글 폰트 설정 (Windows: Malgun Gothic / Mac: AppleGothic)
plt.rc('font', family='malgun gothic')  
# [환경 설정] 마이너스 기호('-')가 깨지는 현상 방지
plt.rcParams['axes.unicode_minus'] = False 

# --- 1. 기본적인 선 그래프와 축 설정 ---
x = ("서울", "인천", "수원")    # 튜플 (리스트도 가능하나 Set은 순서가 없어 불가)
y = [5, 3, 7]

# plt.xlim, plt.ylim: x축과 y축의 표시 범위 [최소, 최대] 지정
plt.xlim([-1, 3])
plt.ylim([0, 10])

# plt.yticks: y축의 눈금(Tick)을 인위적으로 설정 (0부터 10까지 3 간격)
plt.yticks(list(range(0, 11, 3)))

plt.plot(x, y)
plt.show()

# --- 2. 데이터 값 표시 (plt.text) ---
data = np.arange(1, 11, 2)
plt.plot(data)  # x축을 생략하면 데이터의 인덱스(0, 1, 2...)가 자동 설정됨

x = [0, 1, 2, 3, 4]
for a, b in zip(x, data):
    # plt.text(x, y, text): 그래프 상의 특정 좌표에 텍스트 출력
    plt.text(a, b, str(b))
plt.show()

# --- 3. 스타일 커스터마이징 (포맷 문자열) ---
x = np.arange(10)
y = np.sin(x)
# 'go--': 색상(green), 마커(circle), 선스타일(dashed)을 한 번에 지정
# linewidth: 선 두께, markersize: 마커 크기
plt.plot(x, y, 'go--', linewidth=2, markersize=12)
plt.show()

# --- 4. 복합 그래프와 레이아웃 ---
x = np.arange(0, np.pi * 3, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# plt.figure: 그래프 도화지의 전체 크기(가로, 세로 인치) 설정
plt.figure(figsize=(10, 5))    
plt.plot(x, y_sin, 'r')         # 선 그래프 (red)
plt.scatter(x, y_cos)           # 산점도 (점 그래프)

plt.xlabel('x 축')
plt.ylabel('y 축')
plt.title('sine & cosine')
# plt.legend: 범례 표시 (데이터의 이름표 역할)
plt.legend(['sine', 'cosine'])    
plt.show()

# --- 5. 서브플롯 (Subplot) 활용 ---
print("===========subplot===========")
# plt.subplot(행, 열, 순서): 하나의 Figure를 나누어 여러 그래프를 그림
plt.subplot(2, 1, 1)    # 2행 1열의 첫 번째
plt.plot(x, y_sin)
plt.title('sine')

plt.subplot(2, 1, 2)    # 2행 1열의 두 번째
plt.plot(x, y_cos)
plt.title('cosine')
plt.show()

# --- 6. 그리드 설정 및 파일 저장 ---
irum = ['a', 'b', 'c', 'd', 'e']
kor = [80, 50, 70, 70, 90]
eng = [60, 70, 80, 90, 100]

plt.plot(irum, kor, 'ro-')
plt.plot(irum, eng, 'bo--')
plt.ylim([50, 100])
plt.title('시험 점수')
# loc=4: 범례 위치 지정 (4는 우측 하단/lower right)
plt.legend(['국어', '영어'], loc=4)
# plt.grid: 보조선(격자) 표시
plt.grid(True)

# plt.gcf(): 현재 생성된 Figure(도화지) 객체를 가져옴
fig = plt.gcf()
plt.show()

# fig.savefig: 생성된 그래프를 이미지 파일로 저장
fig.savefig('plot.png')

from matplotlib.pyplot import imread
img = imread('plot1.png')
plt.imshow(img)