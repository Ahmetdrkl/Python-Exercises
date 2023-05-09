import datetime
bilgi = []
hasta = {}
sayı = int(input("lütfen hasta id sini giriniz="))
def hasta_ekle(sayı):
    isim = input("lütfen hasta adını giriniz=")
    soyisimi = input("Lütfen hastanın soyismini giriniz=")
    hastalık_bilgi = int(input("""
                             Lütfen hatalık indeksini giriniz=
                             [
                             {"id":1,"hastalık":"grip"},
                             {"id":2,"hastalık":"covid"},
                             {"id":3,"hastalık":"zature"},
                             {"id":4,"hastalık":"soğuk algınlığı"},
                             ]
                             """))
    tedavi_zamani = datetime.datetime.now()
    hasta = {"id": sayı}, {"hasta isim": isim}, {"hasta soyisim": soyisimi}, {"hastalık bilgisi": hastalık_bilgi}, {
        "tedavi zamanı": tedavi_zamani}
    for i in hasta:
        bilgi.append(i)
    print(bilgi)
def hasta_bilgi_düzenle():
    değişim = int(input("lütfen bilgilerini değiştirmek istedeğiniz hastanın id sini giriniz="))
    if (sayı == değişim):
        print("düzenlemek istediğiğiniz hastanın bilgileri=", bilgi)
        print("""
              isim için 1 i
              soyisim için 2 yi 
              hastalık bilgisi için 3 ü
              hastalık zamanı için 4 ü giriniz
              """)
        karar = int(input("="))
        if (karar == 1):
            isim = input("lütfen yeni ismi giriniz=")
            bilgi[1] = {"hastanın ismi=", isim}
        elif (karar == 2):
            soyismi = input("lütfen yeni ismi giriniz=")
            bilgi[2] = {"hastanın soyisim=", soyismi}
        elif (karar == 3):
            hastalık_bilgi = input("lütfen yeni ismi giriniz=")
            bilgi[3] = {"hastanın hastalık=", hastalık_bilgi}
        print("yeni bilgi", bilgi)
    else:
        print("hastanemizde istediğiniz hasta bulunaadı")
def hasta_listele():
    print("hastenedeki hastalar=", bilgi)
while True:
    giris = input("hasta eklemek için 1'e, hasta bilgisi düzenlemek için 2'ye," +
                  "hastaları listelemek için 3, çıkış için 4 giriniz: ")
    if giris == '1':
        hasta_ekle(sayı)
        sayı += 1
    elif giris == '2':
        hasta_bilgi_düzenle()
    elif giris == '3':
        hasta_listele()
    elif giris == '4':

        print("çıkış yapılıyor...")
        break