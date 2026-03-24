# BeautifulSoup 객체 메소드 활용
from bs4 import BeautifulSoup

html_page = """
<html><body>
<h1>제목 태그</h1>
<p>웹문서 연습</p>
<p>원하는 자료 확인</p>
</body></html>
"""
print(type(html_page))          # <class 'str'> (단순 문자열)
# html.parser: 파이썬 기본 내장 파서로 별도 설치 없이 사용 가능합니다.
soup = BeautifulSoup(html_page, 'html.parser')
print(type(soup))               # <class 'bs4.BeautifulSoup'> (구조화된 객체)
print()

# 계층 구조(도트 연산자)를 이용한 접근
h1 = soup.html.body.h1
print("h1 : ", h1.string)
p1 = soup.html.body.p           # 동일한 태그가 여러 개일 경우 '가장 첫 번째' 태그를 가져옵니다.
print("p1 : ", p1.string)

# .next_sibling: 형제 노드(다음 요소)로 이동합니다. 
# 보통 태그 사이의 '줄바꿈(\n)'도 하나의 요소로 취급되므로 두 번 사용해야 다음 태그에 닿습니다.
p2 = p1.next_sibling.next_sibling
print("p2 : ", p2.string)

print('\n--find() method 사용-------')
html_page2 = """
<html><body>
<h1 id="title">제목 태그</h1>
<p>웹문서 연습</p>
<p id = "my" class = "our" >원하는 자료 확인</p>
</body></html>
"""
soup2 = BeautifulSoup(html_page2, 'html.parser')

# [find 메서드]: 조건에 맞는 단 하나의 태그만 반환합니다.
print(soup2.p, ' ', soup2.p.string)
print(soup2.find('p').string)

# id나 class 같은 속성(Attribute)을 이용하면 특정 요소를 정확히 찝어낼 수 있습니다.
print(soup2.find('p', id="my").string)
print(soup2.find(id = "title").string)
print(soup2.find(id = "my").string)

# class는 파이썬 예약어이므로 매개변수로 쓸 때 class_ (언더바 추가) 형식을 사용합니다.
print(soup2.find(class_="our").string)

# attrs 속성을 딕셔너리 형태로 전달하면 더 복잡한 조건도 검색 가능합니다.
print(soup2.find(attrs={"class":"our"}).string)
print(soup2.find(attrs={"id":"my"}).string)

print('\n--find_all(), findAll method 사용-------')
html_page3 = """
<html><body>
<h1 id="title">제목 태그</h1>
<p>웹문서 연습</p>
<p id = "my" class = "our" >원하는 자료 확인</p>
<div>
    <a href="https://www.naver.com">naver</a><br>
    <a href="https://www.daum.net">daum</a><br>
</div>
</body></html>
"""

soup3 = BeautifulSoup(html_page3, 'html.parser')
# 리스트 형태로 태그명을 전달하면 여러 종류의 태그를 한꺼번에 모두 찾아옵니다.
print(soup3.find_all(['a']))
print(soup3.find_all(['a', 'p']))
print()

links = soup3.find_all('a')
for i in links:
    # .attrs: 태그의 모든 속성을 딕셔너리 형태로 반환합니다. 
    # i.attrs['href'] 처럼 사용하여 링크 주소를 뽑아낼 수 있습니다.
    text = i.text       # 태그 내부의 텍스트 추출 (i.string과 유사하지만 자식 태그가 많을 때 유리)
    # print(text)

print('\n정규표현식 사용====')
import re
# re.compile: 특정 패턴(여기서는 https로 시작하는 문자열)을 가진 속성값만 필터링합니다.
links2 = soup3.find_all(href=re.compile(r'^https'))
for k in links2:
    print(k.attrs['href'])

print("====벅스 사이트 음악 순위 읽기====")
import requests
url = "https://music.bugs.co.kr/chart"
response = requests.get(url)
# print(response.text) # 전체 HTML 소스 확인용

bsoup = BeautifulSoup(response.text, 'html.parser')

# 벅스 차트에서 곡 정보는 보통 <td class="check"> 안의 <input> 태그 title 속성에 들어있습니다.
musics = bsoup.find_all("td", class_ = "check")

for idx, music in enumerate(musics):
    # music.input["title"]: td 태그 자식인 input 태그를 찾아 그 안의 title 속성값을 가져옵니다.
    # enumerate를 활용해 순위(index)를 매깁니다.
    print(f"{idx + 1}위) {music.input['title']}")