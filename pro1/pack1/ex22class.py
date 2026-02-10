# 클래스는 새로운 타입을 만들어 자원을 공유

# ex22singer.py 
class Singer:   # 초기화할게 없기 때문에 __init__은 없다
    title_song = "빛나라 대한민국"

    def sing(self):
        msg = "노래는"
        print(msg, self.title_song)

from ex22singer import Singer
bts = Singer()  # 생상자 호출에 객체 생성 후 주소를 bts에 치환
bts.sing() # 처음에는 bts의 title_song이 없기 때문에 Singer의 title_song을 가져옴
print(type(bts))
bts.title_song = 'Permission to Dance'
bts.sing()
bts.co = '빅히트'
print('소속사 :', bts.co)
print()

ive = Singer()
ive.sing()
print(type(ive))
# print('소속사 :', ive.co) # ive는 co를 갖고 있지 않음

Singer.title_song = "아 대한민국" # 프로토타입(원형 클래스)의 title_song을 변경
bts.sing()
ive.sing()

niceGroup = ive
niceGroup.sing()    #ive - 동일 주소
