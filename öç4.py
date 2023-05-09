class Dikdortgen:
    def __init__(self, UzunKenar, KisaKenar):
        self.UzunKenar = UzunKenar
        self.KisaKenar = KisaKenar

    def dikdortgenCiz(self):
        print("*" * self.UzunKenar)
        for j in range(self.KisaKenar):
            print("*", end="")
            print("", end=" " * (self.UzunKenar - 2))
            print("*")
        print("*" * self.UzunKenar)

    def dikdortgenMi(self):
        if self.UzunKenar != self.KisaKenar:
            return True
        else:
            return False

    def setUzunKenar(self, yeni_uzunkenar):
        self.UzunKenar = yeni_uzunkenar

    def setKisaKenar(self, yeni_kisakenar):
        self.KisaKenar = yeni_kisakenar

    def getUzunKenar(self):
        return self.UzunKenar

    def getKisaKenar(self):
        return self.KisaKenar


if __name__ == "__main__":
    dik = Dikdortgen(10, 5)
    print("10-5 lik Çokgenimiz")
    dik.dikdortgenCiz()

    print("Dikdorgen mi?: " + ("Evet" if dik.dikdortgenMi() else "Hayır"))

    dik2 = Dikdortgen(6, 6)
    print("6-6 lik Çokgenimiz")
    dik2.dikdortgenCiz()

    print("Dikdorgen mi?: " + ("Evet" if dik2.dikdortgenMi() else "Hayır"))

    dik2.setKisaKenar(int(input("Dikdörtgenin kısa kenarını giriniz: ")))
    print(f"Dikdörtgenimizin yeni kısa kenar değeri: {dik2.getKisaKenar()}")

    dik2.setUzunKenar(6)
    dik2.getUzunKenar()

    print("6 - 3'lik Çokgenimiz")
    dik2.dikdortgenCiz()
    print("Dikdorgen mi?: " + ("Evet" if dik2.dikdortgenMi() else "Hayır"))