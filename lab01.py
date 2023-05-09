from abc import ABC, abstractmethod

class Hayvanlar:
    hayvan_isimleri_listesi = []

    def __init__(self, isim, tur):
        self.__isim = isim
        self.__tur = tur

    @abstractmethod
    def ses_cikar(self):
        pass
    def set_isim():
        pass
    def set_tur():
        pass
    def get_isim():
        pass
    def get_tur():
        pass

    @classmethod
    def hayvan_ismi_ekle(cls, yeni_isim):
        cls.hayvan_isimleri_listesi.append(yeni_isim)

    @classmethod
    def hayvan_isimleri(cls):
        return cls.hayvan_isimleri_listesi

class Kedi(Hayvanlar):
    def __init__(self, kedi_isim, oyuncak):
        kedi_oyuncagi = ""
        super().__init__(kedi_isim,oyuncak)
        self.__isim = kedi_isim
        self.oyuncak = kedi_oyuncagi
        self.__tur = "Kedi"

    def ses_cikar(self):
        return "Miyavv"

    @property
    def get_hayvan_ismi(self):
        return self.__isim

    @get_hayvan_ismi.setter
    def set_hayvan_turu(self, yeni_deger):
        self.__tur = yeni_deger

    @property
    def get_hayvan_turu(self):
        print(self.__tur)

class Kopek(Hayvanlar):
    def __init__(self, kopek_isim, koku_indeks_orani):
        koku_inedsi = 0
        super().__init__(kopek_isim,koku_indeks_orani)
        self.__isim = kopek_isim
        self.koku_indeks_orani = koku_indeks_orani
        self.__tur = "Köpek"

    def ses_cikar(self):
        return "HavHav"

    @staticmethod
    def karsilastirma():
        pass
kopek=Hayvanlar("karabas","kangal")
kedi=Hayvanlar("pamuk","iran kedisi")