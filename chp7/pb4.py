num = int(input("Enter number: "))

count = 0

for k in range(1,num,1):
    if (num%k==0):
        count +=1

if count == 1:
    print("Prime number")
else:
    print("Not prime")

# num = int(input("Enter number: "))

# count = 0

# for k in range(1,int(num**0.5)+1,1):
#     if (num%k==0):
#         count +=1

# if count == 1:
#     print("Prime number")
# else:
#     print("Not prime")