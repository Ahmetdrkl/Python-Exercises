class ogrenci():
    def __init__(self,isim,soyisim,fakulte,bolum,numara):
        self.isim=isim
        self.soyisim=soyisim
        self.fakulte=fakulte
        self.bolum=bolum
        self.numara=numara
    def get_bilgi(self):
        print(self.isim,self.soyisim,self.fakulte,self.bolum,self.numara)

o1=ogrenci("Ahmet Mahmut","Durukal","Mühendislik","Bilgisayar",1)
o2=ogrenci("Esat Emir","Albayrakoğlu","Mühendislik","Bilgisayar",2)
o3=ogrenci("Fatih ","Mehmet", "Sağlık Bilimleri","Hemşire",3)
o3.get_bilgi()