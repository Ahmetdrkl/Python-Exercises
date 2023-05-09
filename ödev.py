class Ogrenci:
    def __init__(self,isim,soyisim):
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
        if(self.__ort>90 and 100<=self.__ort):
            harf_notu="AA"
        elif(self.__ort>80 and self.__ort <=90):
            harf_notu="BA"
        elif(self.__ort>70 and self.__ort <= 80):
            harf_notu="BB"
        elif(self.__ort>60 and self.__ort <= 70):
            harf_notu="CB"
        elif(self.__ort>55 and self.__ort <= 60):
            harf_notu="CC"
        elif(self.__ort>50 and self.__ort <= 55):
            harf_notu="DC"
        elif(self.__ort>40 and self.__ort <= 50):
            harf_notu="DD"
        elif(self.__ort>30 and self.__ort <= 40):
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
