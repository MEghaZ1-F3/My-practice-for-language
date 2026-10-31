class Vector:
    def __init__(self, i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self,other):
        return Vector(self.i + other.i,self.j + other.j,self.k + other.k)

    def __sub__(self,other):
        return Vector(self.i - other.i,self.j - other.j,self.k + other.k)

    def __mul__(self,other):
        return Vector (self.i * other.i,self.j * other.j,self.k + other.k)

    def __str__(self):
        return f"Vector ({self.i}i , {self.j}j , {self.k}k)"
u1 = Vector(4,6,8)
u2 = Vector(3,7,5)
add = u1 + u2
sub = u1 - u2
mul = u1 * u2
print(add)
print(sub)
print(mul)