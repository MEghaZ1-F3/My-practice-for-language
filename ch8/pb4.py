# def sum(n):
#     if( n==1):
#         return 1
#     return sum(n-1) + n
# print(f" the sum is {sum(4)}")
def sum(n):
    if( n==1):
        return 1
    return sum(n-1) + n
n = int(input('Enter the number'))
print(sum(n))
# def sum(n):
#     if( n==1):
#         return 1
#     return sum(n-1) + n
# print(sum(4))