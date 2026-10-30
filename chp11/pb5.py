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

    def __mul__(self,other):
        return Vector(self.i * other.i,self.j * other.j,self.k + other.k)

u1 = Vector(4,6,8)
u2 = Vector(3,7,5)
add = u1 + u2
sub = u1 - u2
mul = u1 * u2
add.Ndimentionalvec()
sub.Ndimentionalvec()
mul.Ndimentionalvec()