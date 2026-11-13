a = int(input("Enter a number here: "))

b = int(input("Enter second number here: "))

if (b== 0):
    raise ZeroDivisionError("hey our program is not meant to divide number by zero and sp on")
else:
    print (f"The division of a/b is {a/b}")