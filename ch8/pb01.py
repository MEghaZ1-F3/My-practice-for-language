a= int(input(" Enter a number: "))
b= int(input(" Enter b number: "))
c= int(input(" Enter c number: "))
def gteatest(a,b,c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>a and c>b):
        return c
print(f"The greatest number is : {gteatest(a,b,c)}")