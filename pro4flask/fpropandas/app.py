import os
import io
import base64
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pymysql
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from markupsafe import escape

app = Flask(__name__)

# 한글 폰트 설정 (윈도우 기준)
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

db_config = {
    'host':'127.0.0.1', 
    'user':'root', 
    'password':'123',
    'database':'test', 
    'port':3306, 
    'charset':'utf8mb4'
}

def get_connection():
    return pymysql.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dbshow', methods=['GET', 'POST'])
def dbshow():
    dept = request.args.get("dept", "").strip()
    engine = create_engine("mysql+mysqldb://root:123@127.0.0.1:3306/test?charset=utf8")

    # 1) 전체 데이터 가져오기 (사번, 직원명, 부서명, 직급, 연봉, 근무년수)
    sql = """
        select j.jikwonno as 사번, j.jikwonname as 직원명, b.busername as 부서명,
        j.jikwonjik as 직급, j.jikwonpay as 연봉, 
        TIMESTAMPDIFF(YEAR, j.jikwonibsail, CURDATE()) as 근무년수,
        j.jikwongen as 성별
        from jikwon j
        inner join buser b on j.busernum=b.buserno
    """
    df = pd.read_sql(sql, engine)
    
    # 부서번호(사번으로 대체 가능)와 직원명 순으로 오름차순 정렬
    df = df.sort_values(by=['부서명', '직원명'], ascending=True)

    # 1번 결과: HTML 변환
    jikwondata = df[['사번', '직원명', '부서명', '직급', '연봉', '근무년수']].to_html(index=False)

    # 2) 부서명, 직급별 연봉합, 연봉평균
    stats_df = df.groupby(["부서명", "직급"])["연봉"].agg(['sum', 'mean']).reset_index()
    stats_df.columns = ['부서명', '직급', '연봉합', '연봉평균']
    statsdata = stats_df.to_html(index=False)

    # 3) 부서명별 연봉합, 평균 세로막대 그래프 (이미지 저장 방식)
    graph_df = df.groupby("부서명")["연봉"].agg(['sum', 'mean']).reset_index()
    plt.figure(figsize=(8, 4))
    x = np.arange(len(graph_df))
    plt.bar(x, graph_df['sum'], width=0.4, label='연봉합')
    plt.bar(x-0.4, graph_df['mean'], width=0.4, label='연봉평균')
    plt.xticks(x, graph_df['부서명'])
    plt.legend()
    
    # 메모리에 저장 후 base64 인코딩 (파일 저장보다 관리하기 편함)
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    graph_img = f"data:image/png;base64,{img_base64}"
    plt.close()

    # 4) 성별, 직급별 빈도표
    # 빈도표는 index(성별)가 보여야 하므로 index=True로 설정
    cross_tab = pd.crosstab(df['성별'], df['직급'], margins=True)
    graph_num4 = cross_tab.to_html()

    # 5) 부서별 최고 연봉자 출력
    # 각 부서 그룹별로 연봉이 가장 높은 인덱스를 찾아 해당 행만 추출
    top_pay_df = df.loc[df.groupby("부서명")["연봉"].idxmax()]
    top_pay_data = top_pay_df[['부서명', '직원명', '연봉']].to_html(index=False)

    # 6) 부서별 직원 비율 계산
    total_count = len(df)
    dept_counts = df['부서명'].value_counts().reset_index()
    dept_counts.columns = ['부서명', '인원수']
    dept_counts['비율(%)'] = (dept_counts['인원수'] / total_count * 100).round(2)
    ratio_data = dept_counts.to_html(index=False)

    return render_template('dbshow.html', 
                            jikwondata=jikwondata,
                            statsdata=statsdata,
                            graph_img=graph_img,
                            graph_num4=graph_num4,
                            top_pay_data=top_pay_data,
                            ratio_data=ratio_data,
                            total_info=f"총 인원: {total_count}명")

if __name__ == '__main__':
    app.run(debug=True)