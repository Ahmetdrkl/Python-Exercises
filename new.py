from abc import ABC, abstractmethod
class University(ABC):
    def __init__(self,isim,kurulus_yili):
        self.__isim=isim
        self.__kurulus_yili=kurulus_yili
    def bilgiYazdir(self):
        pass
class Departmant(University):
    def __init__(self,isim,kurulus_yili,nesneler=[]):
        super().__init__(isim,kurulus_yili)
        self.__nesneler=nesneler
    @staticmethod
    def UniversiteBilgilendirme():
        print("")
    @classmethod
    def bilgiYazdir(cls):
        print("""
        Bölüm İsmi: {}
        Bölüm Kuruluş Yılı: {}
        """.format(cls.__isim,cls.__kurulus_yili))
    def nesneleriYazdir(cls):
        print("Sozluk:",cls.__nesneler)
    def nesneEkle(self,x):
        self.__nesneler.append(x)
class Students(University):
    def __init__(self,isim,soyisim,kurulus_yili,aldigi_ders,ortalama_not,donem,bilgiler=[]):

        super().__init__(isim,kurulus_yili)
        self.__soyisim=soyisim
        self.__aldigi_ders=aldigi_ders
        self.__ortalama_not=ortalama_not
        self.__donem=donem
        self.__bilgiler=bilgiler
    @classmethod
    def OgrenciBilgi(cls):
        print("Ad: {}  Soyad: {} Doğum Tarihi: {} ".format(cls.__isim,cls.__soyisim,cls.__kurulus_yili))
    def dersBilgileri(self):
        self.__bilgiler["Dönem"]=self.__donem
        self.__bilgiler["Aldığı Ders:"]=self.__aldigi_ders
        self.__bilgiler["Ortalama Not:"]=self.__ortalama_not
s1=Students("Ahmet Mahmut","Durukal","2003","Bilgisayar","71","2")
d1=Departmant("Hitit Üniversitesi","2020")
d1.nesneEkle(s1)
d1.nesneleriYazdir