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