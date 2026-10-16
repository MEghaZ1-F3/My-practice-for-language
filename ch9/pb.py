g = open("poem.txt")
poem = g.read()
if("Tweenkle" in poem):
    print(" the words is present in poem")
else:
    print("Not present in poem")
g.close()