# Module : 소스 코드의 재사용을 가능하게 하며
# 소스 코드를 하나의 이름 공간으로 구분하고 관리
# 하나의 파일은 하나의 모듈이 된다
# 표준 모듈, 사용자 작성 모듈, 제3자 모듈(third party)로 구분할 수 있음
print(print.__module__) # builtins이 모듈 안에 print가 있음

import sys
import math
print(sys.path) # import하기 전에는 에러가 있기 때문에 RAM으로 import 해야함
a = 5
if a > 7:
    sys.exit() # 응용프로그램의 강제 종료

print(math.pi) # math 모듈의 pi라는 멤버다를 확인

import calendar
calendar.setfirstweekday(6)
calendar.prmonth(2026,2)
del calendar 
# calendar.prmonth(2026,2) # calendar를 메모리에서 없어졌기 때문에 에러가 발생

import random

print(random.random()) # 0에서 1사이의 실수 난수
print(random.randrange(1, 10)) # 1부터 10까지의 정수 중 난수

from random import random, choice, randrange
# random 모듈(첫번째)에서 random 멤버(두 번째)를 가져온다
from random import * 
# random 모듈에 있는 모든 멤버를 가져옴
# 불필요하게 메모리 관리가 안되기 때문에 위 방법 추천

print(random()) # ~.random 이런식으로 쓸 필요 없음

print('end')
# 프로그램이 진행되는 동안 소스코드에 있는 데이터가 RAM 상에 부트되지만
# end를 만나면서 휘발성 데이터들이 사라짐
