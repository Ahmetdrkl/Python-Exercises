class Hayvanlar():
    toplam_hayvan_sayisi = 0
    hayvanlar_listesi = []
    def __init__(self, hayvan_turu, yas, boy):#init metoduyla program başlangıcı yapılır
        self.hayvan_turu = hayvan_turu      #self metoduyla fonksiyonlar tüm programda kullanılabilecek hale getirilir
        self.yas = yas
        self.boy = boy
        self.isim = ""
        Hayvanlar.toplam_hayvan_sayisi += 1
    def hayvanlar_listesine_ekle(self):      # Hayvanlar classından alınan bilgiler tanımladığımız listeye eklenir.
        Hayvanlar.hayvanlar_listesi.append([self.hayvan_turu, self.yas, self.boy])
    def hayvan_ismi_güncelle(self, isim):    # Hayvan ismi güncellenir.
        self.isim = isim
        return self.isim
    def hayvan_ismi_yazdir(self):            # Hayvan ismi ekrana yazdırılır.
        print("{0}nin ismi {1}'idir".format(self.hayvan_turu, self.isim))
    def hayvan_sayisini_yazdir():            # Hayvan sayısı ekrana yazdırılır.
        print("Toplam hayvan sayisi: {} dür.".format(Hayvanlar.toplam_hayvan_sayisi))
    @classmethod
    def metre_cinsinden_nesne_olustur(cls, hayvan_turu, yas, boy):
        return cls(hayvan_turu, yas, boy)
    @classmethod
    def hayvanlari_listele(cls):
        return cls.hayvanlar_listesi
hayvan1 =Hayvanlar("Köpek", 2, 50) #tanımlanılan metodların çağırımı yapılır
hayvan1.hayvan_ismi_güncelle("Karabaş")
hayvan1.hayvanlar_listesine_ekle()
hayvan1.hayvan_ismi_yazdir()
hayvan2 = Hayvanlar("Tavşan", 1, 12)
hayvan2.hayvan_ismi_güncelle("Pamuk")
hayvan2.hayvanlar_listesine_ekle()
hayvan2.hayvan_ismi_yazdir()
hayvan3 = Hayvanlar.metre_cinsinden_nesne_olustur("İnek",3,1.2)
hayvan3.hayvanlar_listesine_ekle()
Hayvanlar.hayvan_sayisini_yazdir()
print(Hayvanlar.hayvanlari_listele())