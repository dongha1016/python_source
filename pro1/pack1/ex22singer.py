class Singer:   # 초기화할게 없기 때문에 __init__은 없다
    title_song = "빛나라 대한민국"

    def sing(self):
        msg = "노래는"
        print(msg, self.title_song)