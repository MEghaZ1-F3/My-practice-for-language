class Calculator:
    def __init__(self,n):
        self.n = n


    def square(self):
        print(f" The squre of {self.n} : {self.n**2}")
    def qube(self):
        print(f" The qube of {self.n} : {self.n**3}")
    def squareroot(self):
        print(f" The squreroot of {self.n} : {self.n**1/2}")

w= Calculator(5)
w.square()
w.qube()
w.squareroot()