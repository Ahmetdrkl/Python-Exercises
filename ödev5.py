class Geometri():
    def __init__(self, kenar_sayisi):
        self.kenar_sayisi = kenar_sayisi
        self.kenarlar = 0

    def kenarlari_gir(self):
        self.a = int(input("1.kenarın uzunluğunu Giriniz:"))
        self.b = int(input("2.kenarın uzunluğu Giriniz :"))
        self.c = int(input("3.kenarın uzunluğu Giriniz :"))

    def kenarlari_listele(self):
        print("1.kenarın uzunluğu:", self.a)
        print("2.kenarın uzunluğu:", self.b)
        print("3.kenarın uzunluğu:", self.c)


class Dikdörtgen_Prizma(Geometri):  # Geometri Classından Super(). metodu ile miras alınır.

    def __init__(self, kenar_sayisi):
        super().__init__(kenar_sayisi)
        self.kenar_sayisi = 3

    def hacim_hesabı(self):
        hacim = self.a * self.b * self.c
        print("Dikdörtgen prizmasının Hacmi: {} cm".format(hacim))  # Hacim Hesaplanır ve yazdırılır.

    def alan_hesabı(self):
        alan = 2 * ((self.a * self.b) + (self.b * self.c) + (self.a * self.c))
        print("Dikdörtgen prizmasının Alanı: {} cm".format(alan))  # Alan Hesaplanır ve yazdırılır.
    def cevre_hesabı(self):
        cevre = (self.a + self.b + self.c) * 4
        print("Dikdörtgen prizmasının Çevresi: {} cm".format(cevre))  # Çevre Hesaplanır ve yazdırılır.
dik_pri = Dikdörtgen_Prizma(3)
dik_pri.kenarlari_gir()
print("\n")
dik_pri.kenarlari_listele()
print("\n")
dik_pri.hacim_hesabı()
dik_pri.alan_hesabı()
dik_pri.cevre_hesabı()