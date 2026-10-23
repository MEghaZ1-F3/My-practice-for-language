class Employee:
    name= "Amjad"
    language = "js"
    salary = 23000

    def __init__(r, name,salary,language):
        r.name= name
        r.salary = salary
        r.language = language
        print(" I am creating object")

    def get_info(r):
        print(f"The language is {r.language} and salary is {r.salary}")
    @staticmethod
    def greet():
        print("Good Morning")

class Employee:
    name= "Amjad"
    language = "js"
    salary = 23000

    def __init__(r, name,salary,language):
        r.name= name
        r.salary = salary
        r.language = language
        print(" I am creating object")

    def get_info(r):
        print(f"The language is {r.language} and salary is {r.salary}")
    @staticmethod
    def greet():
        print("Good Morning")

print("Enter Employee Details:")
user_name = input("Naam daliye: ")
user_salary = int(input("Salary daliye (numbers me): "))  # int() lagaya taaki salary number bane
user_lang = input("Language daliye: ")

amjas = Employee(user_name,user_salary,user_lang)
# print(amjas.name,amjas.salary,amjas.language)

print(f"\nEmployee Name: {amjas.name}")
amjas.get_info()