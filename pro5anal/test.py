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

print("조건3")
print(np.array(a[1,:]))
print(np.array(a[:, 4]))
print("조건4")
print(np.array(a[2:5, 2:5]))

print("문제2-2 조건1")
matrix = np.zeros((6, 4))
random_starts = np.random.randint(20, 101, 6)
matrix1 = random_starts.reshape(6, 1)
incre = np.arange(4)
# 3. 조건1: 각 행에 1씩 증가하는 값 채우기
# [0, 1, 2, 3] 형태의 배열을 더해 각 행을 완성
matrix = matrix1 + incre
print(matrix)

print("문제2-2 조건2")
matrix[0] = 1000
matrix[5] = 6000
print(matrix)

print("문제3번")
li = np.random.randn(4, 5)
print(li)
print("평균 : ", np.mean(li))
print("합계 : ", np.sum(li))
print("표준편차 : ", np.std(li))
print("분산 : ", np.var(li))
print("최댓값 : ", np.max(li))
print("최솟값 : ", np.min(li))
print("중앙값: ", np.median(li))
print("1사분위수 : ", np.percentile(li, 25))
print("2사분위수 : ", np.percentile(li, 50))
print("3사분위수 : ", np.percentile(li, 75))
print("요소값 누적합 : ", np.cumsum(li))

print("추가 문제 1번")
a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30])
print(a*b)
x = (a*b).reshape(1, 9)
x = list(np.where(x >= 30))
print(x)
