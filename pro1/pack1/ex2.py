# 연산자
v1 = 3
v1 = v2 = v3 = 5
print(v1, v2, v3)
print('출력1', end = ' ') # 줄바꿈 대신 '(공백)'으로 출력 이어가기 
print('출력2')
print('출력3')

v1, v2 = 10, 20
print(v1, v2)
v2, v1 = v1, v2 # 두 값을 변경

print('값 할당 : packing 연산')
v1  = 1, 2, 3, 4, 5 # v1 = (1, 2, 3, 4, 5)
v1  = [1, 2, 3, 4, 5] 
*v1, v2, v3 = [1, 2, 3, 4, 5]
print(v1, ' ', v2, ' ', v3) 


print(format(1.5678, '10.3f')) # 전체 10자리를 주고 소수점 3째자리까지만 출력
print('나는 나이가 %d 이다.'%23)
print('나는 나이가 %s 이다.'%'스물셋')
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100)) #나는 키가 177.700000이고, 에너지가 100%.
print('이름은 {0}, 나이는 {1}'.format('한국인', 33)) 
print('이름은 {}, 나이는 {}'.format('신선해', 33))
print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))

abc = 123
print(f"abc의 값은 {abc}")
print('본격적 연산 ----------') # \n(다음 줄로), \b(뒤로 한칸), \t(탭 키)
print(5 + 3, 5 - 3, 5 * 3, 5 / 3, 5 // 3, 5 % 3, 3 ** 3)

print(divmod(5, 3), ' ', 5 % 3)
result = 3 + 4 * 5 + (2 + 3) / 2
print(result) # 연산자 우선순위: () -> ** -> 단향 -> 산술(*,/ --> +,-) -> 관계 연산자 -> 논리 연산자(not -> and -> or) -> = 

print(5 > 3, 5==3, 5 != 3)
print(5 > 3 and 4 < 3, 5 > 3 or 4 < 3, not(5 >= 3))
print(True or False and False)
print(True and False or False)

print( 4 + 5 ) # 산술연산
print( '4' + "5" ) # 문자열 더하기 연산
print('한' + '국' + '만세')
print("한국" * 5) # 한국 5번 더하기

# 누적
a = 10
a = a+1 
a += 1 # 이런 표기 방법이 속도가 더 빠름(-=, *=, /=)
print(f"a는 {a}")
# 파이썬에는 증감 연산자 X(++, --)
print(--a) # 원래 a값(12)
print(-a)
print(a * -1)

# print(('1' + '1') + 1) # 타입 에러(문자열 + 정수)
print(int('1' + '1') + 1) # int('1' + '1') = 11(해당 코드는 형변환을 한 것) 
print(float('1' + '1') + 1) # 12.0
# print((1 + 1) + '1') # TypeError
print(str(1 + 1) + '1') # 21
print('boolean 처리 : ', bool(True), bool(False))
print(bool(1), bool(12.3), bool('ok'), bool([12])) 
# 모두 True => 데이터가 존재하기 때문
print(bool(0), bool(0.0), bool(''), bool([]), bool(None)) 
# 모두 False => 데이터가 존재하지 않기 때문

# r 선행문자
print('aa\tbb') 
print('aa\nbb')
print(r'aa\tbb') # 있는 그대로의 문자열 출력
print(r'aa\nbb')

