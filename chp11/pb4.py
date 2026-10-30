class Complex:
    def __init__(self,r,i):
        self.r= r
        self.i= i

    def __add__(self,other):
        return Complex(self.r + other.r , self.i + other.i )
    def __mul__(self, other):
        return Complex(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)
    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 =  Complex(1,2)
c2 =  Complex(3,4)
c3 =  Complex(5,6)
print(c1 + c2 + c3)
print(c1 * c2 * c3)