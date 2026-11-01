import random

h = random.randint(1,100)
k = 0
guesses = 0
while (h!= k):
    t = int(input("Guess the number: "))

    if (a>t):
        print(f"Higher number please")
        guesses +=1


    elif (a<t):
        print(" lower number please")
        guesses +=1


print(f"You guess the right number {a} in {guesses} attempts")