import random

ronde = 0
scoresDict = {"1" : 0,
              "2" : 0,
              "3" : 0,
              "4" : 0,
              "5" : 0,
              "6" : 0,
              "three of a kind" : 0,
              "four of a kind" : 0,
              "full house" : 0,
              "small straight" : 0,
              "large straight" : 0,
              "yahtzee" : 0,
              "chance" : 0}
getallen = [1,2,3,4,5,6]
totaal = 0
opnieuwaantal = 1

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
    dobbelList = []
    ronde+=1
    if ronde <= 5:
        for x in range(5):
            dobbelList.append(getallen[random.randrange(0,6)])
            print(f'dobbelsteen {x+1} is: {dobbelList[x]}')
        opnieuwFunc(dobbelList)
    else:
        totaalFunc()

def opnieuwFunc(dobbelList):
    global opnieuwaantal
    if opnieuwaantal >= 3:
        keuzeFunc(dobbelList)
    else:
        opnieuw = input("Wilt u nog een keer rollen? (Y/N)").lower()
        if opnieuw == "y":
            opnieuwaantal+=1
            roll()
        elif opnieuw == "n":
            keuzeFunc(dobbelList)
        else:
            print("Only answer with Y or N")
            opnieuwFunc()

def keuzeFunc(dobbelList):
    print("Bovenste vakken: 1,2,3,4,5,6")
    print("Onderste vakken: Three of a kind")
    print("                 Four of a kind")
    print("                 Full house")
    print("                 Small straight")
    print("                 Large straight")
    print("                 Yahtzee")
    print("                 Chance")
    keuze = input("Aan welke combinatie wilt u de score van uw dobbelstenen toevoegen?").lower()
    dobbelList.sort()
    if keuze == "1":
        y = 0
        for x in range(5):
            if dobbelList[x] == 1:
                y+=1
        score1new = scoresDict["1"] + y
        scoresDict.update({"1" : score1new})
        scorebericht(keuze)
        roll()
    elif keuze == "2":
        y = 0
        for x in range(5):
            if dobbelList[x] == 1:
                y+=2
        score2new = scoresDict["2"] + y
        scoresDict.update({"2" : score2new})
        print(scorebericht)
        roll()
    elif keuze == "3":
        y = 0
        for x in range(5):
            if dobbelList[x] == 1:
                y+=3
        score3new = scoresDict["3"] + y
        scoresDict.update({"3" : score3new})
        print(scorebericht)
        roll()
    elif keuze == "4":
        y = 0
        for x in range(5):
            if dobbelList[x] == 1:
                y+=4
        score4new = scoresDict["4"] + y
        scoresDict.update({"4" : score4new})
        print(scorebericht)
        roll()
    elif keuze == "5":
        y = 0
        for x in range(5):
            if dobbelList[x] == 1:
                y+=5
        score5new = scoresDict["5"] + y
        scoresDict.update({"5" : score5new})
        print(scorebericht)
        roll()
    elif keuze == "6":
        y = 0
        for x in range(5):
            if dobbelList[x] == 1:
                y+=6
        score6new = scoresDict["6"] + y
        scoresDict.update({"6" : score6new})
        print(scorebericht)
        roll()
    elif keuze == "three of a kind":
        toakFunc()
    elif keuze == "four of a kind":
        foakFunc()
    elif keuze == "full house":
        if dobbelList[0] == dobbelList[1] and dobbelList[2] == dobbelList[4] or dobbelList[0] == dobbelList[2] and dobbelList[3] == dobbelList[4]:
            fhnew = scoresDict["fullhouse"] + 25
    elif keuze == "small straight":
        if dobbelList[0] == dobbelList[3] or dobbelList[1] == dobbelList[4]:
            smallnew = scoresDict["smallstraight"] + 30
    elif keuze == "large straight":
        if dobbelList[3] == dobbelList[0]+3 or dobbelList[4] == dobbelList[1]+3:
            largenew = scoresDict["largestraight"] + 40
    elif keuze == "yahtzee":
        if dobbelList[0] == dobbelList[4]:
            yahtzeescore = scoresDict["yahtzee"] + 50
            scoresDict.update({"yahtzee" : yahtzeescore})
        print(f'uw score voor yahtzee is nu: {scoresDict["yahtzee"]}')
        roll()
    elif keuze == "chance":
        chancescore = scoresDict["chance"] + dobbelList[0] + dobbelList[1] + dobbelList[2] + dobbelList[3] + dobbelList[4]
        scoresDict.update({"chance" : chancescore})
        print(f'uw score voor chance is nu: {scoresDict["chance"]}')
        roll()
    else:
        print("U heeft geen geldige keuze gemaakt, check of u spelfouten heeft gemaakt.")
        keuzeFunc()
    
def scorebericht(keuze):
    print(f"uw score voor {keuze} is: {scoresDict[keuze]}")

start()