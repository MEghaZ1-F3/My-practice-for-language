

h = random.randint(1,100)
k = 0
guesses = 0
while (h!= k):
    k = int(input("Guess the number is: "))

    if (h>k):
        print(f"Higher number please ")
        guesses +=1


    elif (h<k):
        print(" lower number please ")
        guesses +=1


print(f"You guess the right number {h} in {guesses} attempts")