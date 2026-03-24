import pandas as pd 

# [중첩 딕셔너리로 데이터프레임 생성]
# 중첩된 키('apple', 'orange')는 컬럼명이 되고, 내부 키('count', 'price')는 행 인덱스가 됩니다.
items = {
    'apple':{'count':10, 'price':1500,},
    'orange':{'count':5, 'price':800,}   
}

df = pd.DataFrame(items)
print(df)

# [DataFrame의 다양한 출력 및 저장]

# 1. 클립보드 저장: 현재 데이터프레임을 복사합니다. 
# 이 코드를 실행한 후 엑셀이나 메모장에 '붙여넣기(Ctrl+V)'를 하면 표가 그대로 들어갑니다.
df.to_clipboard()

# 2. HTML 변환: 웹 페이지에서 표를 보여줄 때 사용하는 <table> 태그 형태로 출력합니다.
print(df.to_html())

# 3. JSON 변환: 웹 API 통신이나 NoSQL 데이터베이스에 저장할 때 주로 사용하는 형식입니다.
print(df.to_json())

# [CSV 파일 저장 옵션 비교]
# sep=',': 쉼표로 구분하여 저장
df.to_csv('result1.csv', sep=',')

# index=False: 행 인덱스(count, price)를 제외하고 데이터만 저장합니다. (실무에서 가장 많이 쓰임)
df.to_csv('result2.csv', sep=',', index=False)
# 결과 예시:
# apple,orange
# 10,5
# 1500,800

# header=False: 컬럼명(apple, orange)까지 제외하고 순수 수치 데이터만 저장합니다.
df.to_csv('result3.csv', sep=',', index=False, header=False)
# 결과 예시:
# 10,5
# 1500,800

print()
# [전치(Transpose)와 인코딩]
df2 = df.T  # 행과 열을 바꿈 (과일명이 행 인덱스가 됨)
print(df2)

# encoding='utf-8-sig': 엑셀에서 CSV 파일을 열 때 한글이 깨지는 현상을 방지하는 인코딩 방식입니다.
df2.to_csv('result4.csv', sep=',', index=False, encoding='utf-8-sig')

# 저장한 파일 다시 읽어오기
redata = pd.read_csv('result4.csv')
print(redata)

print('\n=============== 엑셀 관련 ==============')
df3 = pd.DataFrame({
    'name':['Alice', 'Bob', 'Oscar'],
    'age':[24, 22, 29],
    'city':['seoul', 'suwon', 'incheon']
})
print(df3)

# [엑셀 파일 저장]
# sheet_name: 엑셀 파일 내의 시트 이름을 지정합니다.
df3.to_excel('result.xlsx', index=False, sheet_name='work1')

# [엑셀 파일 읽기]
# ExcelFile 객체를 사용하면 하나의 엑셀 파일 안에 있는 여러 시트를 효율적으로 관리할 수 있습니다.
exdf = pd.ExcelFile('result.xlsx')
# 파일에 포함된 모든 시트의 이름을 리스트로 확인
print(exdf.sheet_names)

print("sheet별로 읽기")
# parse(): 특정 시트의 데이터를 데이터프레임으로 변환하여 가져옵니다.
df4 = exdf.parse("work1")
print(df4)