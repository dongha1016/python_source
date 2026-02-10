from abc import *

class Employee(metaclass=ABCMeta):
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def data_print(self):  
        pass

    def irumnai_print(self):
        print(f'이름 : {self.irum}, 나이 : {self.nai},', end = ' ')

class Temporary(Employee):
    ildang = 0
    ilsu = 0
    def __init__(self, irum, nai, ilsu, ildang):
        self.ilsu = ilsu
        self.ildang = ildang
        super().__init__(irum, nai)

    def pay(self):
        pay1 = self.ilsu * self.ildang
        return pay1

    def data_print(self):
        print(f"이름: {self.irum}, 나이: {self.nai}, 월급:{self.pay()}")


class Regular(Employee):
    salary = 0
    def __init__(self, irum, nai, salary):
        self.salary = salary
        super().__init__(irum, nai)
    
    def pay(self):
        pay1 = self.salary
        return pay1

    def data_print(self):
        print(f"이름: {self.irum} 나이: {self.nai} 월급:{self.pay()}")


class Salesman(Regular):
    sales = 0 
    COMMISSION = 0
    def __init__(self, irum, nai, salary, siljuk, susu):
        self.siljuk = siljuk
        self.susu = susu
        super().__init__(irum, nai, salary)
    
    def pay(self):
        pay1 = self.salary + self.siljuk * self.susu
        return pay1

    def data_print(self):
        print(f"이름: {self.irum} 나이: {self.nai} 월급:{int(self.pay())}")

t = Temporary('홍길동', 25, 20, 15000)
r = Regular('한국인', 27, 3500000)
s = Salesman('손오공', 29, 1200000, 5000000, 0.25)

t.data_print()
r.data_print()
s.data_print()