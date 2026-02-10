class ElecProduct:
    volume = 0
    def volumeControl(self, volume):
        self.volume = volume


class ElecTv(ElecProduct):
    def volumeControl(self, volume):
        print('TV: ' + volume)

class ElecRadio(ElecProduct):
    def volumeControl(self, volume):
        print('Elec:' + volume)

tv1 = ElecTv()
radio1 = ElecRadio()

product = input("어떤거 조작할건가요? : ")
vol = input("소리를 얼마로 킬까요? : ")

if product == '티비':
    tv1.volumeControl(vol)
elif product == '라디오':
    radio1.volumeControl(vol)
else: print("제품이 없습니다.")

