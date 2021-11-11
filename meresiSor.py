meresek=[]
print("Írd be a mérési eredményt: ",end="")
ertek=input()
while ertek.lower()!="end":
    try:
        ertek=float(ertek)
    except:
        print('Csak számokat adj meg, tizedes elválasztó a "."')
    else:
        meresek.append(ertek)
    print("Írd be a mérési eredményt: ",end="")
    ertek=input()

print("\nAdd meg az elvárt átlagot: ",end="")
atlag=float(input())
print("\nAdd meg a tűrést %-ban: ",end="")
szazalek=float(input().strip('%'))

listaAtlag=sum(meresek)/len(meresek)
    
if atlag-(szazalek/100*atlag)<=listaAtlag and atlag+(szazalek/100*atlag)>=listaAtlag:
    print("minden okés")
else:
    print("A gyártmányok selejtesek ")