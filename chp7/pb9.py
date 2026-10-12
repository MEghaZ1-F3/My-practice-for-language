n = int(input("Enter the input: "))

for k in range ( 1, n+1,1):


    if( k == 1 or k == n):
        print("*" * n, end="")
        print()
    else:
        print("*" + " " * (n-2) + "*", end="")
        print("")