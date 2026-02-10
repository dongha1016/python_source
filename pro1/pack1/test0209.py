#1번
print('***************1번**************')
li = [1, 2, 2, 2, 3, 4, 5, 5, 5, 2, 2]
im = set(li)
li = list(im)
print(li)

#2번
print('***************2번**************')

# 수행결과 : 1 2 3 4 5


# 이유: set에 대한 반복문으로 set은 중복을 허용하지 않기 때문에 다음과 같은 결과가 나온다

# 3번
num = 0
sum = 0

for i in range(1, 101):
    if i % 3 == 0 or i % 4 == 0 and i % 7 !=0:
        print(i, end = ' ') 
        num += 1
        sum += i
print()  
print(f'건수 : {num}')
print(f'배수의 총합: {sum}')

# 5번
print('***************5번**************')
print(5/3)
print(5//3)
print(5%3)

# 6번
print('***************6번**************')

a = 1.5; b = 2; c = 3;

def Kbs():
    a = 20  
    b = 30
    def Mbc():
        global c
        nonlocal b
        print('Mbc 내의 a:{}, b:{}, c:{}'.format(a, b, c))
        c = 40
        b = 50
    Mbc()

Kbs()

# 7번
print('***************7번**************')

*v1, v2, v3 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(v1)
print(v2)
print(v3)

# 8번
print('***************8번**************')

k = lambda m, n: m + n * 5
print(k(5,3))


# 9번
print('***************9번**************')
print(list(range(1, 6, 2)))

# 10번
print('***************10번**************')

# try:
#     aa = int(input())
#     bb = 10/aa
#     print(bb)
# except ZeroDivisionError as e :
#     print('This is Error : ', e)

# 11번
print('***************10번**************')

star = ''
for i in range(0, 10):
    print(star + '*'*(10-i))
    star += ' '

# 12번
print('***************12번**************')

i = 0
while i < 2: 
    k = int(input('연도입력 : '))
    if k % 4 == 0 and k % 100 != 0 or k % 400 == 0:
        print(f'{k}년은 윤년')
    else: print(f'{k}년은 평년')
    i += 1


# 13번
print('***************13번**************')
i = 0
while True:
    if i % 10 == 3: # 1번
        i += 1
        continue 

    if i > 100: break

    print(i, end = ' ')
    i += 1
    
print()


# 14번
print('***************14번**************')

i = 1
while i < 5:
    j = 1
    while j < 6:
        print(f'{2*i + 1} * {2*j-1} = {(2*i+1)*(2*j-1)}', end = ' ') 
        j += 1
    print()
    i += 1

# 15번
print('***************15번**************')

class Bicycle:
    name = '무명'
    wheel = 0
    price = 0
    def __init__(self, name, wheel, price):
        self.name = name
        self.wheel = wheel
        self.price = price
    
    def display(self):
        total_price = self.wheel * self.price
        print(f'{self.name}님 자전거 바퀴 가격 총액은 {total_price}입니다.')

gildong = Bicycle('길동', 2, 50000)
gildong.display()




