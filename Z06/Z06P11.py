#Dana jest tablica T[N].Proszę napisać programzliczający
#liczbę “enek” o określonym iloczynie.


def nki(t, iloczyn, N):
    suma = 0
    for i in range(0, 2 ** N):
        tmpil = 1
        k = 0
        while i > 0:
            print(i)
            if i % 2 == 1:
                tmpil *= t[k]
            i //= 2
            k += 1
        if tmpil == iloczyn:
            suma += 1
    return suma

def main():
    t = [2, 4, 2, 3, 12, 6]

    print(nki(t, 12, len(t)))

main()