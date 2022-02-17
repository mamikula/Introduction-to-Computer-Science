#Napisać program wczytujący dwie liczby naturalne a,b i wypisujący rozwinięcie dziesiętne
#ułamka a/b w postaci ułamka okresowego. Na przykład 1/3 = 0.(3), 1/6 = 0.1(6), 1/7 = 0.(142857)

def maks(a, b):
    if a > b:
        return a
    return b

def l2i5(b):
    l2 = 0
    l5 = 0
    while b % 2 == 0:
        l2 += 1
        b /= 2
    while b % 5 == 0:
        l2 += 1
        b /= 5
    return maks(l2, l5)

def main():
    a = 1
    b = 3

    if b == 0:
        "nie mozna dzielic przez 0!!"
        return

    print(a // b)
    a = a % b
    if a > 0:
        print('.')

    for i in range(0, l2i5(b)):
        a *= 10
        print(a // b)
        a = a % b
        i += 1

    if a > 0:
        print('(')
        roz = a
        a *= 10
        print(a // b)
        a = a % b

        while a != roz:
            a *= 10
            print(a // b)
            a = a % b
        print(')')

main()