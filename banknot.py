
def para():
    tutar = int(input("Yapılan alışveriş tutarını yazınız: "))
    verilenbanknot = int(input("Verilen banknotu yazınız: "))
    paraustu = (verilenbanknot - tutar)
    sayac200 = 0
    sayac100 = 0
    sayac50 = 0
    sayac20 = 0
    sayac10 = 0
    sayac5 = 0
    sayacbozuk = 0
    while(paraustu>=200):
        sayac200 = paraustu//200
        paraustu=(paraustu%200)
    print("200'lük banknot sayısı:{}".format(sayac200))
    while(paraustu>=100):
        sayac100 = paraustu // 100
        paraustu = (paraustu % 100)
    print("100'lük banknot sayısı:{}".format(sayac100))
    while(paraustu>=50):
        sayac50 = paraustu // 50
        paraustu = (paraustu % 50)
    print("50'lük banknot sayısı:{}".format(sayac50))
    while(paraustu>=20):
        sayac20 = paraustu // 20
        paraustu = (paraustu % 20)
    print("20'lük banknot sayısı:{}".format(sayac20))
    while(paraustu>=10):
        sayac10 = paraustu // 10
        paraustu = (paraustu % 10)
    print("10'lük banknot sayısı:{}".format(sayac10))
    while(paraustu>=5):
        sayac5 = paraustu // 5
        paraustu = (paraustu % 5)
    print("5'lük banknot sayısı:{}".format(sayac5))
    print("1 TL'lik banknot sayısı:{}".format(paraustu))
a1=para()
