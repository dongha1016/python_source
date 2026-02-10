# pack1/ex15module - main
print('사용자 정의 모듈 처리하기')
s = 20 # 뭔가를 하다가 모듈을 가져오기

print('\n경로 지정 방법1 : import 모듈명')

# 같은 패키지에 있다고 하더라도 주메모리에 올리지 않으면 인식 못함
import pack1.mymod1
print(dir(pack1.mymod1)) # mymod1의 멤버를 확인하는 것
print(pack1.mymod1.__file__) # 경로명과 모듈명
print(pack1.mymod1.__name__) # 모듈명
list1 = [1, 2]
list2 = [3, 4, 5]

pack1.mymod1.listHap(list1, list2)
if __name__ == '__main__': print('나는 메인모듈')
# 메인모듈은 실제로 파일을 실행시키는 모듈임

print('\n경로 지정 방법2 : from 모듈명 import 함수명(변수명)')

from pack1.mymod1 import kbs
# ctrl + spacebar : 변수명 보이게 하는 단축키
kbs()
from pack1.mymod1 import mbc, tot
mbc()
print(tot)

from pack1.mymod1 import *
print('tot:', tot)

from pack1.mymod1 import mbc as 엠비씨만세별명 # mbc 멤버를 'as'를 통해 별명으로 치환
엠비씨만세별명()

print('\n경로 지정 방법3 : import 하위패키지.모듈명')

import pack1.subpack.sbs
pack1.subpack.sbs.sbsMansae()
import pack1.subpack.sbs as nickname
nickname.sbsMansae()

print('\n경로 지정 방법4 : 현재 package와 동등한 다른 패키지 모듈 읽기')
from pack1_other import mymod2 
mymod2.hapFunc(4, 3)

# python -m pack1.ex15module => 동등한 패키지가 있는 경우 패키지 명시하여 실행
# 동등한 패키지보다는 subpackage를 활용하는 것을 추천

import mymod3
result = mymod3.gopFunc(4, 3)
print('path가 설정된 곳의 모듈 읽기 - result', result)

print('end')
