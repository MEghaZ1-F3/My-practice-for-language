import random

a = random.randint(1,100)
t = 0
guesses = 0
while (t!= a):
    t = int(input("Guess the number: "))

    if (a>t):
        print(f"Higher number please")


    elif (a<t):
        print(" lower number please")
    else:
        print(f"You guess the right number {a}")