# lop = [2,34,7,4,54,55,75,95,35,40,20]

# def divisible_by_5(n):
#     return n % 5 == 0
# result = list(filter(divisible_by_5, lop))
# print(result)
def divisible5(n):
    if n%5==0:
        return True
    return False

a = [2,34,7,4,54,55,75,95,35,40,20]

r = list(filter(divisible5, a))
print(r)