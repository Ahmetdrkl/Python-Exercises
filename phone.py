class Telefon:
    def __init__(self, numara):
        self.__arananlar_listesi = []
        self.__numara = numara
        self.__toplam_konusma_suresi = 0
    def arama_gerceklestir(self, aranan_numara):
        print("{} Numaralı telefon sahibi {} numarasını aradı.".format(self.__numara, aranan_numara))
        sure = int(input("Konuşma suresi giriniz: "))
        self.__toplam_konusma_suresi += sure
        self.__arananlar_listesi.append(aranan_numara)
    def arananları_listele(self):
        self.__arananlar_listesi
    def aranan_numarayı_arananlardan_sil(self, aranan_numara):
        for i in aranan_numara:
            if aranan_numara in self.__arananlar_listesi:
                self.__arananlar_listesi.remove(aranan_numara)
        print("Silinen numara: {}".format(aranan_numara))
    def numaranı_goster(self):
        self.__numara
    def get_arananları_listele(self):
        print("Arananlar listesi")
        print(self.__arananlar_listesi)
    def get_numaranı_goster(self):
        return (self.__numara)
    def get_toplam_konusma(self):
        return self.__toplam_konusma_suresi
telefon = Telefon("5123455555")
telefon.numaranı_goster()
# kisileri ara
telefon.arama_gerceklestir("5123254845")
telefon.arama_gerceklestir("5143424244")
telefon.arama_gerceklestir("5677686786")
telefon.arama_gerceklestir("5123254845")
telefon.arama_gerceklestir("5123547677")
# arananlari listele
telefon.arananları_listele()
# arayan Sil ve sonra arananlari listele
telefon.aranan_numarayı_arananlardan_sil("5123254845")
telefon.get_arananları_listele()
print("Toplam konusma suresi:",telefon.get_toplam_konusma())