class Animal:
    def move(self):
        pass

class Dog(Animal):
    name = '개'
    def move(self):
        print('Dog Walk')

class Cat(Animal):  
    name = '고양이'
    def move(self):
        print('Cat Walk')
    
class Wolf(Dog, Cat):
    pass

class Fox(Cat, Dog):
    
    def move(self):
        print('Fox Walk')

    def foxMethod(self):
        print('Fox 고유 메소드')

animal = [Dog(), Cat(), Fox()]
for a in animal:
    a.move()