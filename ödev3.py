from abc import ABC,abstractmethod
class Kütüphane(ABC):
    @abstractmethod
    def __init__(self,isim,yazar):
        self.isim=isim
        self.yazar=yazar
    def isimyazdır(self):
        return self.isim
    def yazaryazdır(self):
        return self.yazar
class Kitap(Kütüphane):
    kitap_sayısı=0
    def __init__(self,isim,yazar,çıkış):
        super().__init__(isim,yazar)
        self.çıkış=çıkış
    @classmethod
    def kitapyazdır(cls):
        cls.kitap_sayısı+=cls.kitap_sayısı
    def getkitap(self):
        print("{} isimli kitabın yazarı: {} ve çıkış tarihi: {}".format(self.isim,self.yazar,self.çıkış))
class Dergi(Kütüphane):
    def __init__(self,isim,yazar,sure):
        super().__init__(isim,yazar)
        self.sure=sure
    def getdergi(self):
        print("{} isimli derginin yazarı: {} ve yayınlanma aralığı: {}".format(self.isim, self.yazar, self.sure))

kitap1=Kitap("Perili Köşk","Ömer Seyfettin",1959)
kitap2=Kitap("Ahmet Mahmut Durukal","Yazılım",2022)
kitap3=Kitap("suç ve ceza","Dostoyevski",1865)
dergi1=Dergi("şampiyon Galatasaray ","Fatih Terim","canı isterse")
dergi2=Dergi("fenerbahçe kümeye","ali koç","her saniye")


kitaplistesi=[kitap1,kitap2,kitap3]
dergilistesi=[dergi1,dergi2]

for k in kitaplistesi:
    k.getkitap()
for i in dergilistesi:
    i.getdergi()