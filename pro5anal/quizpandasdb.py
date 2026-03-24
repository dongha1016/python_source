# pandas 문제 7)
#  a) MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오.

import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwonno, jikwonname, busername, jikwonjik, jikwonpay
        from jikwon inner join buser on jikwon.busernum = buser.buserno
    """
#      - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
    cursor.execute(sql)
    print("=========DataFrame으로 출력=========")
    df1 = pd.DataFrame(cursor.fetchall(), 
                    columns=['jikwonno', 'jikwonname', 'busername', 'jikwonjik', 'jikwonpay'])
    print(df1)

#      - DataFrame의 자료를 파일로 저장
    cursor.execute(sql)
    with open('quizpandasdb.csv', mode='w', encoding='utf-8') as fobj:
        writer = csv.writer(fobj)
        for row in cursor.fetchall():
            writer.writerow(row)
    df = pd.read_csv('pandasdb2.csv', header=None, names=['번호', '이름', '부서', '직급', '연봉'])

#      - 부서명별 연봉의 합, 연봉의 최대/최소값을 출력

    cursor.execute(sql)
    df2 = pd.read_sql(sql, conn)
    df2.columns = ['번호', '이름', '부서', '직급', '연봉']
    buser_sum = df2.groupby(['부서'])['연봉'].sum()
    buser_max = df2.groupby(['부서'])['연봉'].max()
    buser_min = df2.groupby(['부서'])['연봉'].min()
    print(buser_sum, buser_min, buser_max)

#      - 부서명, 직급으로 교차 테이블(빈도표)을 작성(crosstab(부서, 직급))

    ctab = pd.crosstab(df2['부서'], df['직급'], margins=True)
    print('빈도표\n', ctab)

#      - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시

    # cursor = conn.cursor()
    # sql = """
    #     select gogekno, gogekname, gogektel
    #     from gogek inner join buser on jikwon.jikwonno = gogek.gogekdamsano
    # """
    # cursor.execute(sql)
    
    
#      - 연봉 상위 20% 직원 출력  : quantile()
    print(df2.loc[df2['연봉']].quantile(0.2))
#      - SQL로 1차 필터링 후 pandas로 분석 
#             - 조건: 연봉 상위 50% (df['연봉'].median() ) 만 가져오기  후 직급별 평균 연봉 출력
#      - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성


except Exception as e:
    print('처리 오류 : ', e)
finally:
    cursor.close()
    conn.close()


#  b) MariaDB에 저장된 jikwon 테이블을 이용하여 아래의 문제에 답하시오.
#      - pivot_table을 사용하여 성별 연봉의 평균을 출력
#      - 성별(남, 여) 연봉의 평균으로 시각화 - 세로 막대 그래프
#      - 부서명, 성별로 교차 테이블을 작성 (crosstab(부서, 성별))

#  c) 키보드로 사번, 직원명을 입력받아 로그인에 성공하면 console에 아래와 같이 출력하시오.
#       조건 :  try ~ except MySQLdb.OperationalError as e:      사용
#      사번  직원명  부서명   직급  부서전화  성별
#      ...
#      인원수 : * 명
#     - 성별 연봉 분포 + 이상치 확인    <== 그래프 출력
#     - Histogram (분포 비교) : 남/여 연봉 분포 비교    <== 그래프 출력