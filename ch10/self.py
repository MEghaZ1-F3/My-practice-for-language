class Employee:
    name= "Amjad"
    language = "js"
    salary = 23000

    def get_info(r):
        print(f"The language is {r.language} and salary is {r.salary}")
    def greet(t):
        print("Good Morning")


amjad = Employee()
amjad.name = "Amjad"
# print(amjad.name,amjad.language,amjad.salary)
# Employee.get_info(amjad)
amjad.greet()
amjad.get_info()