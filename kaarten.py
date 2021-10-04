import random

kaarten = []
kleurlist = ["harten","klaveren","schoppen","ruiten"]

y = 0
for x in range(1,5):
    kleur = kleurlist[y]
    for x in range(2,11):
        kaarten.append("{} {}".format(kleur,x))
    kaarten.extend(("{} boer".format(kleur),"{} vrouw".format(kleur),"{} heer".format(kleur),"{} aas".format(kleur)))
    y = y + 1
kaarten.extend(("joker","joker"))

random.shuffle(kaarten)

for x in range(1,8):
    getal = random.randint(1,54)
    print("kaart {}: {}".format(x,kaarten[getal]))
    del kaarten[getal]

print("\ndeck (47 kaarten): {}".format(kaarten))