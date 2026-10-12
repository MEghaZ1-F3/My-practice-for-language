def factoriyal(n):
    if(n==1 or n==0):
        return 1
    return n * factoriyal(n-1)
n = int(input("Enter input: "))
print(f"The factoriyal of {n} is : {factoriyal(n)}")