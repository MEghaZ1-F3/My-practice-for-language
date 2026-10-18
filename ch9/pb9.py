with open("this_copy.txt") as g:
    con1 = g.read()

with open("this.txt") as j:
    con3 = j.read()

if con1 == con3:
    print("identical")
else:
    print("not identical")