def pattern(n):
    if (n==0):
        return
    print("*" * n)
    pattern(n-1)


pattern(5)

# def pattern(n):
#     if (n==0):
#         return
#     for k in range( 1, n+1):
#         print("*" * k)


# pattern(5)

