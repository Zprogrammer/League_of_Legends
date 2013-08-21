import random
s = {}
s["schrei"] = {"deckung_gehen":0,"ausweichen":0.5,"verstecken":1,"heiltrank":1}
s["riss"] = {"deckung_gehen":1,"ausweichen":0,"verstecken":0.5,"heiltrank":1}
s["klaue"] = {"deckung_gehen":0.5,"ausweichen":1,"verstecken":0,"heiltrank":1}
s["schlafen"] = {"deckung_gehen":0,"ausweichen":0,"verstecken":0,"heiltrank":0}
#schadensmodell
#Heiltrank :1
#ausweichen + schrei:0.5
#ausweichen + riss:0
#ausweichen + klaue:1
#verstecken + schrei : 1
#verstecken + riss : 0.5
#verstecken + klaue : 0
#deckung gehen + schrei : 0
#deckung gehen + riss : 1
#deckung gehen + klaue : 0.5


b="cho gath"
bhp = 1500
schaden = 4
maxschaden = 100
runde = 0
kritt = 0.2
shp = 100
deckung_gehen = False
ausweichen = False
verstecken = False
monsteraktion = ["schrei",
                 "klaue",
                 "riss",
                 "schlafen"]
menuA = ["Beenden",
         "Normaler Angriff",
         "Ultimativer Angriff"]
        

menuD = ["Beenden",
         "deckung_gehen",
         "ausweichen",
         "verstecken",
         "heiltrank"]
        

while bhp > 0 and shp > 0:
    runde = runde + 1 
    print("Autsch!",b,"hat noch",bhp,"leben übrig")
    print("☻" * int(bhp))
    while True:
        for x in menuA:
            print(menuA.index (x),x)
        x = input("Drücke enter")
        print()
        if x <"0" or x > "6" or len (x)>1:
            print("Falsche Eingabe!!")
            continue 
        else:
            print("Brav")
            break
    if x == "0":
        break
    elif x == "1":
        print("Goblin greift an! runde:",runde)
        schaden = random.randint(0,maxschaden)
        print(b,"erleidet",schaden,"schaden")
        bhp = bhp-schaden
    elif x == "2" :
        print("Du versuchst den Ultimativen Angriff")
        treffer = random.random()
        if treffer < kritt:
            print("Ultima geglückt")
            schaden = maxschaden * 4
            print(b,"erleidet",schaden,"schaden")
            bhp = bhp-schaden
            print("☻" * int(bhp))
        else:
            print("Ultima verschwendet")

     
    #drache schlägt zurück
    deckung_gehen = False   
    ausweichen = False
    verstecken = False

    while True:
        for x in menuD:
            x = input(menuD.index (x),x)
            print("Drücke enter")
        print()
        if x <"0" or x > "6" or len (x)>1:
            print("Falsche Eingabe!!")
            continue 
        else:
            print("Brav", x)
            break
    if x == "0":
        break
    elif x == "4":
        print("Du trinkst einen heiltrank")
        shp = shp + 15
        print("Du hast jetzt ",shp,"hp")
        print("♥" * int(shp))

    elif x == "1":
        deckung_gehen = True
    elif x == "2":
        ausweichen = True
    elif x == "3":
        verstecken = True
        


    aktion = random.choice(drachenaktion)
    if aktion == "schrei":
         print("das monster spuckt feuer")
    elif aktion == "klaue":
        print("das monster schlägt nach dir")
    elif aktion == "riss":
        print("das monster schnappt nach dir")
    elif aktion == "schlafen":
        print("Das monster schläft ein")
    #schadensberechnung
    #print (menuD[x])
    schaden = s[aktion][menuD[int(x)]] * random.randint(10,20)
    shp = shp - schaden
    print("Du erleidest schaden:",schaden)
    print("Du hast noch",shp,"Leben")
    print("♥" * int(shp))
