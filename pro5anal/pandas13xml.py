from bs4 import BeautifulSoup

# [로컬 XML 파일 읽기]
# 'with' 문을 사용해 파일을 열면 처리가 끝난 후 자동으로 파일을 닫아줍니다.
with open('my.xml', mode='r', encoding='utf-8') as f:
    xmlfile = f.read()
    print(xmlfile, type(xmlfile))

# BeautifulSoup 객체 생성: XML 구조를 파싱하기 위해 'lxml' 파서를 사용합니다.
soup = BeautifulSoup(xmlfile, 'lxml')
print(type(soup))  # <class 'bs4.BeautifulSoup'>
print()

# find_all(): 'item'이라는 모든 태그를 리스트 형태로 가져옵니다.
itemTag = soup.find_all('item')
print(itemTag)

print()

# 태그의 속성(Attribute) 접근
nameTag = soup.find_all('name')
# nameTag[0]['id']: 첫 번째 name 태그 안에 작성된 id="값" 속성을 추출합니다.
print(nameTag[0]['id'])
print('--------------------')

# [중첩 루프를 이용한 세부 데이터 추출]
for i in itemTag:
    # 각 item 노드 하위의 name 태그들을 다시 찾습니다.
    nameTag = i.find_all('name')
    for j in nameTag:   
        # j['id']: 속성값 추출 / j.string: 태그 사이의 텍스트 추출
        print("id: " + j['id'] + ' / name: ' + j.string)
        # item 노드 안에서 tel 태그를 하나 찾아 텍스트를 출력합니다.
        tel = i.find('tel')
        print("tel :", tel.string)
    
    # exam 태그에 속성으로 저장된 점수(kor, eng) 정보를 추출합니다.
    for j in i.find_all('exam'):
        print("kor:" + j["kor"] + ", emg:" + j["eng"])
    print()

print('\n 서울시 제공 도서관 정보 xml 샘플 자료 5개 읽기')

import urllib.request as req
import pandas as pd

# 서울시 열린데이터 광장 Open API URL (도서관 운영시간 정보 1~5번 데이터)
url = "http://openapi.seoul.go.kr:8088/sample/xml/SeoulLibraryTimeInfo/1/5/"
# urllib를 통해 데이터를 읽어온 후 문자열로 디코딩합니다.
plainText = req.urlopen(url).read().decode()
print(plainText)

# XML 전용 파서('xml')를 사용하여 객체를 생성합니다.
xmlObj = BeautifulSoup(plainText, 'xml')

# select('row'): CSS 선택자를 이용해 모든 <row> 태그를 수집합니다.
libData = xmlObj.select('row')

rows = [] # 데이터프레임 구성을 위한 리스트
for data in libData:
    # find(): 각 row 내부에서 도서관명(LBRRY_NAME)과 주소(ADRES) 태그를 찾습니다.
    name = data.find("LBRRY_NAME").string
    addr = data.find("ADRES").string
    
    print('도서관명: ', name)
    print('주소: ', addr)
    print()
    
    # 딕셔너리 형태로 리스트에 추가하여 데이터프레임 재료를 만듭니다.
    rows.append({"도서관명":name, "주소":addr})
    
    # 루프 내부에서 데이터프레임을 갱신하며 누적 과정을 보여줍니다.
    df = pd.DataFrame(rows)
    print(df)
    print("건수 : ", len(df))