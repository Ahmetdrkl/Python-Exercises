class Oparator:
    #isim=Teknoça
    def __init__(self, numara, bakiye):
        self.__numara = numara
        self.__bakiye = bakiye

class Turkcel(Oparator):
    def _init_(self, numara, bakiye):
        super().__init__(numara, bakiye)

    def set_numara(self, yeni_num):
        self.__numara = yeni_num

    # numarayı döndürür
    def get_numara(self):
        print(self.__numara)

    def set_bakiye(self, yeni_bak):
        self.__bakiye = yeni_bak

    def get_bakiye(self):
        return (self.__bakiye)

    # Kontör atma fonksiyonu
    def Kontor(self):
        kon_list = [52, 72, 82, 102, 110]
        print(f"Kontör Fiyatları:{kon_list}")
        a = int(input("Kontör Atacağınız Fiyatı Giriniz:"))
        if a == 52:
            print("{} numaraya 52 TL lik Kontör Atılmıştır.".format(self.__numara))
            self.__bakiye -= 52
        elif a == 72:
            print(f"{self.__numara} numaraya 72 TL lik Kontör Atılmıştır")
            self.__bakiye -= 72
        elif a == 82:
            print(f"{self.__numara} numaraya 82 TL lik Kontör Atılmıştır")
            self.__bakiye -= 82
        elif a == 102:
            print(f"{self.__numara} numaraya 102 TL lik Kontör Atılmıştır")
            self.__bakiye -= 102
        elif a == 110:
            print(f"{self.__numara} numaraya 110 TL lik Kontör Atılmıştır")
            self.__bakiye -= 110
        elif self.__bakiye < 52:
            print("Bakiye Yetersiz")
        else:
            print("Yanlış Tuşlama Yaptınız")
        print(f"Kalan Bakiye:{self.__bakiye}")

    # paket atma fonksiyonu
    def paket(self):
        pak_list = [85, 90, 100, 110,120, 130]
        print(f"paket Fiyatları:{pak_list}")
        print("Paket içerikleri:85TL'ye:3GB,750DK,1000SMS")
        print("                 90TL'ye:8GB,100DK,1000SMS")
        print("                 100TL'ye:15GB,100DK,2000SMS")
        print("                 110TL'ye:20GB,2000DK,2500SMS")
        print("                 120TL'ye:25GB,2000DK,2500SMS")
        print("                 130 TL'ye:30GB,2500DK,3000SMS")
        a = int(input("Paket Atacağınız Fiyatı Giriniz:"))
        if a == 85:
            print(f"{self.__numara} numaraya 85 TL lik Paket Atılmıştır")
            self.__bakiye -= 85
        elif a == 90:
            print(f"{self.__numara} numaraya 90 TL lik Paket Atılmıştır")
            self.__bakiye -= 90
        elif a == 100:
            print(f"{self.__numara} numaraya 100 TL lik Paket Atılmıştır")
            self.__bakiye -= 100
        elif a == 110:
            print(f"{self.__numara} numaraya 110 TL lik Paket Atılmıştır")
            self.__bakiye -= 110
        elif a == 120:
            print(f"{self.__numara} numaraya 120 TL lik Paket Atılmıştır")
            self.__bakiye -= 120
        elif a == 130:
            print(f"{self.__numara} numaraya 130 TL lik Paket Atılmıştır")
            self.__bakiye -= 130
        else:
            print("Yanlış Tuşladınız")
        print(f"Kalan Bakiye:{self.__bakiye}")

    def Hediye_Net(self):
        import random
        a = random.randint(1, 20)
        print(f"{self.__numara} Numaranıza Çıkan Hediye İnternet: {a}GB ")
        # fatura ödeme fonksiyonu

    def fatura(self):
        import random
        if self.__numara:
            b = random.randint(100, 104)
            print(f"{self.__numara} numaralı telefonun {b} borcu bulunmaktadır")
            self.__bakiye -= b
            print("Bocunuz Ödenmiştir")
            print(f"Kalan Bakiye{self.__bakiye}")


class Vodafone(Oparator):
    def __init__(self, numara, bakiye):
        super().__init__(numara, bakiye)

    def set_numara(self, yeni_num):
        self.__numara = yeni_num

    # numarayı döndürür
    def get_numara(self):
        print(self.__numara)

    def set_bakiye(self, yeni_bak):
        self.__bakiye = yeni_bak

    def get_bakiye(self):
        return (self.__bakiye)

    # Kontör atma fonksiyonu
    def Kontor(self):
        kon_list = [42, 62, 72, 82, 110]
        print(f"Kontör Fiyatları:{kon_list}")
        a = int(input("Kontör Atacağınız Fiyatı Giriniz:"))
        if a == 42:
            print("{} numaraya 52 TL lik Kontör Atılmıştır.".format(self.__numara))
            self.__bakiye -= 42
        elif a == 62:
            print(f"{self.__numara} numaraya 62 TL lik Kontör Atılmıştır")
            self.__bakiye -= 62
        elif a == 72:
            print(f"{self.__numara} numaraya 82 TL lik Kontör Atılmıştır")
            self.__bakiye -= 72
        elif a == 82:
            print(f"{self.__numara} numaraya 102 TL lik Kontör Atılmıştır")
            self.__bakiye -= 82
        elif a == 110:
            print(f"{self.__numara} numaraya 110 TL lik Kontör Atılmıştır")
            self.__bakiye -= 110
        elif self.__bakiye < 52:
            print("Bakiye Yetersiz")
        else:
            print("Yanlış Tuşlama Yaptınız")
        print(f"Kalan Bakiye:{self.__bakiye}")

    def paket(self):
        pak_list = [75, 85, 90, 100, 120,135]
        print(f"paket Fiyatları:{pak_list}")
        print("Paket içerikleri:75TL'ye:5GB,500DK,750SMS")
        print("                 85TL'ye:7GB,750DK,1000SMS")
        print("                 90TL'ye:10GB,1000DK,1500SMS")
        print("                 100TL'ye:15GB,1500DK,2000SMS")
        print("                 120TL'ye:20GB,2500DK,2500SMS")
        print("                 140TL'ye:30GB,2500DK,3000SMS")
        a = int(input("Paket Atacağınız Fiyatı Giriniz:"))
        if a == 75:
            print(f"{self.__numara} numaraya 85 TL lik Paket Atılmıştır")
            self.__bakiye -= 75
        elif a == 85:
            print(f"{self.__numara} numaraya 90 TL lik Paket Atılmıştır")
            self.__bakiye -= 85
        elif a == 90:
            print(f"{self.__numara} numaraya 100 TL lik Paket Atılmıştır")
            self.__bakiye -= 90
        elif a == 100:
            print(f"{self.__numara} numaraya 100 TL lik Paket Atılmıştır")
            self.__bakiye -= 100
        elif a == 120:
            print(f"{self.__numara} numaraya 120 TL lik Paket Atılmıştır")
            self.__bakiye -= 120
        elif a == 140:
            print(f"{self.__numara} numaraya 140 TL lik Paket Atılmıştır")
            self.__bakiye -= 140
        else:
            print("Yanlış Tuşladınız")
        print(f"Kalan Bakiye:{self.__bakiye}")

    def Hediye_net(self):
        import random
        a = random.randint(1, 20)
        print(f"{self.__numara} Numaranıza Çıkan Hediye İnternet: {a}GB ")
        # fatura ödeme fonksiyonu

    def fatura(self):
        import random
        if self.__numara:
            b = random.randint(100, 104)
            print(f"{self.__numara} numaralı telefonun {b} borcu bulunmaktadır")
            self.__bakiye -= b
            print("Bocunuz Ödenmiştir")
            print(f"Kalan Bakiye{self.__bakiye}")


class Pttcell(Oparator):
    def __init__(self, numara, bakiye):
        super().__init__(numara, bakiye)

    def set_numara(self, yeni_num):
        self.__numara = yeni_num

    # numarayı döndürür
    def get_numara(self):
        return self.__numara

    def set_bakiye(self, yeni_bak):
        self.__bakiye = yeni_bak

    def get_bakiye(self):
        return self.__bakiye

    # Kontör atma fonksiyonu
    def Kontor(self):
        kon_list = [42, 62, 72, 82, 110]
        print(f"Kontör Fiyatları:{kon_list}")
        a = int(input("Kontör Atacağınız Fiyatı Giriniz:"))
        if a == 42:
            print("{} numaraya 52 TL lik Kontör Atılmıştır.".format(self.__numara))
            self.__bakiye -= 42
        elif a == 62:
            print(f"{self.__numara} numaraya 62 TL lik Kontör Atılmıştır")
            self.__bakiye -= 62
        elif a == 72:
            print(f"{self.__numara} numaraya 72 TL lik Kontör Atılmıştır")
            self.__bakiye -= 72
        elif a == 82:
            print(f"{self.__numara} numaraya 82 TL lik Kontör Atılmıştır")
            self.__bakiye -= 82
        elif a == 110:
            print(f"{self.__numara} numaraya 110 TL lik Kontör Atılmıştır")
            self.__bakiye -= 110
        elif self.__bakiye < 52:
            print("Bakiye Yetersiz")
        else:
            print("Yanlış Tuşlama Yaptınız")
        print(f"Kalan Bakiye:{self.__bakiye}")

    def paket(self):
        pak_list = [80, 95, 110, 120, 140]
        print(f"paket Fiyatları:{pak_list}")
        print("Paket içerikleri:80TL'ye:5GB,500DK,750SMS")
        print("                 95TL'ye:8GB,750DK,1000SMS")
        print("                 110TL'ye:12GB,1000DK,1500SMS")
        print("                 120TL'ye:15GB,1500DK,2000SMS")
        print("                 140 TL'ye:30GB,2500DK,3000SMS")
        a = int(input("Paket Atacağınız Fiyatı Giriniz:"))
        if a == 85:
            print(f"{self.__numara} numaraya 85 TL lik Paket Atılmıştır")
            self.__bakiye -= 85
        elif a == 90:
            print(f"{self.__numara} numaraya 90 TL lik Paket Atılmıştır")
            self.__bakiye -= 90
        elif a == 100:
            print(f"{self.__numara} numaraya 100 TL lik Paket Atılmıştır")
            self.__bakiye -= 100
        elif a == 110:
            print(f"{self.__numara} numaraya 110 TL lik Paket Atılmıştır")
            self.__bakiye -= 110
        elif a == 120:
            print(f"{self.__numara} numaraya 120 TL lik Paket Atılmıştır")
            self.__bakiye -= 120
        elif a == 140:
            print(f"{self.__numara} numaraya 140 TL lik Paket Atılmıştır")
            self.__bakiye -= 140
        else:
            print("Yanlış Tuşladınız")
        print(f"Kalan Bakiye:{self.__bakiye}")

    # fatura ödeme fonksiyonu
    def Hediye_net(self):
        import random
        a = random.randint(1, 20)
        print(f"{self.__numara} Numaranıza Çıkan Hediye İnternet: {a}GB ")

    def fatura(self):
        import random
        a = random.randint(1, 20)
        print(f"{self.__numara} Numaranıza Çıkan Hediye İnternet: {a}GB ")


turkcel = Turkcel(5442500255, 420)
vodafone = Vodafone(5434550203, 450)
pttcell = Pttcell(5423810255, 400)
while True:
        print(""" Hatınız
                  Turkcell:A
                  Vodafone:B
                  Pttcell:C
                  Çıkış:D
                  tıklayınız
                             """)
        secim = (input("Seçiminiz:"))
        if secim == "A":
            while True:
                print("Turkcelle Hoş Geldiniz.")
                print(""" 
                                        Kontör için:1
                                        Paket  için:2
                                        fatura için:3
                                        Hediye internet için:4
                                        çıkmak için :5
                                    """)
                secim = int(input("Seçiminiz:"))


                if secim == 1:
                    turkcel.set_numara(5443250203)
                    print(turkcel.get_numara())
                    turkcel.set_bakiye(500)
                    #print(turkcel.get_bakiye())
                    turkcel.Kontor()

                elif secim == 2:
                    turkcel.set_numara(5443250203)
                    print(turkcel.get_numara())
                    turkcel.set_bakiye(500)
                    #print(turkcel.get_bakiye())
                    turkcel.paket()
                elif secim == 3:
                    turkcel.set_numara(5443250203)
                    print(turkcel.get_numara())
                    turkcel.set_bakiye(500)
                    #print(turkcel.get_bakiye())
                    turkcel.fatura()
                elif secim == 4:
                    turkcel.set_numara(5443250203)
                    print(turkcel.get_numara())
                    turkcel.set_bakiye(500)
                    # print(turkcel.get_bakiye())
                    turkcel.Hediye_net()
                elif secim==5:
                    print("çıkış yapılıyor")
                break
        elif secim == "B":
            while True:
                print("Vodafone'a Hoş Geldiniz.")
                print(""" 
                        Kontör için:1
                        Paket  için:2
                        fatura için:3
                        Hediye internet için:4
                        çıkmak için :5
                                    """)
                secim = int(input("Seçiminiz:"))
                if secim == 1:
                    vodafone.set_numara(5443250203)
                    print(vodafone.get_numara())
                    vodafone.set_bakiye(500)
                    #print(vodafone.get_bakiye())
                    vodafone.Kontor()
                elif secim == 2:
                    vodafone.set_numara(5443250203)
                    print(vodafone.get_numara())
                    vodafone.set_bakiye(500)
                    #print(vodafone.get_bakiye())
                    vodafone.paket()
                elif secim == 3:
                    vodafone.set_numara(5443250203)
                    print(vodafone.get_numara())
                    vodafone.set_bakiye(500)
                    #print(vodafone.get_bakiye())
                    vodafone.fatura()
                elif secim == 4:
                    vodafone.set_numara(5443250203)
                    print(vodafone.get_numara())
                    vodafone.set_bakiye(500)
                    # print(vodafone.get_bakiye())
                    vodafone.Hediye_net()
                elif secim==5:
                    print("çıkış yapılıyor")
                break
        elif secim == "C":
            while True:
                print("PTTCELL'e Hoş Geldiniz.")
                print(""" 
                        Kontör için:1
                        Paket  için:2
                        fatura için:3
                        Hediye internet için:4
                        çıkmak için :5
                                    """)
                secim = int(input("Seçiminiz:"))
                if secim == 1:
                    pttcell.set_numara(5443250203)
                    print(pttcell.get_numara())
                    pttcell.set_bakiye(500)
                    #print(pttcell.get_bakiye())
                    pttcell.Kontor()
                elif secim == 2:
                    pttcell.set_numara(5443250203)
                    print(pttcell.get_numara())
                    pttcell.set_bakiye(500)
                    #print(pttcell.get_bakiye())
                    pttcell.paket()
                elif secim == 3:
                    pttcell.set_numara(5443250203)
                    #print(pttcell.get_numara())
                    pttcell.set_bakiye(500)
                    #print(pttcell.get_bakiye())
                    pttcell.fatura()
                elif secim==4:
                    pttcell.set_numara(5443250203)
                    print(pttcell.get_numara())
                    pttcell.set_bakiye(500)
                    #print(pttcell.get_bakiye())
                    pttcell.Hediye_net()
                elif secim==5:
                    print("çıkış yapılıyor")
                break





