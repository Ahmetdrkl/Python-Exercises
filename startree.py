bosluk = 0
yukseklik = int(input("Please enter a number for the size of the star tree: "))
yildiz = yukseklik * 2 - 1
for i in range(1, yukseklik + 1):
    print(" " * (bosluk), "*" * (yildiz))
    bosluk += 1
    yildiz -= 2
