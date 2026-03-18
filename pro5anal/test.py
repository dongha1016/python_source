import numpy as np
import random

li = np.random.randn(20).reshape(5, 4)
print(li)
print(np.sum(li[0]))

for i in range(0, 5):
    print(i+1, "행 합계", np.sum(li[i]))
    print(i+1, "행 최대값", np.max(li[i]))


print("##########문제 2번###########")
#  문2-1) 6행 6열의 다차원 zero 행렬 객체를 생성한 후 다음과 같이 indexing 하시오.
#    조건1> 36개의 셀에 1~36까지 정수 채우기
#    조건2> 2번째 행 전체 원소 출력하기 
#               출력 결과 : [ 7.   8.   9.  10.  11.  12.]
#    조건3> 5번째 열 전체 원소 출력하기
#               출력결과 : [ 5. 11. 17. 23. 29. 35.]
#    조건4> 15~29 까지 아래 처럼 출력하기
#               출력결과 : 
#               [[15.  16.  17.]
#               [21.  22.  23]
#               [27.  28.  29.]]

a = np.zeros((6,6))
a = np.arange(1, 37).reshape(6,6)
print(a)

print(a[1])
print(a[5], axis = 1)