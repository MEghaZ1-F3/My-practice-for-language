class Employee:
    s= 5

    @classmethod
    def show(cls):
        print(f"The class attrubite of s is {cls.s}")
t = Employee()
s = 57

print(t.s)