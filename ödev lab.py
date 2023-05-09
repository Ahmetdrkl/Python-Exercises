"""
#1-) merdiven şeklinde girilen kelimeyi yazdırma
kelime = input("Lütfen Bir Kelime Giriniz: ")
a = 0
for i in range(len(kelime)):
    i = (i * 2) + 1
    for j in range(0, i):
        print("*", end="")
    for k in range(1):
        print(kelime[a])
        a += 1

#2-) Girilen sayının basamaklarını bulma
sayi=int(input("Lütfen sayı giriniz: "))
sayi1=sayi
basamak=0
if(sayi==0):
    basamak=1
while(sayi>=1):
    sayi/=10
    basamak+=1
for i in str(sayi1):
    print(i+(basamak-1)*"0")
    basamak-=1
"""
#3-)100 elemanlı bir dizinin içinde random ondalıklı sayılar eklensin ve küçükten büyüğe sıralansın ve bu ondalıklı sayılar diziye eklensin, dizi yazılsın.
import random
# dizi tanımlanır.
dizi = []
for i in range(100):
    dizi.append((random.uniform(0, 10000)))
print("İlk Dizi:\n ", dizi)
# i dizinin uzunluğu kadar dönsün. sonra j de dizinin uzunluğunun 1 eksiği kadar dönsün.
# Eğer j nin döndüğü değer j nin bir sonraki döneceği değerden büyükse
# j değeri 1 fazlasına eşit olsun. 1 fazlası da 1 eksiğine eşit olsun, bu döngü tam 100 kere yapılır.
for i in range(0, len(dizi)):
    for j in range(0, len(dizi) - 1):
        if dizi[j] > dizi[j + 1]:
            dizi[j], dizi[j + 1] = dizi[j + 1], dizi[j]
# Dizi yazdırılır.
print("Sıralanmış Dizi:\n ", dizi)

#4-)Bazı fonksiyonların ne işe yaradıkları anlatılıyor.
#.capitalize() fonksiyonu metin ifadesinin sadece ilk karakterini büyük harfe çevirir.
#Örnek
#metin = "mühendislik"
#print(metin.capitalize())
#-------------------------------------------------------------------------------------
#.casefold() metin ifadesindeki tüm karakterleri küçük harfe çevirir.
#Örnek
#metin2 = "Ahmet Mahmut Drurukal"
#print(metin2.casefold())
#-------------------------------------------------------------------------------------
#.center() metin ifadesine belirtilen sayı kadar boşluk ekleyip ortalanmış olarak döndürür.
#Örnek
#metin3 = "Kırıkkale"
#print(metin3.center(20))
#-------------------------------------------------------------------------------------
#.count() belirtilen metin ifadesi, ana metin ifadesinde kaç kere geçtiğini bulup döndürür.
#Örnek
#metin4 = "Ahmet Mehmet'den daha hızlı çünkü Ahmet çok daha hızlı."
#print(metin4.count("Ahmet"))
#-------------------------------------------------------------------------------------
#.encode() metin ifadesini UTF-8 olarak kodlayıp döndürür.
#Örnek
#metin5 = "Endüstri Mühendisliği"
#print(metin5.encode())
#-------------------------------------------------------------------------------------
#.endswith() metin ifadesi belirtilen metin ifadesi ile bitiyorsa TRUE değeri döndürür.
#Örnek
#metin6 = "Çekozlavakyalaştıramadıklarımızdanmısınız"
#print(metin6.endswith("z"))
#-------------------------------------------------------------------------------------
#.enxpandtabs() Tab boşluğunun miktarının özelleştirilmesini sağlar.
#Örnek
#metin7 = "K\tı\tr\tı\tk\t"
#print(metin7.expandtabs(5))
#-------------------------------------------------------------------------------------
#.find() metin ifadesi içerisinde belirtilen metin ifadesini arar ve bulduğu index değerini döndürür.
#Örnek
#metin8 = "Durukal"
#print(metin8.find("al"))
#-------------------------------------------------------------------------------------
#.format() metin ifadesini biçimlendirir.
#Örnek
#metin9 = "Benim adım {}"
#print(metin9.format("Ahmet Mahmut"))
#-------------------------------------------------------------------------------------
#.format_map() verilen metni biçimlendirir ve onu döndürür.
#Örnek
#metin10 = {"x" :5,"y" :- 4, "z" : 1}
#print('{x} {y} {z}'.format_map(metin10))
#-------------------------------------------------------------------------------------
#.index() Find metodu gibi çalışır. Metin ifadesi içerisinde belirtilen metin ifadesini arar ve bulduğu index değerini döndürür.
#metin11 = "Hitit Üniversitesi"
#print(metin11.index("Üniversitesi"))
#-------------------------------------------------------------------------------------
#.isalnum() metin ifadesindeki tüm karakterler alfanumerik ise TRUE değeri döndürür.
#Örnek
#metin12 = "Mahmut71"
#print(metin12.isalnum())
#-------------------------------------------------------------------------------------
#.isalpha() metin ifadesindeki tüm karakterler alfabetik ise TRUE değeri döndürür.
#Örnek
#metin13 = "KIRIKKALE"
#print(metin13.isalpha())
#-------------------------------------------------------------------------------------
#.isdecimal() metin ifadesindeki tüm karakterler sayı (kodlanmış olsa bile) ise TRUE değeri döndürür.
#Örnek
#metin14 = "71100"
#print(metin14.isdecimal())
#-------------------------------------------------------------------------------------
#.isdigit() metin ifadesindeki tüm karakterler rakam ise TRUE değeri döndürür.
#Örnek
#metin15 = "71210"
#print(metin15.isdigit())
#-------------------------------------------------------------------------------------
#.islower() metin ifadesindeki tüm karakterler küçük harf ise TRUE değeri döndürür.
#Örnek
#metin16 = "galatasaray"
#print(metin16.islower())
#-------------------------------------------------------------------------------------
#.isnumeric() metin ifadesindeki tüm karakterler sayı ise TRUE değeri döndürür.
#Örnek
#metin17 = "72010"
#print(metin17.isnumeric())
#-------------------------------------------------------------------------------------
#.isprintable() metin ifadesindeki tüm karakterler yazdırılabilir ise TRUE değeri döndürür.
#Örnek
#metin18 = "Ahmet Mahmut  \t Durukal"
#print(metin18.isprintable())
#-------------------------------------------------------------------------------------
#.join() belirtilen bir karakteri kullanarak, bir dizgideki tüm öğeleri bir metin ifadesinde birleştir.
#Örnek
#metin19 = ["Ahmet Mahmut Durukal", "Kırıkkale", "Bilgisayar Mühendisliği"]
#print(" / ".join(metin19))
#-------------------------------------------------------------------------------------
#.ljust() metin ifadesini sola yaslayarak döndürür.
#Örnek
#metin20 = "Java"
#print(metin20.ljust(10), "Orta seviyeli bir programlama dilidir.")
#-------------------------------------------------------------------------------------
#.lower() metin ifadesindeki tüm karakterleri küçük harfe döndürür.
#Örnek
#metin21 = "HİTİT ÜNİVERSTİESİ"
#print(metin21.lower())
#-------------------------------------------------------------------------------------
#.lstrip() metin ifadesinin sol tarafındaki boşluk karakterleri temizleyerek döndürür.
#Örnek
#metin22 = "                     GALATASARAY"
#print(metin22.lstrip(), "SÜPER LİGİN EN İYİ TAKIMIDIR.")
#-------------------------------------------------------------------------------------
#.replace() metin ifadesinde, belirtilen metin ifadelerini değiştirir.
#Örnek
#metin23 = "Fenerbahçe en sevdiğim takımdır."
#print(metin23.replace("Fenerbahçe", "Galatasaray"))
#-------------------------------------------------------------------------------------
#.rfind() metin ifadesi içerisinde belirtilen ifadeyi arar, son bulduğu konumdaki index değerini döndürür.
#Örnek
#metin24 = "Galatasaray Şampiyon"
#print(metin24.rfind("Şampiyon"))
#-------------------------------------------------------------------------------------
#.rindex() rfind() metodu gibi, metin ifadesi içerisinde belirtilen ifadeyi arar, son bulduğu konumdaki index değerini döndürür.
#Örnek
#metin25 = "Galatasaray Şampiyon"
#print(metin25.rindex("Şampiyon"))
#-------------------------------------------------------------------------------------
#.rpartition() metin ifadesi içerisinde belirli bir ifadenin en son geçtiği yeri bulur ve ifadeyi üçe böler. Üç elemanlı diziye dönüştürür.
#Örnek
#metin26 = "Ahmet Mahmut Durukal"
#print(metin26.rpartition("Mahmut"))
#-------------------------------------------------------------------------------------
#.split() metin ifadesini belirtilen ifadeye göre sağdan başlayarak dilimler ve listeye dönüştürür.
#Örnek
#metin27 = "Ahmet Mahmut Durukal"
#print(metin27.split("Mahmut"))
#-------------------------------------------------------------------------------------
#.startswith() metin ifadesinin başlangıcında belirli bir metin ifadesi ile başlayıp başlamadığını kontrol eder, başlıyorsa TRUE değerinin döndürür.
#Örnek
#metin28 = "Benim yaşım: 18"
#print(metin28.startswith("yaşım"))
#-------------------------------------------------------------------------------------
#.strip() metin ifadesini sağından ve solundan boşluk karakterlerini siler.
#Örnek
#metin29 = "                       ULTRAASLAN Taraftarı                       "
#print(metin29.strip(), "Bir Harika !")
#-------------------------------------------------------------------------------------
#zfill() metin ifadesinin sol tarafına belirtilen sayı kadar sıfır ekler.
#metin30 = "71"
#print(metin30.zfill(8))
"""
#5-) 1 ile girilecek sayı arasındaki asal sayiları bulan program
asal=[]
sayi = int(input("Lütfen bir sayı giriniz: "))
for k in range(1, sayi + 1):
    if k > 1:
        for i in range(2, k):
            if (k % i) == 0:
                break
        else:
            asal.append(k)
print("Bulunan asal sayılar:",end="")
for i in asal:
    if i != asal[-1]:
        print(" {}".format (i),end=",")
    else:
        print(" {}".format(i))
"""
