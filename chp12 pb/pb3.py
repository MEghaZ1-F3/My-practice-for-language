ti = int(input("Enter a number: "))

Table = [ti * u for u in range(1,11,1)]

with open("2.txt", "a") as f:
    f.write(str(Table) + "\n")

with open("2.txt", "r") as f:
    print(f.read())