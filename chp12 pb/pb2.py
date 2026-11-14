op = [4,7,9,3,6,0,3,4]

for u , o in enumerate(op):
    # if u in [3, 5, 7]:
    if u == 3 or u == 5 or u == 7:
        print(o, end=",")


# tu = [o for u , o in enumerate(op) if u in [3,5,7]]
# print(tu)