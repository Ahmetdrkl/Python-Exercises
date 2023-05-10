class Market:
    def __init__(self,marketisim,sermaye,urunlistesi):
        self.marketisim=marketisim
        self.sermaye=sermaye
        self.urunlistesi=urunlistesi
    def urun_ekle(self,urun,birim_fiyat):
        self.urun=urun
        self.birim_fiyat=birim_fiyat
        self.urunlistesi.append(self.urun)
        self.sermaye=self.sermaye-(self.urun["urun_miktar"]*self.birim_fiyat)
        print(f"{self.urun['urun_adi']} İsimli Ürün Stoğa Eklenmiştir. Mevcut Sermaye:{self.sermaye}")
    def urunu_sat(self,urun_id,urun_miktari):
        self.urun_id=urun_id
        self.urun_miktari=urun_miktari
        if self.urun_id==self.urun["urun_id"]:
            if self.urun["urun_miktar"]>=self.urun_miktari:
                self.sermaye=self.sermaye+(self.urun["urun_miktar"]*self.urun["urun_fiyat"])
                self.urun["urun_miktar"]=self.urun["urun_miktar"]-self.urun_miktari
                print(f"{self.urun['urun_adi']} İsimli Ürün Satılmıştır. Mevcut Ürün Miktari {self.urun['urun_miktar']}")
            else:
                print("İstenen Ürün Miktarı Stoktakinin Üzerindedir.")
        else:
            print("İstediğiniz Ürün Bulunamamıştır.")
    def urunleri_goster(self):
        return self.urunlistesi
    def sermayeyi_gor(self):
        return self.sermaye
    def sermayeyi_guncelle(self,yeni_sermaye):
        self.sermaye=yeni_sermaye
    def get_isim(self):
        return self.marketisim


if __name__ == "__main__":
    print("Program başlatıldı.")
    # Program calistigi surece dongu devam eder
    market = Market("Hitit Market", 10000, [])
    print(f"Merhaba {market.get_isim()}\n")
    # örnek ürün ekleme dict kullanildi
    market.urun_ekle({"urun_id": 1, "urun_adi": "Ayran", "urun_fiyat": 5, "urun_miktar": 100}, 3)
    while True:
        secenek = input("\nÜrün eklemek için 1\nÜrün satmak için 2\nSermayeyi görmek için 3\nSermayeyi güncellemek için4\nÇıkmak için5yazarakEnter'a basınız: ")
        if secenek == "1":
            urun_id = int(input("Ürün id'sini giriniz: "))
            urun_adi = input("Ürün adını giriniz: ")
            urun_miktari = int(input("Ürün miktarini giriniz: "))
            urun_satis_deger = int(input("Ürün satış değerini giriniz: "))
            urun_alis_deger = int(input("Ürün alış değerini giriniz: "))
            market.urun_ekle({"urun_id": urun_id, "urun_adi": urun_adi, "urun_fiyat": urun_satis_deger, "urun_miktar": urun_miktari}, urun_alis_deger)
        elif secenek == "2":
            print(f"\nStoktaki ürünlerimiz: {market.urunleri_goster()}")
            urun_id = int(input("Ürün id'sini giriniz: "))
            urun_miktari = int(input("Almak istediğiniz ürün miktarı: "))
            market.urunu_sat(urun_id, urun_miktari)
        elif secenek == "3":
            print(f"Güncel sermayeniz: {market.sermayeyi_gor()}")
        elif secenek == "4":
            print(f"Güncel sermayeniz: {market.sermayeyi_gor()}")
            market.sermayeyi_guncelle(int(input("Güncel sermaye değerini giriniz: ")))
        elif secenek == "5":
            print("\nHoşçakalın :)")
            break
        else: print("Yanlış giriş !!!")