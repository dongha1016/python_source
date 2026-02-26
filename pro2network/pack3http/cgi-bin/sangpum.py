# 웹 서버에서 DB 자료를 출력하는 방법

import sys
sys.stdout.reconfigure(encoding = 'utf-8')

import MySQLdb
import pickle
# DB의 연동정보를 불러드림

with open("cgi-bin/mydb.dat", mode = 'rb') as obj:
    config = pickle.load(obj)

print("Content-Type: text/html; charset=utf-8")
print()
print("<html><body><b>** 상품 정보 **</b><br/>")
print("<table border = '1'>")
# 테이블을 만드는데 두께를 1로 해라

print("<tr><td>코드</td><td>상품명</td><td>수량</td><td>단가</td></tr>")
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()

    cursor.execute("select * from sangdata order by code desc")
    # SQL문 실행
    datas = cursor.fetchall()
    for code, sang, su, dan in datas:
        print("""
            <tr>
                <td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td>
            </tr>
        """.format(code, sang, su, dan))


except Exception as e:
    print("err: ", e)
finally:
    cursor.close()
    conn.close()

print("</table>")
print("</body></html>")


