import easygui
import random
__credit__="Pictures from Battle of Wesnoth"
easygui.msgbox("Willkommen",image="bolas.gif" )
versuche=0
while True :
    versuche=versuche+1
    if versuche>3:
        easygui.msgbox("Du hast alle versuche verbraucht")
        break
    antwort=easygui.buttonbox("Wo ist die kugel","Finde die Kugel: versuch {}".format(versuche),
                  ["Klick mich","Nein hör nicht auf ihn klick mich",
                   "Wenn du mich klickst wirst du es schaffen","Komm zu mir"],image="sea-serpent.gif")
    richtig=random.choice(["Klick mich","Nein hör nicht auf ihn klick mich",
                   "Wenn du mich klickst wirst du es schaffen","Komm zu mir"])

    if antwort ==richtig:
         easygui.msgbox("Gut gemacht du hast die kugel gefunden.")
         break
    else:
         easygui.msgbox("Leider falsche wahl")


easygui.msgbox("Game Over",image="spectre.gif")
