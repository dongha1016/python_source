# 기본 자료형 : int, float, bool, complex
# 묶음 자료형 : str, list, tuple, set, dict

# 1) str : 문자열 묶음 자료형. 순서 O / 수정 X

s = 'sequence'
print(s, id(s)) # sequence의 첫번째 문자가 주소를 저장하고 있음
print('길이: ', len(s)) # 8
print(s[0], s[2])
print('길이: ', s.find('e'), s.find('e', 3), s.rfind('e'))
# 1번째: e가 몇번째 있는가 / 2번째: 3번째부터 찾아 / 3번째: 뒤에서부터 찾아 

# 인덱싱, 슬라이싱
print(s[5]) # 인덱싱 - 변수명[순서], index는 0부터 출발
print(s[2:5]) # 슬라이싱(2, 3, 4번째)
print(s[:], ' ', s[0:len(s)], s[::1]) # 모든 인덱스 출력
print(s[0:7:2]) # 2칸씩 차이나는 인덱스를 0부터 7까지에서 출력

print(s[-1], ' ', s[-4:-1:1]) # 뒤에서부터 찾기
print(s)
s = 'sequenc' # 수정X, 변경 O
print(s, id(s))
s = 'bequence' 
print(s, id(s)) 
# 주소가 서로 다름(수정이 불가하기 때문)

print('---' * 10)

# 2) List : 다양한 종류의 자료 묶음형(순서O, 수정O, 중복O)

a = [1, 2, 3] # a는 1, 2, 3의 주소를 기억하고 있음
print(a, ',' ,a[0], ',', a[0:3])
b = [10, a, 10, 20.5, True, '문자열'] # int list int float boolean str
# 그림으로 한 번 정리해보기
print(b, ' ', b[1], ' ', b[1][0]) # b[1] => a
print()
family = ['엄마', '아빠', '나', '여동생']
print(id(family))
family.append('남동생') # 리스트의 가장 뒤에 추가
print(id(family)) # 앞에 주소와 동일한 것을 통해 수정이 가능한 것을 확인할 수 있음
family.remove("나") # 리스트에서 삭제
print(family)
family.insert(0, "할머니") # 리스트에 원하는 위치에 삽입
family.extend(['삼촌', '고모', '조카']) # 리스트 가장 뒤에 확장해서 추가
family += ['이모'] # 리스트 가장 뒤에 추가
print(family)
print(family.index('아빠')) # 아빠가 위치한 인덱스 출력
print('엄마' in family, '나' in family) # 해당 데이터가 있는지 bool 자료로 출력

family.remove('아빠') # 값에 의한 삭제
del family[2] # 순서에 의한 삭제
print(family) 

print()

kbs = ['123', '34', '234']
kbs.sort() # 문자열 정렬
print(kbs)

mbc = [123, 34, 234]
mbc.sort() # 숫자 정렬(내림차순)
print(mbc)
mbc.sort(reverse = True) # 숫자 정렬(내림차순)
print(mbc)

sbs = [123, 34, 234]
ytn = sorted(sbs)
print(sbs)
print(ytn)
# sorted와 sort의 차이: sort(원본이 바뀜), sorted(원본 유지, 새로운 기억장소에서 처리)

print('---------------'*3)
name = ['tom', 'james', 'oscar']
name2 = name
print(name, id(name))
print(name2, id(name2)) # name, name2 주소 동일

import copy 
name3 = copy.deepcopy(name) # 새로운 객체 name3를 만들어 name 리스트의 값만 복사
print(name3, id(name3)) # name과 name3의 주소 다름

name[0] = '길동'
print(name)
print(name2)
print(name3) # 별도의 기억장소이기 때문에 '길동'으로 변하지 않음

# 3) tuple : 리스트와 유사하나 읽기 전용(순서O, 수정X, 중복O)

t = (1,2,3,4)
t = 1,2,3,4 # 위와 동일(괄호 사용 추천)
print(t, type(t))

k = (1) # 튜플 아님
print(k, type(k)) # 정수형으로 인식
k = (1,) # 튜플
print(k, type(k)) # 튜플로 인식

print(t[0], ' ', t[0:2])
# t[0] = 77 # 'tuple' object does not support item assignment

# 튜플을 데이터는 변경 불가능하나 리스트로 변경 후 데이터 수정
imsi = list(t)
imsi[0] = 77
t = tuple(imsi)
print(t) 

# 4) set : 순서X, 중복X, 수정O

ss = {1, 2, 1, 3}
print(ss) # 1, 2, 3(중복된 값은 제거)
ss2 = {3, 4}
print(ss.union(ss2)) # 합집합
print(ss.intersection(ss2)) # 교집합
print(ss-ss2, ss | ss2, ss & ss2) # 차집합, 합집합, 교집합

# print(ss[0]) # 'set' object is not subscriptable => 순서가 없기 때문

ss.update({6, 7}) # set에 데이터 추가
print(ss)
ss.discard(7) # 값 삭제
print(ss)
ss.remove(6) # 값 삭제
print(ss)

# discard: 값이 있으면 지우고, 없으면 패스
# remove: 값이 있으면 지우고, 없으면 error 발생

# 중복을 제거하는 방법
li = ['aa', 'aa', 'bb', 'cc', 'aa']
print(li)
imsi = set(li)
li = list(imsi)
print(li) # ['bb', 'cc', 'aa'] => 순서가 없기 때문