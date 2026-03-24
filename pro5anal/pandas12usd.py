# 네이버 - 증권 - 시장지표 : 환율 값을 실시간 모니터링
import requests
from bs4 import BeautifulSoup
import time
import sys

# [출력 인코딩 설정] 
# Windows 환경의 터미널(CMD) 등에서 한글 깨짐 현상을 방지하기 위해 utf-8로 재설정합니다.
sys.stdout.reconfigure(encoding='utf8')

url = "https://finance.naver.com/marketindex/"
headers = {"User-Agent":"Mozilla/5.0"}

# 무한 루프를 통해 실시간 데이터를 지속적으로 수집합니다.
while(True):
    # 페이지 요청 및 파싱
    res = requests.get(url=url, headers=headers)
    # 네이버 금융은 EUC-KR 인코딩을 사용하는 경우가 많으므로 content를 사용하거나 
    # 별도의 인코딩 처리가 필요할 수 있지만, BeautifulSoup이 대부분 자동으로 처리합니다.
    soup = BeautifulSoup(res.content, 'html.parser')

    # [국가명 추출] h3 태그 안의 blind 클래스를 가진 span에서 '미국 USD' 텍스트를 가져옵니다.
    nation = soup.select_one("h3.h_lst span.blind").get_text(strip=True)
    # print(nation)   # 예: 미국 USD

    # [현재 환율값] .value 클래스를 가진 요소에서 숫자(예: 1,350.50)를 추출합니다.
    price = soup.select_one(".value").get_text(strip=True)
    
    # [통화 단위] .txt_krw 안의 blind 클래스에서 '원'이라는 단위를 가져옵니다.
    unit = soup.select_one(".txt_krw .blind").get_text(strip=True)

    # [변동 금액] 전일 대비 얼마나 오르거나 내렸는지 수치를 가져옵니다.
    change = soup.select_one(".change").get_text(strip=True)

    # [등락 상태] 
    # div.head_info.point_up (상승) 혹은 .point_dn (하락) 클래스 구조 내에서
    # 마지막 blind span 요소인 '상승' 또는 '하락' 텍스트를 추출합니다.
    updown = soup.select("div.head_info.point_up span.blind")[-1].get_text(strip=True)

    # 추출된 데이터를 보기 좋게 포맷팅하여 출력합니다.
    # .replace(' ', '')을 통해 '미국 USD' 사이의 공백을 제거하여 출력합니다.
    print(f"{nation.replace(' ', '')} // {price}{unit} // {updown} // {change}")
    
    # [대기 시간 설정] 
    # 서버에 과도한 부하를 주지 않기 위해, 그리고 실시간 변화를 관측하기 위해 5초의 간격을 둡니다.
    time.sleep(5)