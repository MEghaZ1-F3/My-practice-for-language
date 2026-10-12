def greatest(a,b,c):
    if (a>=b and a>=c):
        print(f"a is greatest : {a}")
    elif(b>=a and b>=c):
        print(f"b is greatest : {b}")
    elif(c>=a and c>=b):
        print(f"c is greatest : {c}")

a = int(input("Enter input: "))
b = int(input("Enter input: "))
c = int(input("Enter input: "))

greatest(a,b,c)
