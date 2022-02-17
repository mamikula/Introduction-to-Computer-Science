#Dana jest tablica int t[N][N] zawierająca liczby naturalne. Proszę napisać funkcję, która sprawdza czy z tablicy
#można usunąć jeden wiersz i dwie kolumny, tak aby każdy z pozostałych elementów tablicy w zapisie dwójkowym
#posiadał nieparzystą liczbę jedynek.

N = 4

def jedynki(a):
    l = 0
    while a > 0:
        if a % 2 == 1:
            l += 1
        a //= 2
    if l % 2 == 0:
        return 0
    else:
        return 1

def usuwanie(t):
    for i in range(N):
        for j in range(N):
            t[i][j] = jedynki(t[i][j])

    for z in t:
        print(t)


    rozne = 0
    w = -1
    k = -1
    for i in range(N):
        for j in range(N):
            if t[i][j] == 0:
                if i != w and j != k:
                    rozne += 1
                    w = i
                    k = j

            if rozne > 3:
                return False

    return True


def main():

    t1 = [
        [0, 1, 8, 8],
        [8, 0, 8, 1],
        [1, 8, 0, 8],
        [8, 1, 8, 0]
        ]


    t2 = [
        [1, 1, 8, 1],
        [8, 1, 8, 1],
        [1, 8, 8, 8],
        [8, 1, 8, 8]
        ]

    print(usuwanie(t1))
    print(usuwanie(t2))
main()