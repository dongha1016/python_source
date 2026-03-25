print("====================1번=======================")
import numpy as np
import pymysql
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import MySQLdb
import sys
import koreanize_matplotlib # matplotlib 그래프에서 한글 폰트가 깨지는 것을 방지함
import csv
data = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(data[::-1, ::-1])


print("====================2번=======================")



print("====================3번=======================")

data = {
    'product':['아메리카노','카페라떼','카페모카'],
    'maker':['스벅','이디아','엔젤리너스'],
    'price':[5000,5500,6000]
}
df = pd.DataFrame(data)
# df.('test', conn, if_exists='append',)

# 1) to_sql
# 2) index = False

print("====================4번=======================")

df = pd.DataFrame(np.arange(12).reshape(4,3), index = ['1월', '2월', '3월', '4월'],
                columns = ['강남', '강북', '서초'])

print(df)

print("====================5번=======================")

# plt.show()

print("====================6번=======================")

# data = DataFrame(items)
# data.to_csv("test.csv", index=False, header=False)

print("====================7번=======================")

frame = DataFrame({'bun':[1,2,3,4], 
                'irum':['aa','bb','cc','dd']},
                index=['a','b', 'c','d'])
print(frame.T)
frame2 = frame.drop('d')
print(frame2)

print("====================8번=======================")

df = pd.read_csv('extest.csv', header=None, names=['a', 'b', 'c', 'd'])
print(df)

print("====================9번=======================")

data = {
    'juso':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon':[23, 25, 15]
}
df = DataFrame(data)
results = Series([x.split()[0] for x in df.juso])
print(results)

print("====================10번=======================")

# Broadcasting(브로드캐스팅)

print("====================11번=======================")

import MySQLdb
import pandas as pd
import numpy as np

def main():
    CONFIG = {"host": "127.0.0.1", 
              "user": "root", 
              "passwd": "123", 
              "db": "test", 
              "port": 3306, 
              "charset": "utf8" }

    conn = MySQLdb.connect(**CONFIG)
        
    sql = "select jikwonpay from jikwon j left join gogek g on j.jikwonno = g.gogekdamsano where gogekdamsano IS NULL"
    
    df = pd.read_sql(sql, conn)
    
    if not df.empty:
        count = len(df)
        mean_pay = df['jikwonpay'].mean()
        std_pay = df['jikwonpay'].std()
        
        print(f"{count}")
        print(f"{mean_pay:.2f}")
        print(f"{std_pay:.2f}")
    
    conn.close()
   
if __name__ == "__main__":
    main()


print("====================12번=======================")

df = DataFrame(np.random.randn(9, 4), columns=['가격1', '가격2', '가격3', '가격4'])

print(df)
print(df.mean())

print("====================13번=======================")

data = {
        "a": [80, 90, 70, 30], 
        "b": [90, 70, 60, 40], 
        "c": [90, 60, 80, 70]
        }

df = pd.DataFrame(data)
df.columns = ['국어', '영어', '수학']
print(df['수학'])
print(df['수학'].std())
print(df[['국어', '영어']])

# print("====================14번=======================")

# x = np.random.normal(0, 1, 1000)
# plt.hist(x, bins=20, alpha=0.9)
# plt.title('good')
# plt.show()

# print("====================15번=======================")

# df = pd.read_csv('sales_data.csv')  
# pframe = df.pivot_table(values='판매수량', index='날짜', columns='제품')
# print(pframe)