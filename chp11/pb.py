class vector1D:
    def __init__(self,x):
        self.x= x
    def vec1D(self):
        print(f"value of x axis: {self.x}i")

    def __add__(self,other):
        return vector1D(self.x + other.x)

class vector2D(vector1D):
    def __init__(self,x,y):
        super().__init__(x)
        self.y= y
    def vec2D(self):
        print(f"value of x axis and y axis : {self.x}i + {self.y}k")

    def __add__(self,other):
        return vector2D(self.x + other.x,self.y + other.y)
class vector3D(vector2D):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z= z
    def vec3D(self):
        print(f"value of x axis and y axis and z axis : {self.x}i + {self.y}j + {self.z}k")

    def __add__(self,other):
        return vector3D(self.x + other.x,self.y + other.y,self.z + other.z)

v1 = vector3D(5,6,8)
v2 = vector3D(4,8,4)
v3 = v1 + v2
v3.vec3D()


a1 = vector1D(5)
a2 = vector1D(10)
a3 = a1 + a2
a3.vec1D()


b1 = vector2D(3, 4)
b2 = vector2D(1, 2)
b3 = b1 + b2
b3.vec2D()
