class Vector:
    def __init__(self, i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def Ndimentionalvec(self):
        print(f"{self.i}i , {self.j}j , {self.k}k")

    def __add__(self,other):
        return Vector(self.i + other.i,self.j + other.j,self.k + other.k)

    def __sub__(self,other):
        return Vector(self.i - other.i,self.j - other.j,self.k + other.k)

u1 = Vector(4,6,8)
u2 = Vector(3,7,5)
u3 = u1 + u2
u4 = u1 - u2
u3.Ndimentionalvec()
u4.Ndimentionalvec()