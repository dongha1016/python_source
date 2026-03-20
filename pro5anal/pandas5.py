# pandas file i/o

import pandas as pd
import numpy as np

df = pd.read_csv('ex1.csv')                 # csv파일 불러오기
print(df, '\n',  type(df))
print()
df = pd.read_table('ex1.csv', sep=',')      # table은 csv처럼 자르지 않기 때문에 구분자를 준다
print(df)
print("skip_blank_lines : 칼럼명, 데이터의 앞에 공백을 제거")
df = pd.read_table('ex1.csv', sep=',', skip_blank_lines=True)     
print(df)
print("======웹상에서 CSV파일 읽기======")
pd.set_option('display.max_columns', None)  # 모든 칼럼 표시 옵션
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex2.csv')
print(df)
print("========모든 데이터가 테이블안에 들어가게=======")
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex2.csv', header=None)
print(df)
print("========행 하나 스킵=======")
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex2.csv', header=None, skiprows=1)
print(df)
print("========칼럼의 이름 주기=======")
# names => column의 이름
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex2.csv', header=None, names=['a', 'b', 'c', 'd', 'e'])
print(df)


print()
df = pd.read_table('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex3.txt', sep=r'\s+')  
# sep='\s+'로 지정하면 => 공백이 몇 칸이든 깔끔하게 무시하고 데이터만 골라냅니다.
print(df)
print(df.iloc[:,0]) # 0번째 column에 대해서만 출력

print("========특정 행 읽기에서 제거=======")
df = pd.read_table('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex3.txt', sep=r'\s+', skiprows=[1,3])  
print(df)

print("============자리수로 읽기(FWF:Fixed-Width Formatted lines)===========")
df = pd.read_fwf('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/data_fwt.txt', 
                header=0, widths=(10,3,5), names=['date', 'name', 'price'], encoding = 'utf8')
print(df)
print(df.iloc[:,0])
print(df['date'])
print("\n============= Chunk : 대량의 데이터를 부분씩 메모리로 읽어 처리 =============")
# 대용량 자료 로딩시 초과 오류 발생 방지 : 메모리를 절약
# 스트리밍 방식(일부만 순차 처리)으로 읽음
# 분산처리의 효과 
# 여러번 반복해 읽어야하므로 속도는 느리다

import time
n_rows = 10000
data = {
    'id':range(1, n_rows + 1),
    'name':[f'Student_{i}' for i in range(1, n_rows + 1)],
    'score1':np.random.randint(50, 101, size=n_rows),
    'score2':np.random.randint(50, 101, size=n_rows)
}

df = pd.DataFrame(data)
print(df.head())    # default 5개
print(df.tail(3))

csv_fname = 'students.csv'
df.to_csv(csv_fname, index=False)   # csv 파일로 저장

print("============= csv 파일 읽기 ============")
start_all = time.time()
df_all = pd.read_csv(csv_fname)
average_all_1 = df_all['score1'].mean()
average_all_2 = df_all['score2'].mean()
time_all = time.time() - start_all  # 전체 걸린 시간 

print('\n처리 결과')
print('전체 한 번에 처리 시간 : ', round(time_all, 5))  # 소수점 5째짜리까지 보여주기

# chunk로 읽기 
chunk_size = 1000
total_score1 = 0 
total_score2 = 0 
total_count = 0
start_chunk_total = time.time()

for i, chunk in enumerate(pd.read_csv(csv_fname, chunksize=chunk_size)):
    start_chunk = time.time()
    # 청크 처리 중 첫번째 학생 정보 출력
    first_student = chunk.iloc[0]
    print(f'Chunk {i+1} 첫번째 학생:ID={first_student['id']}, \
        이름은 {first_student['name']}',
        f"score1={first_student['score1']}, score2={first_student['score2']}")
    
    total_score1 += chunk['score1'].sum()
    total_score2 += chunk['score2'].sum()
    total_count += len(chunk)

    end_chunk = time.time()
    elapsed = end_chunk - start_chunk
    print(f'    처리 시간 : {elapsed:7f}')          # chunk 단위 처리 시간

time_chunk_total = time.time() - start_chunk_total  # 총 시간
average_chunk1 = total_score1 / total_count
average_chunk2 = total_score2 / total_count

print('\n처리 결과')
print(f'전체 학생 수 : {total_count}')
print(f'score1 총합, 평균 : {total_score1}, {average_chunk1:3f}')
print(f'score2 총합, 평균 : {total_score2}, {average_chunk2:3f}')
print(f'전체 한 번에 처리 시간 : {time_all:7f}')
print(f'Chunk로 처리한 총 시간 : {time_chunk_total:7f}')

print("==========청크 처리 시간 시각화==========")
import matplotlib.pyplot as plt
plt.rc('font', family="Malgun Gothic")  # 폰트 깨짐 방지
labels = ['전체 한번에 처리', '청크로 처리']
times = [time_all, time_chunk_total]

plt.figure(figsize=(6,4))
bars = plt.bar(labels, times, color=['skyblue', 'red'])
for bar, time_val in zip(bars, times):
    plt.text(bar.get_x() + bar.get_width() / 2, \
            bar.get_height(), f'{time_val:3f}초', \
            ha = 'center', va = 'bottom', fontsize=10)

plt.ylabel('처리시간(초)')
plt.grid(linestyle='--')
plt.tight_layout()
plt.show()