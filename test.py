import sikidom

negySzog=sikidom.nszog()
print(negySzog.terulet())

k1=sikidom.kor()
print("Kör")
print(k1.kerulet())
print(k1.terulet())

k2=sikidom.kor(10)
print("Kör")
print(k2.terulet())
print(k2.kerulet())