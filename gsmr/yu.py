import random

y = random.randint(1,100)
t = 0
guesses = 0
while (y!= t):
    t = int(input("Guess the number is: "))

    if (y>t):
        print(f"Higher number please ")
        guesses +=1


    elif (y<t):
        print(" lower number please ")
        guesses +=1


    elif (t<y):
        print(" lower number please ")
        guesses +=1
print(f"You guess the right number {h} in {guesses} attempts")