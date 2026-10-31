import random

a = random.randint(1,100)
t = -1
guesses = 0
while (t!= a):
    t = int(input("Guess the number: "))

    if (a>t):
        print(f"inter greater number ")


    elif (a<t):
        print("inter lower number")
    else:
        print(f"You guess the right number {a}")