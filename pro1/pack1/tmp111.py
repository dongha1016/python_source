i = 0
while i < 2: 
    k = int(input('연도입력 : '))
    if k % 4 == 0 and k % 100 != 0 or k % 400 == 0:
        print(f'{k}년은 윤년')
    else: print(f'{k}년은 평년')
    i += 1