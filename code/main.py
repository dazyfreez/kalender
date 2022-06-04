from re import X


print("das ist ein kalender")
x = int(input("geben sie die anzahl der tage ein für die sie planen möchten"))
print(X)
print("ist diese anzahl richtig?")  
print("ja oder nein")
y = input()
if y == "ja":
    print("okay")
    print("wollen sie den kalender als pdf oder als txt anzeigen?") #pdf oder txt
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
    elif z == 2:
        print("txt")
    else:
        print("fehler")
