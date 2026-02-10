var1 = "안녕 파이썬" 
print(var1) # 주석

var1 = 5 
# 5라는 값이 주소를 갖고 기억장소의 어딘가에 저장되어 있음 => 이 주소값을 var1이 가짐
# var1 => 참조형 기억장소
# 들어오는 데이터로 타입을 결정함(C와는 다름)
var1 = 10
var1 = 5.6
print(var1)

var2 = var1
print(var1, var2)
var3 = 7
print(var1, var2, var3)
print(id(var1), id(var2), id(var3))
Var3 = 8
print(var3, Var3)

a = 5
b = a
c = 5
print(a, b, c)
print(a is b, a == b)
print(b is c, b == c)

aa = [5]
bb = [5]
print(aa, bb)
print(aa is bb, aa == bb)

print('---------') # print("------")

import keyword # 키워드 목록 확인용 모듈 읽기
print('예약어 목록:', keyword.kwlist)

print('type(자료형) 확인')
kbs = 9
print(isinstance(kbs, int))
print(isinstance(kbs, float))

print(5.1, type(5.1))

print(5.3, type(5.3))
print(3+4j, type(3+4j))
print(True, type(True))
print('good', type('good'))
print((1,), type((1,)))
print([1], type([1]))
print({1}, type({1}))
print({'k':1}, type({'k':1}))