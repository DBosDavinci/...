import random

ronde = 0
scoresDict = {"score1" : 0,
              "score2" : 0,
              "score3" : 0,
              "score4" : 0,
              "score5" : 0,
              "score6" : 0,
              "threeofakind" : 0,
              "fourofakind" : 0,
              "fullhouse" : 0,
              "smallstraight" : 0,
              "largestraight" : 0,
              "yahtzee" : 0,
              "chance" : 0}
dobbeldict = {}
opnieuwaantal = 0
getallen = [1,2,3,4,5,6]
totaal = 0

def start():
    spelers = int(input("Met hoeveel spelers wilt u het spel spelen?"))
    if spelers == 1:
        print("Ok, het spel start met 1 speler")
        roll()
    elif spelers > 1:
        print()
    else:
        print("U moet het spel met minimaal 1 speler starten")
        start()

def roll():
    global ronde
    ronde+=1
    for x in range(5):
        dobbeldict.update({f"dobbel{x}": getallen[random.randrange(0,6)]})
        print(f'dobbelsteen {x+1} is: {dobbeldict[f"dobbel{x}"]}')
    opnieuwFunc()

def opnieuwFunc():
    global opnieuwaantal
    opnieuw = input("Wilt u nog een keer rollen? (Y/N)").lower()
    if opnieuw == "y":
        if opnieuwaantal >= 3:
            print("U kunt maximaal 3 keer opnieuw rollen")
            keuzeFunc()
        else:
            opnieuwaantal+=1
            roll()
    elif opnieuw == "n":
        keuzeFunc()
    else:
        print("Only answer with Y or N")
        opnieuwFunc

def keuzeFunc():
    print("Bovenste vakken: 1,2,3,4,5,6")
    print("Onderste vakken: Three of a kind")
    print("                 Four of a kind")
    print("                 Full house")
    print("                 Small straight")
    print("                 Large straight")
    print("                 Yahtzee")
    print("                 Chance")
    keuze = input("Aan welke combinatie wilt u de score van uw dobbelstenen toevoegen?").lower()
    if keuze == "1":
        y = 0
        for x in range(5):
            if dobbeldict[f"dobbel{x}"] == 1:
                y+=1
        scoresDict.update({"score1" : y})
        print(f'Uw score voor 1 is nu: {scoresDict["score1"]}')
        roll()
    elif keuze == "2":
        y = 0
        for x in range(5):
            if dobbeldict[f"dobbel{x}"] == 1:
                y+=1
        scoresDict.update({"score2" : y})
        print(f'Uw score voor 2 is nu: {scoresDict["score1"]}')
        roll()
    elif keuze == "3":
        y = 0
        for x in range(5):
            if dobbeldict[f"dobbel{x}"] == 1:
                y+=1
        scoresDict.update({"score3" : y})
        print(f'Uw score voor 3 is nu: {scoresDict["score1"]}')
        roll()
    elif keuze == "4":
        y = 0
        for x in range(5):
            if dobbeldict[f"dobbel{x}"] == 1:
                y+=1
        scoresDict.update({"score4" : y})
        print(f'Uw score voor 4 is nu: {scoresDict["score1"]}')
        roll()
    elif keuze == "5":
        y = 0
        for x in range(5):
            if dobbeldict[f"dobbel{x}"] == 1:
                y+=1
        scoresDict.update({"score5" : y})
        print(f'Uw score voor 5 is nu: {scoresDict["score1"]}')
        roll()
    elif keuze == "6":
        y = 0
        for x in range(5):
            if dobbeldict[f"dobbel{x}"] == 1:
                y+=1
        scoresDict.update({"score6" : y})
        print(f'Uw score voor 6 is nu: {scoresDict["score1"]}')
        roll()
    elif keuze == "three of a kind":
        toakFunc()
    elif keuze == "four of a kind":
        foakFunc()
    elif keuze == "full house":
        fhFunc()
    elif keuze == "small straight":
        smallFunc()
    elif keuze == "large straight":
        largeFunc()
    elif keuze == "yahtzee":
        if dobbeldict["dobbel1"] == dobbeldict["dobbel2"] == dobbeldict["dobbel3"] == dobbeldict["dobbel4"] == dobbeldict["dobbel5"]:
            yahtzeescore = scoresDict["yahtzee"] + 50
            scoresDict.update({"yahtzee" : yahtzeescore})
        print(f'uw score voor yahtzee is nu: {scoresDict["yahtzee"]}')
        roll()
    elif keuze == "chance":
        chancescore = scoresDict["chance"] + 50
        scoresDict.update({"chance" : chancescore})
    else:
        print("U heeft geen geldige keuze gemaakt, check of u spelfouten heeft gemaakt.")
        keuzeFunc()

start()