from functools import reduce
# map
t = [1,5,3,7,8,]

squre = lambda o: o*o

slist = map(squre,t)
# print(slist)
print(list(slist))

def odd(e):
    if e%2 != 0:
        return True
    return False

# filter

oddlist = filter(odd,t)
print(list(oddlist))

# reduce

def sub(a,b):
    return a-b

print(reduce(sub,t))