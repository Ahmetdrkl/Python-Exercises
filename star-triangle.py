new_int=int(input("Enter a number for the size of the star triangle: "))
def ucgen(satir):
    print(" "*(satir+1)+"*")
    for i in range(satir):
        print(" "*(satir-i)+"*",end="")
        print((" "*(2*i+1)+"*"))
    print("*"*(2*(satir+1)+1))
ucgen(new_int)
