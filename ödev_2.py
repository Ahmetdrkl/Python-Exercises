liste=[]
sayi=int(input("Çarpanlarını bulmak istediğiniz sayıyı giriniz: "))
for i in range(1,sayi+1):
    if sayi%i==0:
        liste.append(i)
print("Çarpanları: ",liste)