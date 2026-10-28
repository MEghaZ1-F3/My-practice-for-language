class Employee:
    s= 5

    @classmethod
    def show(cls):
        print(f"The class attrubite of s is {cls.s}")

    @property
    def name(self):
        return f"{self.yname} {self.iname}"
    @name.setter
    def name(self,value):
        self.yname = value.split(" ")[0]
        self.iname = value.split(" ")[1]
        # self.tname = value.split(" ")[2]

t = Employee()

t.s = 57

t.name = "Amjad khan"

print(t.name)

# print(t.__dict__)

t.show()