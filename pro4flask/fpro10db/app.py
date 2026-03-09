from flask import Flask, render_template, request, redirect, url_for, flash
# flash : 임시메세지 출력용 (내부적으로 session 저장해 둠 - secret_key 필요)
# pip install pymysql
import pymysql
import os
from flask import get_flashed_messages  # 저장해 둔 메세지를 꺼내는 함수
# ex) flash("에러~") -> 메세지를 세션에 잠시 저장 후 get_flashed_messages() 하면 메세지를 읽음

app = Flask(__name__);
app.secret_key = "abcdef123456"    # session/flash를 위한 쿠키 서명용 비밀키

# MariaDB 연결 정보
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root") # 실 산업에서는 사용자 계정으로 접속
DB_PASSWORD = os.getenv("DB_PASSWORD", "123") # 실 산업에서는 사용자 계정으로 접속
DB_NAME = os.getenv("DB_NAME", "test") # 실 산업에서는 사용자 계정으로 접속

def get_conn():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset="utf8mb4",   # utf8mb4 : 전세계 문자(한글 포함) + 이모지까지 처리 가능
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False
    )
    # DictCursor : select 결과를 'dict type' 형태로 받게 해줌
    # {'code' : 1, 'sang':'마우스'...} -> row['code'], row['sang']
    # row를 써주면 가독성이 좋아짐

@app.get("/")
def root():
    return redirect(url_for("show_list"))

## 1) DB 연결
@app.get('/show')
def show_list():
    # DB 서버와 연결
    conn = get_conn()
    # 외부와 연결할 때는 무조건 try를 사용해라. => 외부 장치는 현재는 잘 돌아가도 장치 고장으로 안돌아 갈 수 있음
    try:
        # conn.cursor() 사용 후 자동으로 닫힘
        with conn.cursor() as cur:
            cur.execute("select code, sang, su, dan from sangdata order by code")
            rows = cur.fetchall()

        messages = list(get_flashed_messages())
        return render_template("list.html", rows=rows, messages=messages)

    # except pymysql.err.IntegrityError as e:
    #     # ...
    except Exception as e:
        pass
        # flash(f'DB 자료 읽기 오류 : {e}')
        # return redirect(url_for("show_list"))
    finally:
        # 작업 후 연결 끊기
        conn.close()


## 2) 데이터 추가
# 추가 폼 호출
@app.get("/add/")
def add_form():
    messages = list(get_flashed_messages())
    return render_template("form_add.html", messages=messages)  # 추가 폼 호출

# 추가 처리
@app.post("/add/")
def add_save():
    messages = list(get_flashed_messages())
    sang = (request.form.get("sang") or "").strip()
    su_raw = (request.form.get("su") or "").strip()  # '23'
    dan_raw = (request.form.get("dan") or "").strip()

    if not sang or not su_raw.isdigit() or not dan_raw.isdigit():
        flash("sang은 필수, su/dan은 숫자만 허용")
        return redirect(url_for("add_form"))

    su = int(su_raw)    # 연산없이 추가이므로 숫자화 안해도 됨
    dan = int(dan_raw)

    conn = get_conn()
    try:
        # code는 자동증가 프로그래밍 하기
        with conn.cursor() as cur:
            cur.execute('select max(code) as max_code from sangdata')
            row=cur.fetchone()
            max_code = row['max_code'] if row else None
            # 새 상품의 코드를 얻음
            next_code = (max_code + 1) if max_code is not None else 1
            
            # 추가하기
            cur.execute("insert into sangdata(code, sang, su, dan) values (%s, %s, %s, %s)", (next_code, sang, su, dan))
        conn.commit()
        return redirect(url_for("show_list"))
    
    except Exception as e:
        conn.rollback()
        flash(f'저장 실패 : {e}')
        return redirect(url_for("add_form"))
    finally:
        conn.close()


## 3) 데이터 수정
# 수정 폼 호출
@app.get("/edit/<int:code>/")
def edit_form(code:int):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("select * from sangdata where code=%s", (code,))
            row = cur.fetchone()
        if not row:
            flash("해당 자료가 없어요")
            return redirect(url_for("show_list"))
        
        messages = list(get_flashed_messages())
        return render_template("form_edit.html", row=row, messages=messages)

    finally:
        conn.close()

# 수정 처리
@app.post("/edit/<int:code>/")
def edit_save(code:int):    
    messages = list(get_flashed_messages())
    sang = (request.form.get("sang") or "").strip()
    su_raw = (request.form.get("su") or "").strip()  # '23'
    dan_raw = (request.form.get("dan") or "").strip()

    if not sang or not su_raw.isdigit() or not dan_raw.isdigit():
        flash("sang은 필수, su/dan은 숫자만 허용")
        return redirect(url_for("edit_form", code=code))

    su = int(su_raw)    # 연산없이 추가이므로 숫자화 안해도 됨
    dan = int(dan_raw)

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # 수정하기
            cur.execute("update sangdata set sang=%s, su=%s, dan=%s where code=%s",(sang, su, dan, code))
        conn.commit()
        return redirect(url_for("show_list"))
    
    except Exception as e:
        conn.rollback()
        flash(f'수정 실패 : {e}')
        return redirect(url_for("edit_form"))
    finally:
        conn.close()


## 4) 데이터 삭제
# 삭제
@app.post("/delete/<int:code>/")
def delete_row(code:int):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # 삭제하기
            cur.execute("delete from sangdata where code=%s",(code))
        conn.commit()
        return redirect(url_for("show_list"))
    
    except Exception as e:
        conn.rollback()
        flash(f'삭제 실패 : {e}')
        return redirect(url_for("show_form"))
    finally:
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)