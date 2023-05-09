#1-) merdiven şeklinde girilen kelimeyi yazdırma
kelime = input("Lütfen Bir Kelime Giriniz: ")
a = 0
# kelime uzunluğu len ile tespit edilir
for i in range(len(kelime)):
    i = (i * 2) + 1
    for j in range(0, i):
        print("*", end="")
    for k in range(1):
        print(kelime[a])
        a += 1