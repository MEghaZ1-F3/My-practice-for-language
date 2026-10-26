class Employee:
    b= 1

class Programmer(Employee):
    f=3

class Manager(Programmer):
    g = 3


u = Manager()

print(u.g,u.b)