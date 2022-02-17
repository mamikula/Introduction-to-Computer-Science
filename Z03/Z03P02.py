#Napisać program wczytujący dwie liczby naturalne i odpowiadający
#na pytanie czy są one zbudowane z takich samych cyfr, np. 123 i
#321, 1255 i 5125, 11000 i 10001.

def main():
    ilosc_cyfr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    a = 12335
    b = 1235

    while a > 0:
        ilosc_cyfr[a % 10] += 1
        a //= 10

    while b > 0:
        ilosc_cyfr[b % 10] -= 1
        b //= 10

    for i in range(0, len(ilosc_cyfr)):
        if i != 0:
            print('Nie sa')
            return

    print('Sa')
    return

main()