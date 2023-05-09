
from abc import ABC, abstractmethod
import hashlib

class KontrolPaneli(ABC):
    @abstractmethod
    def _init_(self,isim,surum,url,sifre):
        self.isim=isim
        self.surum=surum
        self.url=url
        self.sifre=(hashlib.md5(sifre.encode())).hexdigest()
        self.durum=False
    @abstractmethod
    def giris_yap(self):
        pass
    @abstractmethod
    def oturum_kontrol(self):
        pass



class Veritabani(KontrolPaneli):
    sayi=0
    def _init_(self,isim,surum,url,sifre,veritabani):
        super()._init_(isim,surum,url,sifre)
        self.veritabani=veritabani
        self.liste=[]
    def giris_yap(self,sifre):
        if sifre==(hashlib.md5(sifre.encode())).hexdigest():
            self.durum=True
        else:
            self.durum=False
    def oturum_kontrol(self):
        if self.durum==True:
            print("Oturum Açıktır.")
        elif self.durum==False:
            print("Oturum Kapalıdır.")

    def yeni_tablo_ekle(self,tabloismi):
        self.tabloismi=tabloismi
        self.liste.append(self.tabloismi)

    @classmethod
    def tablo_sayisi_artir(cls):
        cls.sayi+=1
        print("Mevcut Tablo Sayısı:{}".format(cls.sayi))





class Sunucu(KontrolPaneli):
    def _init_(self,isim,surum,url,sifre):
        super()._init_(isim,surum,url,sifre)
    def giris_yap(self,sifre):
        if sifre==(hashlib.md5(sifre.encode())).hexdigest():
            self.durum==True
        else:
            self.durum==False

    def oturum_kontrol(self):
        if self.durum==True:
            return "Oturum Açıktır."
        elif self.durum==False:
            return "Oturum Kapalıdır."
    @staticmethod
    def iki_farkli_sunucunun_versiyonlarini_goster(self,sunucu1,sunucu2):
        self.sunucu1=self.surum
        self.sunucu2=self.surum
        print("Sunucu Versiyonu:{}".format(self.surum))

veritabani1 = Veritabani("Mysql","12.01","127.0.0.1/mysql","veritabanisifresi","Universite_Otomasyonu")
sunucu1 = Sunucu("Apache","59.1","127.0.0.1/apache","apachesifresi")
sunucu2 = Sunucu("Cats","12.54","127.0.0.1/cats","catssifre")
for i in [veritabani1,sunucu1,sunucu2]:
    i.giris_yap(input("Lütfen oturumu açmak için sifreyi giriniz"))
    i.oturum_kontrol()
veritabani1.yeni_tablo_ekle("siniflar")
Veritabani.tablo_sayisi_artir()
veritabani1.yeni_tablo_ekle("ogrenciler")
Veritabani.tablo_sayisi_artir()
Sunucu.iki_farkli_sunucunun_versiyonlarini_goster(sunucu1,sunucu2)