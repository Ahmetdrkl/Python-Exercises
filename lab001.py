from abc import ABC, abstractmethod
class Hastane(ABC):
    @abstractmethod
    def __init__(self, isim):
        self.isim = isim
    @abstractmethod
    def get_isim(self):
        return self.isim
    @abstractmethod
    def bilgi(self):
        pass
    @abstractmethod
    def isim_getir(self):
        pass
class Doktor(Hastane):
    def __init__(self, isim, unvan, uzman):
        super().__init__(isim)
        self.unvan = unvan
        self.uzman = uzman
    def bilgi(self):
        print("Ünvanı:{},uzmanlık alanı: {}  olan Doktor hastanemiz görevlisidir.".format(self.unvan, self.uzman))
    def get_isim(self):
        return super().get_isim()
    def isim_getir(self):
        return("{} doktor ile ilgili bilgi:".format(super().get_isim()))
class Hasta(Hastane):
    def __init__(self, isim, hastalik, ilac):
        super().__init__(isim)
        self.hastalik = hastalik
        self.ilac = ilac
    def bilgi(self):
        print("Hastamızın rahatsızlığı: {} , Kullandığı ilac: {} ".format(self.hastalik, self.ilac))
    def get_isim(self):
        return super().get_isim()
    def isim_getir(self):
        print("{} isimli hasta ile ilgili Bilgi:".format(super().get_isim()))
    @classmethod
    def hastaligi_belli_olmayan_hasta(cls):
        return (cls.isim, "hastalik simdilik yok")

hasta = Hasta('Volkan Demirel', 'Diare', 'Galatasaray')
print("Hastanın ismi: {}".format(hasta.get_isim()))
hasta.isim_getir()
hasta.bilgi()
print("---------------------------")
dr = Doktor("Wesley Snaijder" ,'Pr'
                               'of',"Pediyatri")
print("Doktorun ismi: {}".format(dr.get_isim()))
dr.isim_getir()
dr.bilgi()
print("---------------------------")
