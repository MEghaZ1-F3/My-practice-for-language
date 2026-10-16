import random

def game():
    print("You are playing the game")
    score = random.randint(1,20)
    with open("hiscore.txt") as g:
        hiscore = g.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"You score: {score}")
    if(score>hiscore):
        with open("hiscore.txt","w") as g:
            g.write(str(score))


    return score

game()