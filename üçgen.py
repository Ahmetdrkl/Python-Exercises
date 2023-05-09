
def ucgen(satır):
    print(" "*(satır+1)+"*")
    for i in range(satır):
        print(" "*(satır-i)+"*",end="")
        print((" "*(2*i+1)+"*"))
    print("*"*(2*(satır+1)+1))
ucgen(5)
"""
def e(eharfi):
eharfi=int
    print("*" * eharfi)
    for i in range((eharfi)/2):
        print("*")
    print("*" * ((eharfi/5)*3))
    for i in range(eharfi/2):
        print("*")
    print("*" * eharfi)
e(3)
"""