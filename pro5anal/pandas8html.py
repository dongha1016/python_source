import xml.etree.ElementTree as etree

# [로컬 XML 파일 파싱]
# etree.parse(): 파일 경로를 통해 XML 문서를 읽어 트리 구조로 변환합니다.
xmlfile = etree.parse("my.xml")

print(xmlfile, type(xmlfile))
# getroot(): XML의 가장 바깥쪽 태그(최상위 요소)를 가져옵니다.
root = xmlfile.getroot()    # 예: <items> ... </items>
print(root.tag)
print(root[0].tag)          # root 요소의 첫 번째 자식 노드명 얻기
print(root[0][0].tag)       # 첫 번째 자식의 첫 번째 손자 노드명 얻기

print()
# .find(): 특정 태그를 찾아 해당 노드로 이동합니다.
# .text: 태그 사이에 있는 실제 문자열 데이터를 가져옵니다.
myname = root.find('item').find("name").text
mytel = root.find('item').find("tel").text
print(myname + " " + mytel)

print("\n===============기상청 제공 XML 자료 읽기================")
import requests

# 실시간 기상 정보 XML URL
url = "https://www.kma.go.kr/XML/weather/sfc_web_map.xml"
headers = {"User-Agent":"Mozilla/5.0"}

# requests를 이용해 웹상의 XML 데이터를 가져옵니다.
res = requests.get(url, headers=headers)
res.raise_for_status()    # 200 OK가 아닐 경우 에러를 발생시켜 중단함
print(res.text, type(res.text))     # 서버로부터 받은 데이터는 아직 '문자열(str)' 상태임

# etree.fromstring(): 문자열 형태의 XML 데이터를 메모리상의 트리 객체로 변환합니다.
root = etree.fromstring(res.text)    
print(root)               # 출력 예: <Element '{current}current' ...>

# [중요: XML 네임스페이스 제거 처리]
# 많은 공공데이터 XML은 태그명 앞에 {url} 형태의 네임스페이스가 붙어 있어 접근이 까다롭습니다.
print("{current} namespace 제거")
for elem in root.iter():
    # 태그명에 '}'가 포함되어 있다면 (즉, 네임스페이스가 있다면)
    if '}' in elem.tag:
        # '}'를 기준으로 잘라 뒷부분(실제 태그명)만 다시 저장합니다.
        elem.tag = elem.tag.split('}', 1)[1]    
        # 예: {current}weather => weather 

# 네임스페이스가 제거되었으므로 직관적인 이름으로 찾기 가능
weather = root.find('weather')

# .get('속성명'): <weather year="2026" ...> 처럼 태그 안에 포함된 속성값을 읽습니다.
year = weather.get('year')  
month = weather.get('month')
day = weather.get('day')
hour = weather.get('hour')

print(f"{year}년 {month}월 {day}일 {hour}시 현재 예보")

# .findall(): 일치하는 모든 태그를 리스트 형태로 가져옵니다. (다수의 지역 정보 처리)
# 각 지역(local tag)을 하나씩 순회하며 데이터 추출
for local in weather.findall('local'):
    # .text: 태그 사이의 지명(서울, 부산 등) 추출 후 앞뒤 공백 제거(.strip())
    name = local.text.strip()   
    # .get('ta'): 해당 지역의 기온(ta) 속성값 추출
    ta = local.get('ta')        
    print(f'{name} 지역 온도는 {ta}')