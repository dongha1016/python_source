# Pandas의 Dataframe의 자료를 원격 DB의 테이블에 저장

import pandas as pd
from sqlalchemy import create_engine
import pymysql

data = {
    'code':[10,11,12],
    'sang':['사이다', '맥주', '와인'],
    'su':[20, 22, 5],
    'dan':[5000, 3000, 70000]
}
try:
    frame = pd.DataFrame(data)
    print(frame)

    engine = create_engine("mysql+mysqldb://root:123@127.0.0.1:3306/test?charset=utf8")
    # "내 컴퓨터에 있는 MySQL 서버의 test 데이터베이스에 root 계정으로 접속하기 위한 '전용 통로'를 만드는 코드입니다."
    conn = engine.connect()
    # 저장
    # frame 데이터를 MySQL의 'sangdata' 테이블로 저장하며, 이미 테이블이 있으면 새로 교체(replace)한다.
    frame.to_sql(name='sangdata', con=engine, if_exists='replace', index=False)
    # 읽기
    df = pd.read_sql("select * from sangdata", engine)


except Exception as e:
    print("처리 오류 :", e)
