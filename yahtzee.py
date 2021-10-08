import random

ronde = 0
score1 = 0
score2 = 0
score3 = 0
score4 = 0
score5 = 0
score6 = 0
threeofakind = 0
fourofakind = 0
fullhouse = 0
smallstraight = 0
largestraight = 0
yahtzee = 0
chance = 0
dobbeldict = {}
getallen = [1,2,3,4,5,6]

def start():
    spelers = int(input("met hoeveel spelers wilt u het spel spelen?"))
    if spelers == 1:
        print("Ok, het spel start met 1 speler")
        for x in range(5):
            dobbeldict.update({f"dobbel{x}": getallen[random.randrange(0,6)]})
            print(f'dobbelsteen {x+1} is: {dobbeldict[f"dobbel{x}"]}')
    elif spelers > 1:
        print()
    else:
        print("U moet het spel met minimaal 1 speler starten")
        start()

start()