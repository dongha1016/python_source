a = 1
while a <= 5:
    print(a, end = ' ') # 무한루프(조건이 계속 참일 경우)
    a = a + 1
else: 
    print('수행성공')

print()

i=1
while i<=3:
    j=1
    while j<=4:
        print('i=' + str(i) + '/j=' + str(j))
        j = j + 1
    i = i + 1

print('1 ~ 100 사이의 정수 중 3의 배수의 합 ---')

su = 1; hap = 0
while su <= 100:
    if su % 3 == 0:
        hap += su
    su += 1

print('합은', hap)

print()

colors = ["빨강", "파랑", "노랑", "검정"]

num = 0 
# while num < 3:
while num < len(colors):
    print(colors[num])
    num += 1

print("\n별찍기---------")

i = 1
while i <= 10:
    j=1
    msg = ''
    while j<=i:
        msg += "*" # str에 *의 모양을 추가
        j += 1
    print(msg)
    i += 1

print('if 블럭 내 while 블럭 사용 -----')

import time # 
sw = input('폭탄 스위치를 누를까요?[y/n]')
print("sw :", sw)
if sw == 'Y' or sw == 'y':
    count = 5
    while 1 <= count:
        print('%d초 남았습니다.'%count)
        time.sleep(1) # 1초 후 다음 문장을 실행해라
        count -= 1
    print('폭발')
    # pass: 아무것도 수행하지 말아라(빈 내용으로 놔두면 안됨)
elif sw == 'N' or sw == 'n':
    print('작업취소')
else: 
    print('y 또는 n을 누르세요')

print('\nContinue와 Break ---')

a = 0
while a < 10:
    a += 1
    if a == 3 or a == 5: continue # 아래 코드를 무시하고 while로 다시 올라감
    if a == 7: break # while 반복문 탈출
    print(a)
else: 
    print('정상 종료') # 조건에 의해 탈출하면 실행(a < 10)

print('while 수행 후 %d'%a)

print('\n키보드로 숫자를 입력받아 홀수 짝수 확인하기(무한반복)')

while True:    # True, 1, 100, -12, 4.5 => 참
    mysu = int(input('확인할 숫자 입력(예:5):'))
    if mysu ==0:
        print("프로그램 종료")
        break
    elif mysu % 2 == 0:
        print("%d: 짝수"%mysu)
    else: print("%d: 홀수"%mysu)

print('end')