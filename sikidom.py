import math
class nszog:
    oldal=0
    def __init__(self, oldalHossz=1):
        self.oldal=oldalHossz

    def kerulet(self, mertekegyseg=False):
        vissza=4*self.oldal
        if mertekegyseg:
            vissza=str(vissza)
            vissza+="cm"
        return vissza
    def terulet(self, mertekegyseg=False):
        vissza=self.oldal*self.oldal
        if mertekegyseg:
            vissza=str(vissza)
            vissza+="cm2"
        return vissza
        

class kor:
    r=0
    def __init__(self,r=1) -> None:
        self.r=r

    def terulet(self):
        return self.r*self.r*math.pi
        
    def kerulet(self):
        return 2*self.r*math.pi

        
        
vmi=nszog(5)
vmi2=nszog
vmi3=nszog
print(vmi.terulet)
print(vmi2.terulet)
print(vmi3.terulet)
