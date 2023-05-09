"""
#Print Fonksiyonları
print("ahmet",18,"mahmut","durukal")
print("ahmet\nmahmut\ndurukal")
print("10","06","2003",sep="/") # bu satır ekrana döğum tarihi yazar
print("{} + {} = {}".format(2,3,2+3))
"""
"çoklu yorum satırı"
"""

#Veri Tipleri
a = 3                                #İntager veri tipi
b = 3.14                             #Float veri tipi
c = "Python"                         #String veri tipi
d = [1,2,3,4,5,"Python"]             #List veri tipi
e = (1,2,3,4,5,"Python")             #Tuple veri tipi
f = {"Elma":3,"Armut":5}             #Dictionary v tipi
g = True,False                       #Bool veri tipi
print (type (a))                     #Değişkenin tipini öğreniriz

#String ifadelerin toplanması
ğ = "Bilgisayar"
h = " Mühendisliği"
print(ğ + h)
print(ğ*5)
for i in range (10):
    print("*"*i)

#Karakter çağırma işlemi
ı="EbubekirDurukal"
i=[1,2,3,4,5,6,9]
print(ı[4])#"e" harfini yazdırır.çünkü ebubekir kelimesinin 0 dan başlamak
# şartıyla 4. karakteri ebubekir isminin 5. harfi olan e ye eşittir.
print(i[5])#i dizisinin 5. indeksi 6 ya eşittir. "indeks 0'dan başlar
print(len(i))#len fonksiyonu değişkenin dizinin vs. kaç haneden oluştuğunu yazar
print(i[len(i )-1])
print(ı [0:3])#indeksin belli bir kısmını almak için kullanılır
print(ı[:3])
print(ı[:len(ı):2]) #0'dan başlayıpı değişkeninin uzunluğuna kadar süren ve 2'şer atlayarak yazdırır

#İnput alma
yas = input ("Yaşınızı Giriniz: ")
print("Yaşınız: "+ yas)

#Tpolama İşlemi
sayı1 = int(input("sayı1: "))
sayı2 = int(input("sayı2: "))
toplam = sayı1+sayı2
print("toplam: ",toplam)

#Koşul Durumu
yas =int(input("Yaşınızı giriniz: "))
if (yas<18):
    print("Mekana giremezsiniz...")
else:
    print("Hoşgeldiniz...")

#and or ve not işlemler içerisinde kullanılabilir

#While
j = 0
while (j < 10):
    print("j:",j)
    j += 2 # j = j + 2
    
#Kare alma işlemi
k = 1
while k<1000:
    print(k)
    k*=2

#Break ve Continue
#break kullanımı kolay continue bil
l = 1
while l<10:
    if (l==3 or l==5):
        l = l + 1
        continue
    print("l: ",l)
    l+=1

#def fonksiyon kullanımı
def çarpma (a , b):
    return a * b
sonuç = çarpma (10 , 5)
print(sonuç)
"""
def selamla(isim="ahmet"):
    print("Merhaba")
    print("Nasılsın ?")
selamla("ahmet")

#Klavyeden girilen(N) sayının faktoryelini alan programın akış şeması.
faktoriyel = 1
a = int(input("Faktoriyelini almak istediğiniz sayıyı giriniz: "))
for i in range (1,a+1):
  faktoriyel = faktoriyel * i
print("Sayının faktoriyeli: ",faktoriyel)

#ax²+bx+c=0 şeklinde verilen 2. derece denklemin köklerini bulan programın akış diyagramını çizin.
import math
print("İkinci derece denklemi formülize edilmiş yerlere bilinmeyenleri giriniz: ")
print("ax²+bx+c=0")
a = float(input("a sayısını giriniz: "))
b = float(input("b sayısını giriniz: "))
c = float(input("c sayısını giriniz: "))
delta = (b * b) - (4 * a * c)
if(delta< 0):
    print("Reel kök yok")
elif(delta == 0):
    print("Tek reel kök vardır: ",(-b + (math.sqrt(delta))) / (2*a))
elif (delta > 0):
    print("İki reel kök vardır: ")
    print("x1= ",(-b + (math.sqrt(delta))) / (2*a))
    print("x2= ",(-b - (math.sqrt(delta))) / (2*a))

#taş kağıt makas
import random
seçenek = ["taş","kağıt","makas"]
taş = seçenek[0]
kağıt = seçenek[1]
makas = seçenek[2]
print("Taş Kağıt Makas Oyununa Hoş Geldiniz. Oyunu Bitirmek İçin 'ç' Tuşuna Basınız")
while(True):
    seçim = input("Taş mı Kağıt mı Makas mı:\n")
    com_seçim = random.choice(seçenek)
    if(seçim==taş):
        if(com_seçim==taş):
            print("Bilgisayarın seçimi: {} - Durum Berabere".format(com_seçim))
        elif(com_seçim==kağıt):
            print("Bilgisayarın seçimi: {} - Bilgisayar Kazandı".format(com_seçim))
        elif(com_seçim==makas):
            print("Bilgisayarın seçimi: {} - Siz Kazandınız".format(com_seçim))
    if (seçim == kağıt):
        if (com_seçim == taş):
            print("Bilgisayarın seçimi: {} - Siz Kazandınız".format(com_seçim))
        elif (com_seçim == kağıt):
            print("Bilgisayarın seçimi: {} - Durum Berabere".format(com_seçim))
        elif (com_seçim == makas):
            print("Bilgisayarın seçimi: {} - Bilgisayar Kazandı".format(com_seçim))
    if (seçim == makas):
        if (com_seçim == taş):
            print("Bilgisayarın seçimi: {} - Bilgisayar Kazandı".format(com_seçim))
        elif (com_seçim == kağıt):
            print("Bilgisayarın seçimi: {} - Siz Kazandı".format(com_seçim))
        elif (com_seçim == makas):
            print("Bilgisayarın seçimi: {} - Durum Berabere".format(com_seçim))
    if(seçim=="ç"):
        break

##Adam Asmaca Oyunu##
kelime = "durukal"
yedektahmin = ""
can = 10
while can > 0:
	kalankarakter = 0
	for i in kelime:
		if i in yedektahmin:
			print(i)
		else:
			print("-")
			kalankarakter += 1
	if kalankarakter == 0:
		print("kazandınız")
		break
	tahmin = input("Bir Harf giriniz= ")
	yedektahmin += tahmin
	if tahmin not in kelime:
		can -= 1
		print("yanlış")
		print(f"kalan canın={can} ")
		if can == 0:
			print("kaybettin")

#sayı tahmin oyunu

while(True):
        import random
        a = 10
        while(True):
            b = int(input("1. kullanıcının sayısı: "))
            if(a == b):
                print("1. kullanıcı KAZANDI")
                break
            elif(a > b):
                print("Daha büyük bir sayı girmelisiniz.")
            elif (a < b):
                print("Daha küçük bir sayı girmelisiniz.")
                c = int(input("2. kullanıcının sayısı: "))
                if (a == c):
                    print("2. kullanıcı KAZANDI")
                    break
                elif (a > c):
                    print("Daha büyük bir sayı girmelisiniz.")
                elif (a < c):
                    print("Daha küçük bir sayı girmelisiniz.")
        global inp
        choice = int(input("Devam etmek istiyor musunuz [1)-EVET / 2)-HAYIR]\n"))
        if(choice==1):
            continue
        elif(choice==2):
            break
        else:
            print("Geçerli bir değer giriniz")

#lab zar
import random

zar1 = 0
zar2 = 0
puan1 = 0
puan2 = 0
oyuncu1 = 0
oyuncu2 = 0
while (True):
    for i in range:
#e(1,4):
        zar1 = random.randint(1,6)
        zar2 = random.randint(1,6)
        if(zar1>zar2):
            puan1=puan1+1
        elif(zar1==zar2):
            puan1 = puan1
            puan2 = puan2
        else:
            puan2=puan2+1
        print(zar1, zar2)
    if(puan1>puan2):
        oyuncu1 = oyuncu1 + 1
        print("1. oyuncu puanı:",oyuncu1)
    elif(puan1<puan2):
        oyuncu2= oyuncu2 + 1
        print("2. oyuncu puanı:",oyuncu2)
    elif(puan1==puan2):
        print("DURUM BERABERE")
    if (oyuncu1 == 5 or oyuncu2 == 5):
        break
#basamak bulma
sayı=int(input("Bir sayı giriniz: "))
basamak=0
if(sayı==0):
    basamak=1
while(sayı>=1):
    sayı/=10
    basamak+=1
print("Basamak sayınız: {0}".format(basamak))















