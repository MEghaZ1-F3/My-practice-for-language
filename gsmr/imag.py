import random

h = random.randint(1,100)

while (h!= k):
    k = int(input("Guess the number: "))

    if (h>k):
        print(f"Higher number please")
        guesses +=1


    elif (h<k):
        print(" lower number please")
        guesses +=1


print(f"You guess the right number {h} in {guesses} attempts")