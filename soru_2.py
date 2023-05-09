#2-) Girilen sayının basamaklarını bulma
#sayı1 str olarak alınır çünkü len uzunluk almak için str alınması gerekir
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
