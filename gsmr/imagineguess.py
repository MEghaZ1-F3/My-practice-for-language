import random

a = random.randint(1,100)
t = -1
guesses = 0
while (t!= a):
    t = int(input("Guess the number: "))

    if (a>t):
        print(f"inter greater number ")


