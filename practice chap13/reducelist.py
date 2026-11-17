from functools import reduce
u = [4,6,8,6,78,8,45,98,45,6]

def greatest(t,u):
    if t>u:
        return t
    return u

print(reduce(greatest,u))