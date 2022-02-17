#Napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb.

def NWD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def main():
    a = 13
    b = 26
    c = 39
    print(NWD(NWD(a, b), c))
    return NWD(NWD(a, b), c)

main()