with open("log.txt") as h:
    koj = h.read()

if "python" in koj:
    print("yes")
else:
    print ('not present')