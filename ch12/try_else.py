try:
    a = str(input("Enter a string: "))
    print(a)
except Exception as y:
    print("An error occurred:", y)
else:
    print("No error occurred. The string you entered is:", a)