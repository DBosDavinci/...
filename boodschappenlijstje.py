itemsDict = {}

def lijstjeInput():
    global itemsDict
    item = input("Wat wilt u toevoegen aan uw boodschappenlijstje?")
    if item in itemsDict:    
        itemsDict[item] += 1
    else:
        itemsDict[item] = 1
    opnieuw = input("Wilt u nog een item toevoegen aan uw lijstje? (Y/N)").lower()
    if opnieuw == "y":
        lijstjeInput()
    elif opnieuw == "n":
        lijstje()

def lijstje():
    global itemsDict
    for key in itemsDict:
        print(key,":",itemsDict[key])

lijstjeInput()