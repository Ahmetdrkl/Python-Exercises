#Yazılacak programda 0 ile 100 arasında tam sayı istenecektir. Yazılan sayının ikili pozitif tam sayı çarpımlarını bulan alg yaz
while(True):
    sayi = int(input("çarpanlarını bulmak istediğiniz sayıyı giriniz: "))
    if(sayi<100 and sayi>0):
        for i in range(1, sayi + 1):
            if (sayi % i == 0):
                print("{}*{}".format(i, sayi // i))
    else:
        print("Geçerli değer giriniz: ")