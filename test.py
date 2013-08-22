import easygui
import random
__credit__="Pictures from Battle of Wesnoth"
easygui.msgbox("Willkommen",image="bolas.gif" )
versuche=0
while True :
    versuche=versuche+1
    if versuche>3:
        easygui.msgbox("Du hast alle Versuche verbraucht")
        break
    antwort=easygui.buttonbox("Wo ist die Kugel?","Finde die Kugel: Versuch {}".format(versuche),
                  ["Klick mich!","Nein, hör nicht auf ihn! Klick mich!",
                   "Wenn du mich klickst, wirst du es schaffen.","Komm zu mir!"],image="sea-serpent.gif")
    richtig=random.choice(["Klick mich!","Nein, hör nicht auf ihn! Klick mich!",
                   "Wenn du mich klickst, wirst du es schaffen.","Komm zu mir!"])

    if antwort ==richtig:
         easygui.msgbox("Gut gemacht du hast die Kugel gefunden.")
         break
    else:
         easygui.msgbox("Leider falsche Wahl")


easygui.msgbox("Game Over",image="spectre.gif")
