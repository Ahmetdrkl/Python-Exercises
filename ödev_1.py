x = []
z = []
a = 0
boyut = int(input("Lütfen matrisin boyutunu giriniz="))
for i in range(boyut):
    y = []
    for j in range(boyut):
        sayi = int(input("Lütfen {}.satır {}. sütünü giriniz=".format(i, j)))
        y.append(sayi)
        z.append(sayi)
    x.append(y)
for i in range(boyut):
    print("")
    for j in range(boyut):
        print(z[a], end=" ")
        a += 1

m = []
c = 0
for i in range(boyut):
    k = []
    for j in range(boyut):
        k.append(x[j][i])
    m.append(k)
for i in range(boyut):
    if (x[i] == m[i]):
        c += 1
if (c == boyut):
    print("\nMatris Simetriktir")
else:
    print("\nMatris simetrik değil")


