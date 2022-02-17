#Dana jest tablica T[N]. Proszę napisać program zliczający
#liczbę “enek” o określonym iloczynie.
#Zadanie  Proszę zmodyfikować poprzedni program aby
#wypisywał znalezione n-ki.




def nki(t, iloczyn, N):
    suma = 0
    for i in range(0, 2 ** N):
        tmpil = 1
        k = 0
        s = ''
        while i > 0:
            if i % 2 == 1:
                s = s + str(t[k]) + '*'
                tmpil *= t[k]
            i //= 2
            k += 1
        if tmpil == iloczyn:
            print(s, end='')
            suma += 1
            print('\n')
    return suma

def main():
    #t = [2, 4, 2, 3, 12, 6]
    t = [2, 4, 6, 8, 12]

    print(nki(t, 12, len(t)))

main()