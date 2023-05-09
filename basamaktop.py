sayi = input("Lütfen sayı giriniz:")                  # str formatında giriş yapılır
toplam = 0                                            # bu sayede basamaklar arasında
for rakam in sayi:                                    # geçiş harfler arasındaki gibi yapılabilir
    toplam += int(rakam)                              # alınan her rakam int olduğu belirtilerek teker
print("Sayının basamaklarının toplamı:", toplam)      # teker toplam değişkenine atılır ve yazdırılır


