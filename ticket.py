
koltuk=[1,2,3,4,5,6,7,8,9,10] #listeye 10 koltuk eklenir
rezerve=[]                    #rezerve koltukları atayacağımız bış bir rezerve listesi tanımlanır
while (True): #döngü başlatılır
    print("Suan rezerve olmayan yerler:",koltuk)
    a=int(input("Lütfen rezerve edeceğiniz numarayı giriniz veya çıkış için -1 giriniz:")) #koltuk numarası input alınır
    if a==-1:               #input alınan koltuk numarasına -1 yazıldığı durumda program sonlandırılır
        break
    elif a in koltuk:
        koltuk.remove(a)    #koltuk listesinden silinir
        rezerve.append(a)   #1 den 10 a kadar olan koltuk seçiminde o koltuk rezerve listesine dahil edilir
    else:
        print("{} Numaralı koltuk rezerve".format(a))  #eğer rezerve edilmiş bir koltuk alınmaya çalışılırsa rezerve olduğu yazdırılır


def bolenleri_bul(sayi):
    bolen_listesi = []
    for i in range(1, sayi + 1):
        if (sayi % i == 0):
            bolen_listesi.append(i)
    return bolen_listesi


while True:
    sayi = input("Bölenlerini bulmak istediğiniz sayıyı giriniz (Çıkmak için 'q'):")
    if (sayi == "q"):
        print("Programdan Çıkılıyor...")
        break
    else:
        sayi = int(sayi)
        print(bolenleri_bul(sayi))
