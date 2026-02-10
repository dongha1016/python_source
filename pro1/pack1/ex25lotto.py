import random

class LottoBall:
    def __init__(self, num):
        self.num = num

class LottoMachine:
    def __init__(self):
        self.ballList = []
        for i in range(1, 46):
            self.ballList.append(LottoBall(i))  # 클래스의 포함관계

    def selectBalls(self):
        # for a in range(45):
        #     print(self.ballList[a].num, end = ' ') # 번호 잘 들어 가있는지 먼저 확인
        # print()

        random.shuffle(self.ballList) # 45개 섞어두기
        # for a in range(45):
        #     print(self.ballList[a].num, end = ' ') 
        return self.ballList[0:6]

class LottoUI:
    def __init__(self):
        self.machine = LottoMachine()   # 포함 관계

    def playLotto(self):
        input('로또를 시작하려면 엔터키를 누르세요')
        selectedBalls = self.machine.selectBalls()
        for ball in selectedBalls:
            print(f'{ball.num}')

if __name__ == '__main__':
#     machine = LottoMachine()
#     print(machine.selectBalls())
    # lot = LottoUI()
    # lot.playLotto()
    LottoUI().playLotto()   # 위와 실행결과가 같음