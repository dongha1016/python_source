# 매개변수 유형
# 위치 매개변수 : 인수와 순서대로 대응
# 기본값 매개변수 : 매개변수에 입력값이 없으면 기본값 사용 
# 키워드 매개변수 : 실인수와 가인수 간 동일 이름으로 대응
# 가변 매개변수 : 인수의 갯수가 동적인 경우

def showGugu(start, end=5): # 매개변수(또는 인수, 인자, args) => 가인수
    for dan in range(start, end+1):
        print(str(dan) + '단 출력')
        for i in range(1, 10):
            print(str(dan) + "*" + \
                  str(i) + "=" + str(dan * i), end = ' / ')
            # print문에 '/'를 통해 다음 행에 작성 
        print()

showGugu(2, 3) # 실인수 => 위치 매개변수
print()
showGugu(2) 
# 실인수 개수가 1개라 에러
# 함수에서 'end = 5' 값을 초기화해주면 에러 없음 => 기본값 매개변수
print()
showGugu(end=9, start=6) # 키워드 매개변수 
print()
showGugu(7, end=9) 

print('/n'+'*'*30+'\n')
# 가변 매개변수
def func1(*ar): # * : 여러개의 인자를 tuple로 묶어서 받겠다는 의미
    print(ar)
    for i in ar:
        print('밥 : ' + i)

func1('김밥', '비빔밥', '볶음밥')
func1('김밥')

print('/n'+'*'*30+'\n')

def func2(a, *ar):
# def func2(*ar, a) => 에러 발생
    print(a)
    print(ar)

func2('김밥', '비빔밥')
func2('김밥', '비빔밥', '볶음밥', '공기밥')

print('/n'+'*'*30+'\n')

def func3(w, h, **other): # ** : dict
    print(f'몸무게 : {w}, 키 : {h}')
    print(f'기타 : {other}')

func3(80, 180, irum = '신기루', nai = 23)
# func3(80, 180, {'irum'='신기루', nai = 23}) # 에러

print('/n'+'*'*30+'\n')

def func4(a, b, *c, **d): # 인자, 인자, 튜플, 사전형
    print(a, b)
    print(c)
    print(d)

func4(1, 2)
func4(1,2,3,4,5)
func4(1, 2, 3, 4, 5, kbs = 9, mbc = 11)

'''
1 2
()
{}
1 2
(3, 4, 5)
{}
1 2
(3, 4, 5)
{'kbs': 9, 'mbc': 11}
'''

print('\n'+'*'*30+'\n')
# type hint : 함수의 인자와 반환값에 type을 적어 가독성 향상
def typeFunc(num:int, data:list[str]) -> dict[str, int]: 
    # 구속력은 없으나 가독성 향상 / 반환값은 dict라는 것에 대한 설명
    print(num)
    print(data)
    result = {}
    for idx, item in enumerate(data, start=1):
        print(f'idx:{idx}, item:{item}')
        result[item] = idx # 사전형으로 변환
    return result

rdata = typeFunc(1.2, ['일', '이', '삼'])
print(rdata)

rdata = typeFunc("한개", [10,20,30]) # 문자로 주어도 에러가 있는 건 아님
print(rdata)