#3-)100 elemanlı bir dizinin içinde random ondalıklı sayılar eklensin ve küçükten büyüğe sıralansın ve bu ondalıklı sayılar diziye eklensin, dizi yazılsın.
import random
# dizi tanımlanır.
dizi = []
for i in range(100):
    dizi.append((random.uniform(0, 10000)))
print("İlk Dizi:\n ", dizi)
# i dizinin uzunluğu kadar dönsün. sonra j de dizinin uzunluğunun 1 eksiği kadar dönsün.
# Eğer j nin döndüğü değer j nin bir sonraki döneceği değerden büyükse
# j değeri 1 fazlasına eşit olsun. 1 fazlası da 1 eksiğine eşit olsun, bu döngü tam 100 kere yapılır.
for i in range(0, len(dizi)):
    for j in range(0, len(dizi) - 1):
        if dizi[j] > dizi[j + 1]:
            dizi[j], dizi[j + 1] = dizi[j + 1], dizi[j]
# Dizi yazdırılır.
print("Sıralanmış Dizi:\n ", dizi)
