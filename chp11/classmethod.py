class Employee:
    s= 5

    @classmethod
    def show(cls):
        print(f"The class attrubite of s is {cls.s}")
t = Employee()

t.s = 57

t.show()