def K():
    for j in range(5):
        for i in range(1):
            print("*", end="")
        for i in range(6 - j):
            print(" ", end="")
        for i in range(1):
            print("*", end="")
        print("")

    a = 1

    for i in range(5):
        for i in range(1):
            print("*", end=" ")
        for i in range(1):
            print(" " * a, end="")
        for i in range(1):
            print("*", end="")
        a += 1
        print("")


def U():
    for i in range(6):
        print("*", end="")
        print(6 * " ", end="")
        print("*")
    print(8 * "*")


def S():
    for i in range(5):
        print("*", end=" ")
    print("")
    for i in range(2):
        print("*")
    for i in range(5):
        print("*", end=" ")
    print("")
    for i in range(2):
        print(" " * 7, end=" ")
        for i in range(1):
            print("*")
    for i in range(5):
        print("*", end=" ")


kelime = input("Lütfen U, S, K harflerini içeren bir şey yazınız: ")

harfleri_ayir = list(kelime)

for i in harfleri_ayir:
    if i == "k" or i == "K":
        print("")
        print(K())

    elif i == "u" or i == "U":
        print("")
        print(U())

    elif i == "s" or i == "S":
        print("")
        print(S())

    else:
        print("Lütfen geçerli karakter tuşlayınız.")