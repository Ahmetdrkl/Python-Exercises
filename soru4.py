import random
sat=[]
sut=[]
a=0
boyut=int(input("Matris Boyutunu Giriniz: "))
for i in range(boyut):
    for j in range (boyut):
        sayi=int(random.randint(0,9))
        sat.append(sayi)
        sut.append(sayi)
for i in range (boyut):
    print("")
    for j in range(boyut):
        print(sat[a],end=" ")
        a+=1
print("\n")
satf=[]
sutf=[]
a=0
b=0
c=0
boyut=int(input("Filtre Matris Boyutunu Giriniz: "))
for i in range(boyut):
    for j in range (boyut):
        sayi=int(random.randint(0,9))
        satf.append(sayi)
        sutf.append(sayi)
for i in range (boyut):
    print("")
    for j in range(boyut):
        print(satf[a],end=" ")
        a+=1
for i in range(boyut):
    for j in range(boyut):
        print((sat[i],sut[j])*(satf[i],sutf[j]))


