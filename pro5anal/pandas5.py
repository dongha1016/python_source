# pandas file i/o

import pandas as pd
import numpy as np

# [CSV 읽기 기본]
df = pd.read_csv('ex1.csv')                 # 쉼표(,)로 구분된 표준 CSV 파일을 불러와 데이터프레임으로 생성
print(df, '\n',  type(df))
print()

# [read_table 사용법]
# read_table은 기본 구분자가 탭('\t')이므로, CSV를 읽을 때는 sep=','를 명시해야 합니다.
df = pd.read_table('ex1.csv', sep=',')      
print(df)

# skip_blank_lines: 데이터 사이의 빈 줄을 무시하고 읽어올지 결정합니다.
print("skip_blank_lines : 칼럼명, 데이터의 앞에 공백을 제거")
df = pd.read_table('ex1.csv', sep=',', skip_blank_lines=True)     
print(df)

print("======웹상에서 CSV파일 읽기======")
# 데이터가 너무 많아 줄임표(...)로 보일 때 모든 컬럼을 다 보고 싶다면 아래 옵션을 씁니다.
pd.set_option('display.max_columns', None)  # 모든 칼럼 표시 옵션
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex2.csv')
print(df)

print("========모든 데이터가 테이블안에 들어가게=======")
# header=None: 파일의 첫 줄이 컬럼명이 아닐 때 사용합니다. 판다스가 0, 1, 2... 숫자로 이름을 붙여줍니다.
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex2.csv', header=None)
print(df)

print("========행 하나 스킵=======")
# skiprows: 불필요한 행(예: 파일 설명 등)을 건너뛰고 실제 데이터부터 읽고 싶을 때 사용합니다.
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex2.csv', header=None, skiprows=1)
print(df)

print("========칼럼의 이름 주기=======")
# names: 데이터에 컬럼명이 없을 때 리스트 형태로 직접 이름을 부여합니다.
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex2.csv', header=None, names=['a', 'b', 'c', 'd', 'e'])
print(df)


print()
# sep=r'\s+': 정규표현식을 사용하여 하나 이상의 공백(스페이스, 탭 등)을 모두 구분자로 인식합니다.
df = pd.read_table('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex3.txt', sep=r'\s+')  
print(df)
print(df.iloc[:,0]) # 첫 번째 열 전체 출력

print("========특정 행 읽기에서 제거=======")
# skiprows에 리스트를 주면 [1, 3]번 인덱스의 행을 정확히 골라 빼고 읽습니다.
df = pd.read_table('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex3.txt', sep=r'\s+', skiprows=[1,3])  
print(df)

print("============자리수로 읽기(FWF:Fixed-Width Formatted lines)===========")
# 구분자 없이 데이터의 '길이'가 정해진 파일(예: 과거 금융 데이터 등)을 읽을 때 사용합니다.
df = pd.read_fwf('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/data_fwt.txt', 
                header=0, widths=(10,3,5), names=['date', 'name', 'price'], encoding = 'utf8')
print(df)
print(df.iloc[:,0])
print(df['date'])

print("\n============= Chunk : 대량의 데이터를 부분씩 메모리로 읽어 처리 =============")
# [청크 처리의 의미]
# 1. 메모리 절약: 10GB 파일을 1GB씩 10번에 나눠 읽으면 저사양 PC에서도 분석이 가능합니다.
# 2. 스트리밍: 데이터 전체가 로드될 때까지 기다리지 않고, 읽어온 부분부터 바로 처리를 시작합니다.
# 3. 분산 처리 준비: 데이터를 쪼개서 병렬로 계산할 수 있는 기반이 됩니다.

import time
n_rows = 10000
data = {
    'id':range(1, n_rows + 1),
    'name':[f'Student_{i}' for i in range(1, n_rows + 1)],
    'score1':np.random.randint(50, 101, size=n_rows),
    'score2':np.random.randint(50, 101, size=n_rows)
}

df = pd.DataFrame(data)
print(df.head())    # 상위 데이터 확인
print(df.tail(3))   # 하위 데이터 확인

csv_fname = 'students.csv'
df.to_csv(csv_fname, index=False)   # 분석용 샘플 CSV 생성

print("============= csv 파일 읽기 ============")
# [일반 방식] 전체를 한 번에 메모리에 올림
start_all = time.time()
df_all = pd.read_csv(csv_fname)
average_all_1 = df_all['score1'].mean()
average_all_2 = df_all['score2'].mean()
time_all = time.time() - start_all  # 전체 소요 시간 계산

print('\n처리 결과')
print('전체 한 번에 처리 시간 : ', round(time_all, 5))

# [청크 방식] 일정 단위(1,000줄)씩 나누어 순차적으로 처리
chunk_size = 1000
total_score1 = 0 
total_score2 = 0 
total_count = 0
start_chunk_total = time.time()

# chunksize를 설정하면 데이터프레임이 아닌 'TextFileReader'라는 반복자(Iterator)를 반환합니다.
for i, chunk in enumerate(pd.read_csv(csv_fname, chunksize=chunk_size)):
    start_chunk = time.time()
    
    # 현재 읽어온 뭉치(chunk)에서 첫 번째 데이터 확인
    first_student = chunk.iloc[0]
    print(f'Chunk {i+1} 첫번째 학생:ID={first_student["id"]}, '
          f'이름은 {first_student["name"]}, '
          f"score1={first_student['score1']}, score2={first_student['score2']}")
    
    # 쪼개진 데이터별로 합계와 개수를 누적합니다.
    total_score1 += chunk['score1'].sum()
    total_score2 += chunk['score2'].sum()
    total_count += len(chunk)

    end_chunk = time.time()
    elapsed = end_chunk - start_chunk
    print(f'    단위 처리 시간 : {elapsed:7f}')

time_chunk_total = time.time() - start_chunk_total  # 청크 처리 총 소요 시간
average_chunk1 = total_score1 / total_count
average_chunk2 = total_score2 / total_count

print('\n최종 처리 결과 요약')
print(f'전체 학생 수 : {total_count}')
print(f'score1 총합, 평균 : {total_score1}, {average_chunk1:3f}')
print(f'score2 총합, 평균 : {total_score2}, {average_chunk2:3f}')
print(f'전체 로드 방식 소요 시간 : {time_all:7f}')
print(f'Chunk 분할 방식 소요 시간 : {time_chunk_total:7f}')

print("==========처리 방식별 성능 시각화==========")
import matplotlib.pyplot as plt
plt.rc('font', family="Malgun Gothic")  # 한글 깨짐 방지 설정
labels = ['전체 한 번에', '청크 분할']
times = [time_all, time_chunk_total]

plt.figure(figsize=(7,5))
bars = plt.bar(labels, times, color=['skyblue', 'salmon'])

# 막대 위에 정확한 초 단위 시간 표시
for bar, time_val in zip(bars, times):
    plt.text(bar.get_x() + bar.get_width() / 2, 
            bar.get_height(), f'{time_val:3f}s', 
            ha = 'center', va = 'bottom', fontsize=11, fontweight='bold')

plt.title('데이터 로드 방식별 처리 시간 비교', fontsize=14)
plt.ylabel('처리시간(초)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()