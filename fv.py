def beKer(szoveg="Írd be az adatot"):
    print(szoveg+": ",end="")
    be=input()
    return be

def beKerEgeszSzam(szoveg):
    a=beKer(szoveg)
    hiba=True
    while hiba:
        try:
            a=int(a)
        except:
            print("Egészszámokat írjál")
            a=beKer(szoveg)
            hiba=True
        else:
            hiba=False



beKer("Éljen a python!")
beKer()
a=beKerEgeszSzam("Add meg a számot1")
a=beKerEgeszSzam("Add meg a számot2")
a=beKerEgeszSzam("Add meg a számot3")

    