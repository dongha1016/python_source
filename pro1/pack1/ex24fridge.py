# 클래스의 포함관계 연습 - 냉장고 객체에 음식 객체 담기

class Fridge:
    isOpened = False 
    foods = []

    def open(self):
        self.isOpened = True
        print("냉장고 문을 열기")

    def close(self):
        self.isOpened = False
        print("냉장고 문을 닫기")
    
    def foodsList(self):    # 냉장고 문이 열린 경우 음식 확인 가능
        for f in self.foods:
            print(f' - {f.name} {f.expiry_date}')
        print()
    
    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print(f'냉장고에 {thing.name} 넣음')
            self.foodsList()
        else: 
            print('냉장고 문이 닫혀있음')

class FoodData:
    def __init__(self, name, expiry_date):
        self.name = name
        self.expiry_date = expiry_date

fObj = Fridge()
apple = FoodData('apple', '2026-8-1')
fObj.put(apple)    # 문이닫겨있기 때문에 사과가 들어가지 않음 => 포함관계 성립
fObj.open()     # 문열기
fObj.put(apple) # 사과 넣기
fObj.close()

cola = FoodData('cola', '2027-11-1')
fObj.open()     # 문열기
fObj.put(cola) # 콜라 넣기
fObj.close()