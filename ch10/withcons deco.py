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

amjad = Employee("akpil",8000,"js")
amjad.greet()
amjad.get_info()
amjas = Employee("amjad",800000,"kubolt")
print(amjas.name,amjas.salary,amjas.language)