# JSON 자료 : XML에 비해 경량이며, 키-값(Key-Value)과 배열 개념으로 처리 가능
import json

# [파이썬 데이터 생성]
dict = {'name':'tom', 'age':25, 'score':['90', '80', '88']}
print(dict, type(dict))

print('json 인코딩 : dict -> str ====')
# json.dumps(): 파이썬 객체(dict, list 등)를 JSON 형식의 문자열로 변환합니다.
str_val = json.dumps(dict)
# indent=4: 사람이 읽기 좋게 들여쓰기를 추가하여 출력합니다.
str_val = json.dumps(dict, indent=4)
print(str_val, type(str_val))    # 결과는 <class 'str'> (텍스트 데이터)
print(str_val[0:20])

print('json 디코딩 : str -> dict ==== ')
# json.loads(): JSON 문자열을 다시 파이썬의 딕셔너리나 리스트로 복원합니다.
json_val = json.loads(str_val)
print(type(json_val))            # 결과는 <class 'dict'> (데이터 추출 가능 상태)
print(json_val['name'])

# 딕셔너리의 키(Key)들만 순회
for k in json_val.keys():
    print(k)

# 딕셔너리의 값(Value)들만 순회
for v in json_val.values():
    print(v)

print("\n서울시 제공 도서관 정보 JSON 샘플 자료(5개) 읽기")
import urllib.request as req

# JSON 형식의 데이터를 제공하는 API URL
url = "http://openapi.seoul.go.kr:8088/sample/json/SeoulLibraryTimeInfo/1/5/"
# 웹 데이터를 읽어와서 문자열로 디코딩
plainText = req.urlopen(url).read().decode()

# 문자열을 파이썬 객체(딕셔너리)로 변환
jsonData = json.loads(plainText)

# [계층적 접근] 
# JSON은 딕셔너리 안에 딕셔너리나 리스트가 중첩된 구조입니다.
# 대괄호를 이용해 단계별로 키를 찾아 들어갑니다.
print(jsonData["SeoulLibraryTimeInfo"]["row"][0]["LBRRY_NAME"])

# [dict의 get() 메서드 사용]
# get()을 사용하면 해당 키가 없을 경우 에러 대신 None을 반환하여 프로그램 중단을 방지합니다.
print()
datas = []
# 최상위 키 -> 하위 키 순서로 데이터를 좁혀 들어갑니다.
libData = jsonData.get("SeoulLibraryTimeInfo").get("row")

# 첫 번째 도서관 이름 확인
name = libData[0].get('LBRRY_NAME')
print(name)

# [리스트 순회하며 데이터 수집]
for ele in libData:
    name = ele.get('LBRRY_NAME')
    tel = ele.get('TEL_NO')
    addr = ele.get('ADRES')
    print(name, ' ', tel, ' ', addr)
    
    # 분석을 위해 리스트에 수집된 정보를 담습니다.
    datas.append([name, tel, addr])

# [Pandas를 이용한 최종 데이터 구조화]
import pandas as pd
# 수집된 리스트 데이터를 사용하여 데이터프레임 생성 (컬럼명 명시)
df = pd.DataFrame(datas, columns=['도서관명', '전화번호', '주소'])
print(df)