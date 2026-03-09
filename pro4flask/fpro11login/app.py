# pip install pymysql
# pip install python-dotenv
from flask import Flask, render_template, request, redirect, url_for, flash, session
# flash : 임시메세지 출력용 (내부적으로 session 저장해 둠 - secret_key 필요)
from dotenv import load_dotenv
# API 키, 데이터베이스 비밀번호, Flask의 SECRET_KEY 같은 민감한 정보들을
# 코드에 직접 적지 않고 별도의 파일(.env)에 저장한 뒤 불러오기 위해 사용합니다

import pymysql
import os
from flask import get_flashed_messages  # 저장해 둔 메세지를 꺼내는 함수
# ex) flash("에러~") -> 메세지를 세션에 잠시 저장 후 get_flashed_messages() 하면 메세지를 읽음

app = Flask(__name__);
app.secret_key = "abcdef123456"    # session/flash를 위한 쿠키 서명용 비밀키

load_dotenv()   # .env 파일에 저장된 환경변수 읽기 함수

# MariaDB 연결 정보
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_USER = os.getenv("DB_USER") # 실 산업에서는 사용자 계정으로 접속
DB_PASSWORD = os.getenv("DB_PASSWORD") # 실 산업에서는 사용자 계정으로 접속
DB_NAME = os.getenv("DB_NAME") # 실 산업에서는 사용자 계정으로 접속

def get_conn():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset="utf8mb4",   # utf8mb4 : 전세계 문자(한글 포함) + 이모지까지 처리 가능
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )
    # DictCursor : select 결과를 'dict type' 형태로 받게 해줌
    # {'code' : 1, 'sang':'마우스'...} -> row['code'], row['sang']
    # row를 써주면 가독성이 좋아짐

@app.get("/")
def root():
    return redirect(url_for("login_form"))

# 로그인폼

@app.get("/login")
def login_form():
    return render_template("login.html")

@app.post("/login")
def login_post():
    jikwonno_raw = (request.form.get("jikwonno") or "").strip()
    jikwonname = (request.form.get("jikwonname") or "").strip()

    if not jikwonno_raw.isdigit() or not jikwonname:
        flash("직원번호는 숫자, 직원이름은 필수입니다.")
        return redirect(url_for("login_form"))
    
    jikwonno = int(jikwonno_raw)

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # 로그인 체크
            cur.execute("""
                select jikwonno, jikwonname from jikwon
                where jikwonno = %s and jikwonname = %s
            """,(jikwonno, jikwonname))

            me = cur.fetchone()
            if not me:
                flash("로그인 실패: 직원정보 불일치!!")
                return redirect(url_for("login_form"))
            
            # 로그인 성공인 경우
            cur.execute("""
                select jikwonno, jikwonname, busername, jikwonjik, jikwonpay, 
                YEAR(jikwonibsail) as jikwonibsail_year
                from jikwon inner join buser
                on busernum=buserno order by jikwonno
            """)
            rows = cur.fetchall()

        # 세션 생성
        session["jikwonno"] = me["jikwonno"]
        session["jikwonname"] = me["jikwonname"]

        return render_template("jikwonlist.html", rows=rows, login_user = me)

    finally:
        conn.close()

@app.get("/gogek/<int:jikwonno>")
def gogek_list(jikwonno:int):
    if "jikwonno" not in session:
        flash("로그인 후 고객정보 이용하세요")
        return redirect(url_for("login_form"))
    
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                select gogekno, gogekname, gogektel
                from gogek
                where gogekdamsano = %s order by gogekno
            """, (jikwonno,))
            customers = cur.fetchall()

            cur.execute("""
                    select jikwonname from jikwon
                    where jikwonno = %s
                    """, (jikwonno,))
            emp = cur.fetchone()

        return render_template("gogeklist.html", 
                            customers=customers, empno=jikwonno, 
                            empname = (emp["jikwonname"] if emp else ""))
    finally:
        conn.close()

@app.get("/jikwons")
def jikwon_list():
    if "jikwonno" not in session:
        flash("로그인 후 고객정보 이용하세요")
        return redirect(url_for("login_form"))
    
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                select jikwonno, jikwonname, busername, jikwonjik, jikwonpay, 
                YEAR(jikwonibsail) as jikwonibsail_year
                from jikwon inner join buser
                on busernum=buserno order by jikwonno
            """)
            rows = cur.fetchall()

        login_user = {"jikwonno":session["jikwonno"], "jikwonname":session["jikwonname"]}
        return render_template("jikwonlist.html", rows = rows, login_user = login_user)

    finally:
        conn.close()

# 로그아웃
@app.post("/logout")
def logout():
    session.clear()
    return redirect(url_for("login_form"))

if __name__ == "__main__":
    app.run(debug=True)