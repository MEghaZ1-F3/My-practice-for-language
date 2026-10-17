with open("log.txt") as g:
    lines = g.readlines()
lineno = 1

for line in lines:
    if ("python" in line):
        print(f"yes : {lineno}")
        break
    lineno +=1
else:
    print("not")