# 원격 DB 연동 - jikwon 자료를 읽어 dataFrame에 저장
# import MySQLdb -> pymysql과 유사하게 사용 가능한 라이브러리 (이거 써도 무방)
import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib # matplotlib 그래프에서 한글 폰트가 깨지는 것을 방지함
import csv

# [DB 접속 설정] 딕셔너리 형태로 호스트, 계정, 암호, DB명, 포트, 인코딩을 정의
config = {
    'host':'127.0.0.1', # 데이터베이스가 설치된 서버의 IP 주소 (여기선 로컬 호스트)
    'user':'root',      # 데이터베이스 사용자 아이디
    'password':'123',   # 데이터베이스 비밀번호
    'database':'test',   # 접속할 데이터베이스의 이름
    'port':3306,        # MariaDB/MySQL의 기본 통신 포트
    'charset':'utf8'    # 인코딩 설정 (한글 데이터 처리용)
}

try:
    # 1. DB 연결: 설정한 config 정보를 언패킹(**)하여 DB 서버와 연결을 맺음
    conn = pymysql.connect(**config)
    # 2. 커서 생성: SQL 쿼리 실행 및 결과를 가리키기 위한 커서 객체를 생성
    cursor = conn.cursor()
    
    # 3. SQL 정의: 직원(jikwon)과 부서(buser) 테이블을 조인하여 6가지 정보를 추출하는 쿼리
    sql = """
        select jikwonno, jikwonname, busername, jikwonjik, jikwongen, jikwonpay
        from jikwon inner join buser on jikwon.busernum = buser.buserno
    """
    
    # 4. 쿼리 실행: 정의한 SQL 문을 DB 서버로 전달하여 실행함
    cursor.execute(sql)

    # 참고용: fetchall()을 쓰지 않고 커서를 직접 반복시켜 데이터를 한 줄씩 출력할 수도 있음
    # for jikwonno, jikwonname, busername, jikwonjik, jikwongen, jikwonpay in cursor:
    #     print(jikwonno, jikwonname, busername, jikwonjik, jikwongen, jikwonpay)
    
    print("=========DataFrame으로 출력=========")
    # cursor.fetchall(): 조회된 모든 데이터를 튜플 형태로 한 번에 가져옴
    # columns: 가져온 각 데이터에 이름을 부여하여 pandas 데이터프레임(df1) 생성
    df1 = pd.DataFrame(cursor.fetchall(), 
                    columns=['jikwonno', 'jikwonname', 'busername', 'jikwonjik', 'jikwongen', 'jikwonpay'])
    print(df1.head(3)) # 데이터 프레임 상위 3개 행을 미리보기 출력
    print('연봉의 총합 : ', df1['jikwonpay'].sum()) # sum(): '연봉' 컬럼 데이터의 전체 합계를 계산

    print("=========csv 파일로 출력=========")
    
    # 5. CSV 파일 저장: 데이터를 다시 읽기 위해 쿼리를 재실행하여 커서를 초기화함
    cursor.execute(sql) # => 앞에서 fetchall을 해서 다 읽은 상태이기 때문에 다시 수행한 것
    # mode='w': 쓰기 모드, encoding='utf-8': 한글 인코딩, newline='': 불필요한 공백 행 제거
    with open('pandasdb2.csv', mode='w', encoding='utf-8') as fobj:
        writer = csv.writer(fobj) # CSV를 작성해주는 writer 객체 생성
        for row in cursor.fetchall():
            writer.writerow(row) # 커서에 담긴 한 줄(Row)씩 반복하며 파일에 기록
    
    # 6. 저장된 CSV 읽기: 파일에서 데이터를 로드하고 한글 컬럼명(names)을 새로 부여함
    # => 바로 데이터프레임으로 만들어버림
    df2 = pd.read_csv('pandasdb2.csv', header=None, names=['번호', '이름', '부서', '직급', '성별', '연봉'])
    print(df2.head(3))

    print('\n\npandas의 sql 처리 함수 이용=========')
    # 7. pd.read_sql: 커서를 수동으로 조작하지 않고 직접 DB 데이터를 데이터프레임으로 로드함
    df = pd.read_sql(sql, conn) # => 통로 conn을 통해 sql문을 데이터프레임에서 실행해라
    # 데이터프레임의 모든 컬럼명을 한글로 일괄 변경
    df.columns = ['번호', '이름', '부서', '직급', '성별', '연봉']
    print(df.head(2))
    
    # print(df[:2])와 동일: 상위 2개 행을 슬라이싱하여 보여줌
    # count(): 특정 컬럼의 데이터 개수, len(): 데이터프레임 전체 행의 수
    print(df['이름'].count(), ' ', len(df))
    
    # value_counts(): '부서' 컬럼의 데이터별 빈도수(각 부서에 몇 명이 있는지)를 자동으로 집계
    print('부서별 인원수: ', df['부서'].value_counts())
    
    # .loc: 조건을 만족하는 행을 검색 (연봉 컬럼의 값이 7000 이상인 직원만 추출)
    print('연봉 7000 이상 : ', df.loc[df['연봉'] >= 7000])
    
    # 8. 교차표 작성: '성별'과 '직급' 간의 데이터 분포 빈도표를 만듦
    # margins=True: 가로와 세로의 전체 합계(All)를 포함함
    ctab = pd.crosstab(df['성별'], df['직급'], margins=True)
    print('교차표\n', ctab)

    print("=========시각화=========")
    # 9. 그룹 분석: '직급'을 기준으로 연봉 컬럼의 평균값(mean)을 집계함
    jik_ypay = df.groupby(['직급'])['연봉'].mean()     # 결과는 직급별 평균 연봉
    print('jik_ypay :', jik_ypay)
    
    # 10. 파이 차트(Pie Chart) 생성: 직급별 연봉 평균 비율을 시각화함
    # explode: 특정 조각(직급)을 강조하기 위해 밖으로 띄움 (조각별 이격 거리 설정)
    # labels: 조각의 이름을 설정 (여기서는 직급명)
    # shadow: 차트에 입체적인 그림자 효과 추가, counterclock=False: 시계 방향으로 배치
    plt.pie(jik_ypay, explode=(0.2, 0, 0, 0.3, 0),
                labels = jik_ypay.index,
                shadow = True, counterclock = False)
    plt.show() # 생성한 차트를 화면에 출력


except Exception as e:
    # try 문 내에서 실행 도중 접속 오류나 SQL 문법 오류가 발생하면 예외 메시지 출력
    print('처리 오류 : ', e)
finally:
    # 11. 리소스 반환: 작업이 끝난 커서와 연결 객체를 안전하게 닫음 (메모리 절약)
    cursor.close()
    conn.close()