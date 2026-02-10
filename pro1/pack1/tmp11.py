i = 0
while True:
    if i % 10 != 3: # 1번
        i += 1
        continue 

    if i > 100: break
    print(i, end = ' ')
    i += 1
    
print()

a = 0
while a < 10:
    a += 1
    if a == 3 or a == 5: continue # 아래 코드를 무시하고 while로 다시 올라감
    if a == 7: break # while 반복문 탈출
    print(a)
else: 
    print('정상 종료')