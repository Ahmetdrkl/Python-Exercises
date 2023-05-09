liste=[]
x=0
y=-1
kelime=input("Lütfen bir string giriniz: ")# kelime input alınır
for i in kelime:
    liste.append(i)                 #kelimenin her bir harfi forla listeye dahil edilir
print(liste)
for i in range(len(kelime)//2):     #harf kontrolu kelime uzunluğunun ikiye tam bölündüğü kadar yapılır
    if (kelime[x]==kelime[y]):      #ilk harf ve son harf kontrol edilir ve kontrol mekkanizması kelimenin ortasına doğru devam eder
        x+=1
        y-=1
        if(True):
            print("{} kelimesi palindromdur ".format(kelime))  #kelimenin palindrom olup olmadığı yazdırılır
    else:
        print("{} kelimesi palindrom değil".format(kelime))

