bosluk = 0
yukseklik = int(input("Yıldız ağacının boyutunu giriniz: "))
yildiz = yukseklik * 2 - 1
for i in range(1, yukseklik + 1):
    print(" " * (bosluk), "*" * (yildiz))
    bosluk += 1
    yildiz -= 2
