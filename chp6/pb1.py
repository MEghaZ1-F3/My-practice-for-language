Number1 = int(input("Enter the number 1: "))
Number2 = int(input("Enter the number 2: "))
Number3 = int(input("Enter the number 3: "))
Number4 = int(input("Enter the number 4: "))

if(Number1>=Number2 and Number1>=Number3 and Number1>=Number4):
    print(f"Number 1 is greatest: {Number1}")
elif(Number2>=Number1 and Number2>=Number3 and Number2>=Number4):
    print(f"Number 2 is greatest: {Number2}")
elif(Number3>=Number2 and Number3>=Number1 and Number3>=Number4):
    print(f"Number 3 is greatest: {Number3}")
else:
    print(f"Number 4 is greatest: {Number4}")