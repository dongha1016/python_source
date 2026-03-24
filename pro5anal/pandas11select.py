# CSS 셀렉터(Selector)를 이용한 데이터 추출
from bs4 import BeautifulSoup

html_page="""
<html>
<body>
<div id = "hello">
    <a href="https://www.naver.com">naver</a><br>
    <span>
        <a href="https://www.daum.net">daum</a><br>
    </span>
    <ul class="world">
        <li>안녕</li>
        <li>반가원</li>
    </ul>
</div>
<div id = "hi" class="good">  # (참고: 원본 코드의 따옴표 오타가 있어도 파서가 유연하게 처리함)
    두번째 div
</div>
</body>
</html>
"""
soup = BeautifulSoup(html_page, 'lxml')

# [select_one]: CSS 선택자로 단 하나의 요소만 찾습니다.
# "div#hello > a": id가 hello인 div 바로 아래(직계 자식)에 있는 a 태그를 의미합니다.
aa = soup.select_one("div#hello > a")
print('aa : ', aa, ' ', aa.string)

print()
# [select]: 조건에 맞는 모든 요소를 리스트 형태로 반환합니다.
# "div#hello ul.world > li": id가 hello인 div 안의, class가 world인 ul 밑에 있는 li 태그들
bb = soup.select("div#hello ul.world > li")
print('bb : ', bb)
for i in bb:
    print(i, ' ', i.text)

print("=======위키백과 사이트에서 이순신으로 검색된 자료 읽기======")

import requests
url = "https://ko.wikipedia.org/wiki/이순신"
headers = {"User-Agent":"Mozilla/5.0"}
wiki = requests.get(url=url, headers=headers)

soup = BeautifulSoup(wiki.text, 'html.parser')
# #mw-content-text p: 위키백과 본문 영역 내의 모든 문단(p) 태그 선택
result = soup.select("#mw-content-text p")

for s in result:
    # [데이터 정제: decompose]
    # 위키백과의 각주 번호([1], [2] 등)는 <sup> 태그 안에 들어있습니다.
    # decompose()는 해당 태그를 트리에서 완전히 '도려내어' 제거합니다.
    for sup in s.find_all("sup"):
        sup.decompose()

    # strip=True: 문단 앞뒤의 불필요한 공백을 제거하고 출력
    print(s.get_text(strip=True))


print("========교촌치킨 사이트에서 메뉴, 가격 자료 읽기=======")
import pandas as pd 
url = "https://kyochon.com/menu/chicken.asp"
headers = {"User-Agent":"Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup2 = BeautifulSoup(response.text, 'html.parser')

# [리스트 컴프리헨션을 이용한 데이터 수집]
# 상품명 추출: dl.txt 태그 안의 dt 태그 텍스트 수집
names = [tag.text.strip() for tag in soup2.select("dl.txt>dt")]

# 가격 추출 및 전처리:
# 1. 태그 텍스트 가져오기 -> 2. 콤마(,) 제거 -> 3. 정수형(int) 변환
prices = [int(tag.text.strip().replace(',','')) for tag in soup2.select("p.money strong")]

# [수집된 리스트를 데이터프레임으로 변환]
df = pd.DataFrame({"상품명":names, "가격":prices})
print(df.head(3))

# [기초 통계 분석]
print(f"가격 평균 : {df['가격'].mean():.2f}")
print(f"가격 표준편차 : {df['가격'].std():.2f}")

# [변동계수(CV) 계산]
# 표준편차를 평균으로 나눈 값으로, 데이터의 상대적인 흩어짐 정도를 판단합니다.
cv = df["가격"].std() / df['가격'].mean() * 100
print(f"가격 변동계수(CV) : {cv:.2f}%")
# 해석 : 가격 변동계수가 약 28.31%라면 가격대 형성이 비교적 균일한 편임을 시사합니다.