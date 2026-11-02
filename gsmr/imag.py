import random

h = random.randint(1,100)
k = 0
guesses = 0
while (h!= k):
    k = int(input("Guess the number: "))

    if (h>k):
        print(f"Higher number please")
        guesses +=1

