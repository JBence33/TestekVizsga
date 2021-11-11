#Név;Neme;Részleg;Belépés;Bér
import os


try:
    f=open("./berek2020.txt",encoding="UTF-8")
except:
    print("Nincs meg a file")
else:
    print("Minden oké")
    #print(os.getcwd())
    print("5.feladat: Kérem egy részleg nevét: ",end="")
    reszleg=input()
    #reszleg="karbantartas"
    f.readline()
    db=0
    osszeg=0
    max=0
    legNagyobbFizu=[]
    statisztika=[]
    hely=0
    for sor in f:
        sor=sor.strip("\n").split(";")
        print(sor)
        db+=1
        osszeg+=int(sor[4])
        if sor[2]==reszleg and int(sor[4])>max:
            max=int (sor[4])
            legNagyobbFizu=sor
        
        try:
            hely=statisztika.index(sor[2])
        except:
            statisztika.append(sor[2])
            statisztika.append(1)
        else:
            statisztika[hely+1]+1

    print("3. feladat: Dolgozók száma: "+str(db)+" fő")
    print("4. feladat: Bérek átlaga: "+str(round(osszeg/db/1000,1))+"fő")
    if legNagyobbFizu:
            print("6.feldat: A legtöbbet kereső dolgozó a megadott részlegnél")
            print("\tNév: "+legNagyobbFizu[0])
            print("\tNeme: "+legNagyobbFizu[1])
            print("\tBelépés: "+legNagyobbFizu[3])
            print("\tBér: "+legNagyobbFizu[4]+" forint")
    else: 
        print("6.feladat: A megadott részleg nem létezik a cégnél")
     
        print("7. feladat: Statisztika")
        for i in range(0,len(statisztika),2):
            print("\t"+statisztika[i],end="")   
            print(" - "+str(statisztika[i])+"fő")
           

    f.close()