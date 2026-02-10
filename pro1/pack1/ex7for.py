
for i in {1,2,3,4,5}:
    print(i , end = ' ')

print('분산과 표준편차 구하기')

# numbers = [1,3,5,7,9] # 합은 25, 평균은 5.0
# numbers = [3,4,5,6,7] # 합은 25, 평균은 5.0
numbers = [-3,4,5,7,12] # 합은 25, 평균은 5.0

total = 0
for a in numbers:
    total += a
print(f"합은 {total}, 평균은 {total/len(numbers)}")
avg = total/len(numbers)

hap = 0 
for i in numbers:
    hap += (i - avg) ** 2 # 편차제곱의 합을 구하기 위함
print(f"편차제곱의 합은 {hap}")

vari = hap / len(numbers)
print(f'분산은 {vari}')
print(f'표준편차는 {(vari)**(0.5)}')

print()
colors = ['r', 'g', 'b']
for v in colors:
    print(v, end = ' ')


print('iter(): 반복 가능한 객체를 하나씩 꺼낼 수 있는 상태로 만들어 주는 함수')
iterator = iter(colors)
for v in iterator:
    print(v, end = ', ')
# r, g, b,

print()

for idx, d in enumerate(colors): # enumerate: index와 값을 반환
    print(idx, ' ', d)
# 0   r
# 1   g
# 2   b

print()

print('사전형-----')

datas = {'python':'만능언어', 'java':'웹용언어', 'mariadb':'RDBMS'}

for i in datas.items():
    print(i[0], '~~', i[1]) # i[0] = key / i[1] = value

for k, v in datas.items():
    print(k, ' ~~ ', v) 
# python  ~~  만능언어
# java  ~~  웹용언어
# mariadb  ~~  RDBMS

for k in datas.keys(): # key만 출력
    print(k, end = ' ')

print()
for v in datas.values(): # value만 출력
    print(v, end = ' ')

print('다중 for문===========')

for n in [2, 3]:
    print('--{}단--'.format(n))
    for i in [1,2,3,4,5,6,7,8,9]:
        print('{} * {} = {}'.format(n, i, n*i))

print('continue와 break -------')
nums = [1,2,3,4,5]
for i in nums:
    if i == 2: continue
    if i == 4: break
    print(i, end = ' ')
else: print('정상종료')

print('\n정규 표현식 + for')

str = """우리도 독일 고급창호 할래요"…하이엔드에 치이는 국4내 건자재
 독일 에 동일한 호텔이6 있어요 엔드게K임"""

import re # 정규표현식 모듈
str2 = re.sub(r'[^가-힣\s]', '', str) # 한글과 공백 이외의 문자는 공백으로 대체하라
print(str2)
str3 = str2.split(' ') # 공백을 구분자로 문자열 분리
print(str3)

cou = {} 
for i in str3:
    if i in cou:
        cou[i] += 1    # 같은 단어가 있으면 누적
    else:
        cou[i] = 1 # 최초 단어인 경우 '단어':1
    
print(cou)

for test_ss in ['111-1234', '일이삼=일이삼사', '222-1234', '333&1234']:
    if re.match(r'^\d{3}-\d{4}$', test_ss):
    # 시작(^)은 숫자로 3자리 - 숫자로 4자리 마지막은 숫자로 끝내기($)
        print(test_ss, '전화번호 맞아요')
    else:
        print(test_ss, '전화번호 아니야')

print('comprehension : 반복문 + 조건문 + 값 생성을 한줄로 표현')    
a = [1,2,3,4,5,6,7,8,9,10]
li = []
for i in a:
    if i % 2 == 0:
        li.append(i)
print(li)

print(list(i for i in a if i % 2 == 0)) # 위와 동일한 결과값을 출력

datas = [1, 2, 'a', True, 3.0]
li2 = [i * i for i in datas if type(i) == int]
print(li2)

id_name = {1:'tom', 2:'oscar'}
name_id = {val:key for key, val in id_name.items()} # key, value의 값을 Swap
print(name_id)

print()
print([1,2,3])
print(*[1,2,3]) # * : unpack => 리스트 형태를 풀어주는 것

aa = [(1,2), (3,4), (5,6)]
for a, b in aa:
    print(a + b)

print(*[a + b for a, b in aa], sep = ' ')
print([a + b for a, b in aa])

print('\n수열 생성 : range')

print(list(range(1,6))) # [1,2,3,4,5]
print(tuple(range(1,6,2))) # (1,3,5) => 2씩 증가
print(list(range(-10, -100, -20))) # [-10, -30, -50, -70, -90]
print(set(range(1,6,2))) # {1, 3, 5}

for i in range(6): # 0부터 5까지
    print(i, end = ' ')
    
for _ in range(6): # _ : 변수를 쓰지 않음(단순 반복 위함)
    print('반복')

tot = 0
for i in range(1,11):
    tot += i
print('tot :', tot)
print('tot :', sum(range(1,11))) # sum() : 내장함수  

for i in range(1, 10):
    print(f'2 * {i} = {2 * i}') # 구구단 2단 출력


##################################################################

# for 문 : 2 ~ 9 구구단 출력

for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i}*{j}={i * j}', end = ' / ')
    print()
    
# for 문 : 주사위 두번 던져서 나온 수의 합이 4의 배수일 때 출력

for i in range(1, 7):
    for j in range(1, 7):
        if (i+j)%4 == 0:
           print(i, j, end = '/')













print('\nend')