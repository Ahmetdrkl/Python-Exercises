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
#bu for virgüllerin düzenli şekilde yazılabilmesi için eklenmiştir
for i in asal:
    if i != asal[-1]:
        print(" {}".format (i),end=",")
    else:
        print(" {}".format(i))