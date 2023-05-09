import random
x = []
z = []
a = 0
boyut = int(input("Lütfen matrisin boyutunu giriniz="))
for i in range(boyut):
    y = []
    for j in range(boyut):
        sayi = int(random.randint(0,9))
        y.append(sayi)
        z.append(sayi)
    x.append(y)
for i in range(boyut):
    print("")
    for j in range(boyut):
        print(z[a], end=" ")
        a += 1
print("\n")
print(x[1][0])
print(y[2]
      )
x = []
z = []
a = 0
boyut = int(input("Lütfen matrisin boyutunu giriniz="))
for i in range(boyut):
    y = []
    for j in range(boyut):
        sayi = int(random.randint(0,9))
        y.append(sayi)
        z.append(sayi)
    x.append(y)
for i in range(boyut):
    print("")
    for j in range(boyut):
        print(z[a], end=" ")
        a += 1
