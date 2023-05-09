class Urun:
    def __init__(self, isim):
        self.isim = isim
        self.urun_sayisi = 0
        self.alis_fiyat = 0
        self.satis_fiyat = 0

    def urunEkle(self, miktar):
        self.urun_sayisi += miktar
        print(f"{self.alis_fiyat * miktar} değerinde {miktar} tane ürün eklendi.")

    def urunSat(self, miktar):
        self.urun_sayisi -= miktar
        print(f"{self.satis_fiyat * miktar} değerinde {miktar} tane ürün satıldı.")

    def urunMiktari(self):
        return self.urun_sayisi

    def urunAlisFiyatiniGuncelle(self, fiyat):
        self.alis_fiyat = fiyat

    def urunSatisFiyatiniGuncelle(self, fiyat):
        self.satis_fiyat = fiyat

    def urunIsminiGetir(self):
        return self.isim

    def urunSatisFiyatiGetir(self):
        return self.satis_fiyat

    def urunAlisFiyatiGetir(self):
        return self.alis_fiyat


class Denge:
    def __init__(self, miktar):
        self.para = miktar
        self.gelirler = 0
        self.giderler = 0

    def gelirEkle(self, miktar, urunDegeri):
        self.gelirler += (miktar * urunDegeri)
        self.para += (miktar * urunDegeri)

    def giderEkle(self, miktar, urunDegeri):
        self.giderler += (miktar * urunDegeri)
        self.para -= (miktar * urunDegeri)

    def gelirGiderDurumu(self):
        self.gelirDurumu = self.gelirler - self.giderler
        if self.gelirDurumu < 0:
            print(f"{self.gelirDurumu} zarardasınız.")
        elif self.gelirDurumu > 0:
            print(f"{self.gelirDurumu} kardasınız.")
        elif self.gelirDurumu == 0:
            print(f"{self.gelirDurumu} kar ya da zararınız yok.")
        print(f"Toplam Paranız: {self.para}")


liste = []
liste.append(Urun("Gomlek"))
liste.append(Urun("Pantolon"))

birim = Denge(10000)
while True:
    secim = input(
        "Lütfen seçim yapınız (Ürün Alım:1, Urun Satış:2 ,Urunleri Listele:3, Fiyatları Guncelle:4, Sermayeyi Gör:5, Çıkış:0): ")
    if secim == "0":
        print("Çıkış yapılıyor...")
        break

    elif secim == "1":
        secim = int(input("Lütfen seçim yapınız (Gömlek:1, Pantolon:2): "))
        print(f"{liste[secim - 1].urunIsminiGetir()} isimli üründen {liste[secim - 1].urunMiktari()} adet vardır.")
        eklenecek = int(input("Eklenecek ürün miktarını giriniz: "))
        liste[secim - 1].urunEkle(eklenecek)
        print(f"{liste[secim - 1].urunIsminiGetir()} isimli üründen {liste[secim - 1].urunMiktari()} adet vardır.")

        birim.giderEkle(miktar=eklenecek, urunDegeri=liste[secim - 1].urunAlisFiyatiGetir())

    elif secim == "2":
        secim = int(input("Lütfen seçim yapınız (Gömlek:1, Pantolon:2): "))
        print(f"{liste[secim - 1].urunIsminiGetir()} isimli üründen {liste[secim - 1].urunMiktari()} adet vardır.")
        satilacak = int(input("Satılacak ürün miktarını giriniz: "))
        liste[secim - 1].urunSat(satilacak)
        print(f"{liste[secim - 1].urunIsminiGetir()} isimli üründen {liste[secim - 1].urunMiktari()} adet vardır.")

        birim.gelirEkle(miktar=satilacak, urunDegeri=liste[secim - 1].urunSatisFiyatiGetir())


    elif secim == "3":
        for i in liste:
            print(f"{i.urunIsminiGetir()} isimli üründen güncel olarak {i.urunMiktari()} adet vardır.")

    elif secim == "4":
        secim = int(input("Lütfen seçim yapınız (Gömlek:1, Pantolon:2): "))
        print(
            f"{liste[secim - 1].urunIsminiGetir()} isimli ürünün alış fiyatı: {liste[secim - 1].urunAlisFiyatiGetir()} satış fiyatı: {liste[secim - 1].urunSatisFiyatiGetir()}.")

        liste[secim - 1].urunAlisFiyatiniGuncelle(int(input("Ürün alış fiyatı giriniz: ")))
        liste[secim - 1].urunSatisFiyatiniGuncelle(int(input("Ürün satış fiyatı giriniz: ")))

        print(
            f"{liste[secim - 1].urunIsminiGetir()} isimli ürünün alış fiyatı: {liste[secim - 1].urunAlisFiyatiGetir()} satış fiyatı: {liste[secim - 1].urunSatisFiyatiGetir()}.")

    elif secim == "5":
        birim.gelirGiderDurumu()