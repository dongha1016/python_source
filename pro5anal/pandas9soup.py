# BeautifulSoup 객체를 이용한 웹 문서 처리
import requests
from bs4 import BeautifulSoup

# 대상 웹사이트 주소와 접속 시 브라우저처럼 보이게 하는 Header 설정
baseurl = "https://www.naver.com"
headers = {"User-Agent":"Mozilla/5.0"}

# requests.get(): 지정한 URL에 접속하여 페이지 정보를 가져옵니다.
source = requests.get(baseurl, headers=headers)
print(source, type(source))     # <Response [200]>: 접속 성공을 의미하는 응답 객체
print(source.status_code)       # HTTP 상태 코드 (200: 성공, 404: 페이지 없음, 500: 서버 오류 등)

# BeautifulSoup(데이터, 파서): 
# 단순 텍스트(source.text)를 'lxml' 파서를 통해 트리 구조의 객체로 변환합니다.
# lxml은 속도가 빠르고 유연하여 대규모 데이터 처리에 유리합니다.
conv_data = BeautifulSoup(source.text, 'lxml')

# [데이터 추출 과정]
# .find_all('a'): 문서 내의 모든 <a> (하이퍼링크) 태그를 리스트 형태로 수집합니다.
for atag in conv_data.find_all('a'):
    # .get('href'): <a> 태그 안에 포함된 링크 주소 속성값(href)을 가져옵니다.
    href = atag.get('href')
    
    # .get_text(): 태그 사이에 있는 실제 텍스트 내용을 추출합니다.
    # string=True: 태그 안에 자식 태그가 있더라도 문자열만 골라내는 옵션입니다.
    title = atag.get_text(string=True)
    
    # 제목(title)이 비어있지 않은 경우에만 출력 (가독성 확보)
    if title:
        print(href)   # 연결된 URL 출력
        print(title)  # 화면에 표시되는 텍스트 출력
        print('================')