from re import X


print("das ist ein kalender")
x = int(input("geben sie die anzahl der tage ein für die sie planen möchten"))
print(X)
print("ist diese anzahl richtig?")  
print("ja oder nein")
y = input()
if y == "ja":
    print("okay")
    print("wollen sie den kalender als array oder als irgendwas anzeigen?") #pdf oder txt
    z = int(input())    #pdf oder txt
    if z == 1:
        print("pdf")
        print("okay")
        print("wollen sie den kalender als array oder in einer datenbak anzeigen?") #array oder datenbank
        w = int(input())
        if w == 1:
            print("array")
            print("okay")
            print("die kalender werden in einzelnen arrays gespeichert")
            print("es ist immer der jeweilige tag der name des arrays")
            montag = []
            dienstag = []
            mittwoch = []
            donnerstag = []
            freitag = []
            samstag = []
            sonntag = []
            print("wollen sie einen eintrag hinzufügen?")
            print("ja oder nein")
            a = input()
            if a == "ja":
                print("wie lange soll der eintrag dauern?")
                b = int(input())
                print("wie viele einträge sollen hinzugefügt werden?")
                c = int(input())
                for i in range(c):
                    print("wie lange soll der eintrag dauern?")
                    b = int(input())
                    print("wie viele einträge sollen hinzugefügt werden?")
                    c = int(input())
            print("wollen sie den kalender einsehen?")
            print("ja oder nein")
            d = input()
            if d == "ja":
                print("okay")
                print("für welchen tag möchten sie den kalender anzeigen? 1-7")
                e = int(input())
                if e == 1:
                    print(montag)
                elif e == 2:
                    print(dienstag)
                elif e == 3:
                    print(mittwoch)
                elif e == 4:
                    print(donnerstag)
                elif e == 5:
                    print(freitag)
                elif e == 6:
                    print(samstag)
                elif e == 7:
                    print(sonntag)
                else:
                    print("dieser tag ist nicht vorhanden")
            print("wollen sie den gesamten kalender in einer txt datei anzeigen?")
            print("ja oder nein")
            f = input()
            if f == "ja":
               datei = open("kalender.txt", "w")
        datei.write(str(montag, dienstag, mittwoch, donnerstag, freitag, samstag, sonntag))
        datei.close()
    elif z == 2:
        print("txt")
    else:
        print("fehler")
