"""
kare = int(input("KARE BÜUÜKLÜĞÜNÜ GİRİNİZ: "))
print(kare*"* ")
for i in range(kare-2):
    print("*"+" "*(2*kare-3)+"*")
print(kare*"* ")

def kare(a):
    print(a*("*"+" "))
    for i in range(a-2):
        print("*"+" "*(2*a-3)+"*")
    print(a*("*"+" "))
kare(8)
"""
class Ogrenci:
    def _init_(self,isim,soyisim):
        self.isim=isim
        self.soyisim=soyisim
        self.vize=0
        self.final=0
        self.odev=0
        self.__ort=0
    def notlarigir(self):
        self.odev = int(input("Odev Notunuzu Giriniz: "))
        self.vize = int(input("Vize Notunuzu Giriniz: "))
        self.final =int(input("Final Notunuzu Giriniz: "))
    def Ort(self):
        self.__ort=((self.vize*0.3)+(self.final*0.5)+(self.odev*0.2))
    def harfnotu(self):
        harf_notu=""
        if(self._ort>90 and 100<=self._ort):
            harf_notu="AA"
        elif(self._ort>80 and self._ort <=90):
            harf_notu="BA"
        elif(self._ort>70 and self._ort <= 80):
            harf_notu="BB"
        elif(self._ort>60 and self._ort <= 70):
            harf_notu="CB"
        elif(self._ort>55 and self._ort <= 60):
            harf_notu="CC"
        elif(self._ort>50 and self._ort <= 55):
            harf_notu="DC"
        elif(self._ort>40 and self._ort <= 50):
            harf_notu="DD"
        elif(self._ort>30 and self._ort <= 40):
            harf_notu="FF"
        print(harf_notu)
    def get_ort(self):
        print("ögrencinin ortalaması: {}".format(self.__ort))
    def notyazdir(self):
        print("""
        isim={}
        soyisim={}
        vize={}
        final={}
        odev={}
        """.format(self.isim,self.soyisim,self.vize,self.final,self.odev))
a1=Ogrenci("Ahmet","Durukal")
a1.notlarigir()
a1.Ort()
a1.get_ort()
a1.notyazdir()
a1.harfnotu()