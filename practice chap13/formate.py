# try:
#     t = "name: {} ,marks: {} and phone: {}".format (str(input("Enter name: ")), float(input("Enter marks: ")), int(input("Enter phone: ")))
#     print(t)

# except ValueError as y:
#     print("Error: Invalid input. Please enter the correct data types.")

try:
    name = str(input("Enter name: "))
    Marks =float(input("Enter marks: ")),
    Phone = int(input("Enter phone: "))

    t = "name: {} ,marks: {} and phone: {}".format(name, Marks, Phone)

except ValueError as y:
    print("Error: Invalid input. Please enter the correct data types.")



