"""

class universite:
    def __init__(self,isim,soyisim,yas,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.__maas = maas
        print("Üniversite sınıfı calıstı")
    def getMaas(self):
        print(self.__maas)
    def setMaas(self,yeni_maas):
        self.__maas = yeni_maas
    def bilgi(self):
        print("{} {} {} yasında bir calısandir.".format(self.isim,self.soyisim,self.yas))
class Akademisyen(universite):
    def __init__(self,isim,soyisim,yas,maas,alan):
        super().__init__(isim, soyisim, yas, maas)
        self.alan = alan
    def bilgi(self):
        print("{} {} {} yasında {} alanlı bir akademisyendir.".format(self.isim,self.soyisim,self.yas,self.alan))
a1 = universite("Sefa", "Altun", 21, 9800)
a1.bilgi()
a1.getMaas()
a1.setMaas(18400)
a1.getMaas()
b1 = Akademisyen("Ahmet Mahmut", "Durukal", 18,5500, "Bilgisayar")
b1.bilgi()

kelime=input("Kelime gir: ")
i=0
j=1
while(i<len(kelime)):
    print(j * "*",kelime[i])
    j+=2
    i+=1

"""
for satir in range(1,9):
    for sütun in range(1,16):
        if(satir+sütun==9 or sütun-satir==7 or satir==8):
            print("*",end="")
        else:
            print(end=" ")
    print("")
