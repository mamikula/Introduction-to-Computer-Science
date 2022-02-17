#Dwie liczby naturalne są zgodne jeżeli w zapisie dwójkowym zawierają tę samą liczbę jedynek,
#np. 22 = 101102 i 14 = 11102. Dane są tablice T1[N1][N1] T2[N2][N2], gdzie N2<N1. Proszę napisać funkcję,
#która sprawdza czy istnieje takie położenie tablicy T1 wewnątrz tablicy T2, przy którym liczba zgodnych
#elementów jest większa od 33%. Do funkcji należy przekazać tablicę T1 i T2. Obie oryginalne tablice powinny
#pozostać nie zmieniane.

N = 2
M = 5

def jedynki(a):
    ile = 0
    while a > 0:
        if a % 2 == 1:
            ile += 1
        a //= 2
    return ile



def czy_pokrywa(t1, t2):

    for i in range(N):
        for j in range(N):
            t1[i][j] = jedynki(t1[i][j])

    for i in range(M):
        for j in range(M):
            t2[i][j] = jedynki(t2[i][j])


    for lewX in range(1 - N, M):  #indeks wiersza lewego dolnego naroznika mmniejszej tablicy
        for lewY in range(1 - N, M): #indeks kolumy lewego dolnego nraoznika mniejszej tablicy
            suma = 0
            pokryte = 0

            for rtX in range(0, N): #indeks wiersza prawego dolnego naroznika mniejszej talbicy
                for rtY in range(0, N): #indeks kolumny prawego dolnego naroznika mniejszej tablicy
                    lwtdx = lewX + rtX
                    lwtdy = lewY + rtY
                    #wspolrzedne pierwszego elementu(od lewej) w ostatnim wierszu pokrytego przez mala tablice w duzej tablicy

                    if lwtdx >= 0 and lwtdx < N and lwtdy >= 0 and lwtdy < N: #mała tablica nie musi sie zawierac w duzej, dlatego trzeba sprawdzic czy
                        suma += 1                                             # indeksy nie wychodza poza duza

                        if t1[rtX][rtY] == t2[lwtdx][lwtdy]:
                            pokryte += 1

            if pokryte * 33 > suma * 100:
                return True

    return False



t1 = [[0, 0],
      [0, 1]]
t2 = [[4, 4, 6, 6, 6],
      [4, 4, 3, 2, 1],
      [1, 2, 3, 4, 5],
      [7, 5, 3, 1, 2],
      [4, 4, 4, 4, 4],
      ]

print(czy_pokrywa(t1,t2))