# local db 연동 후 DataFrame의 자료 저장
import sqlite3 

# [SQL 정의] 테이블 생성 쿼리 (상품명, 제조사, 무게, 가격 컬럼 구성)
# if not exists: 테이블이 이미 존재하면 새로 만들지 않음
sql = "create table if not exists " \
    "extab(product varchar(10), maker varchar(10), weight real, price integer)"

# [DB 연결] :memory:는 하드디스크가 아닌 RAM에 임시로 DB를 생성함 (프로그램 종료 시 데이터 소멸)
conn = sqlite3.connect(':memory:')
conn.execute(sql) # 테이블 생성 실행
conn.commit()     # 변경사항 확정

# --- 1. 데이터 삽입 (Insert) ---
data = [('mouse','samsung',12.5,5000), ('keyboard','lg',52.5,35000)]
isql = "insert into extab values(?,?,?,?)" # 파라미터 바인딩 방식 (보안 및 효율성)

# executemany: 리스트 형태의 여러 데이터를 한 번에 삽입
conn.executemany(isql, data)

# execute: 단일 데이터 삽입
data1 = ('pen', 'abc', 5.0, 1200)
conn.execute(isql, data1)
conn.commit()

# --- 2. 데이터 조회 (Select) 및 출력 ---
cursor = conn.execute("select * from extab")
rows = cursor.fetchall() # 조회된 모든 행을 리스트(튜플 묶음)로 가져옴
for a in rows:
    print(a)

print('rows를 DataFrame에 저장')
import pandas as pd
# [방법 1] fetchall로 가져온 튜플 리스트를 직접 DataFrame으로 변환
df1 = pd.DataFrame(rows, columns=['product', 'maker', 'weight', 'price'])
print(df1)
print(df1.describe()) # 수치형 데이터(weight, price)의 기초 통계량 확인
print()

# [방법 2] pd.read_sql: SQL 쿼리를 던져서 결과를 즉시 DataFrame으로 읽어옴 (권장 방식)
df2 = pd.read_sql("select * from extab", conn)
print(df2)
# SQL 함수(count) 사용 예시
print(pd.read_sql("select count(*) as 건수 from extab", conn))

print('DataFrame의 자료를 테이블에 저장(insert)')

# 삽입할 새로운 데이터 정의
data = {
    'product':['연필', '볼펜', '지우개'],
    'maker':['모나미','모나미','모나미'],
    'weight':[2.3, 3.0, 5.0],
    'price':(1000, 2000, 500)
}

frame = pd.DataFrame(data)
print(frame)

# --- 3. DataFrame을 DB 테이블로 저장 (to_sql) ---
# name: 저장할 테이블 이름
# con: 연결된 DB 객체
# if_exists='append': 기존 데이터 뒤에 추가 (replace는 기존 테이블 삭제 후 재생성)
# index=False: DataFrame의 인덱스(0, 1, 2...)는 DB 컬럼으로 저장하지 않음
frame.to_sql("extab", conn, if_exists='append', index=False)

# 최종 저장 결과 확인
df3 = pd.read_sql("select * from extab", conn)
print(df3)

# 리소스 해제
cursor.close()
conn.close()