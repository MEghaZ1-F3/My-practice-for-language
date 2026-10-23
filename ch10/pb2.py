class Calculator:
    def __init__(self,n):
        self.n = n


    def square(self):
        print(f" The squre of {self.n} : {self.n**2}")
    def qube(self):
        print(f" The qube of {self.n} : {self.n**3}")


w= Calculator(5)
w.square()
w.qube()
w.squareroot()