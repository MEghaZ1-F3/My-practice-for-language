ti = int(input("Enter a number: "))

Table = [ti * u for u in range(1,11,1)]

with open("Table.txt", "a") as f:
    f.write(f" Table of {ti} is: {Table}\n")
