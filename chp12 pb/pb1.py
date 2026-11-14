try:
    with open ("1.txt", "r") as i:
        print (i.read())

except Exception as w:
    print(w)

try:
    with open ("2.txt", "r") as o:
        print (o.read())

except Exception as l:
    print(l)


try:
    with open ("4.txt", "r") as p:
        print (p.read())

except Exception as j:
    print(j)

print ("thankyou")
