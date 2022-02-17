# Napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb.

def NWD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def NWW():
    a = 32
    b = 12
    c = 36

    d = (a * b) / NWD(a, b)
    print((d * c) / NWD(d, c))
    return (d * c) / NWD(d, c)

NWW()