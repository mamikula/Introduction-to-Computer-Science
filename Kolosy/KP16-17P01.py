#Dana jest tablica int t[N][N] zawierająca liczby naturalne. Dokładnie w jednym
#wierszu, bądź kolumnie znajduje się fragmentu ciągu arytmetycznego o długości
#większej niż 2, którego elementy są liczbami pierwszymi. Proszę napisać funkcję
#która zwróci długość tego ciągu.

def pierwsza(a, b, c):
    if a < 2 or b < 2 or c < 2:
        return False

    for i in range(2, a):
        if a % i == 0:
            return False

    for i in range(2, b):
        if b % i == 0:
            return False

    for i in range(2, c):
        if c % i == 0:
            return False

    return True

def pull(t):
    cntw = 2
    cntk = 2
    maxc = 0


    for i in range(len(t) - 2):
        for j in range(len(t) - 2):

            if (t[i][j] - t[i][j + 1] == t[i][j + 1] - t[i][j + 2]) and pierwsza(t[i][j], t[i][j + 1], t[i][j + 2]):
                cntw += 1

            else:
                if cntw > maxc:
                    maxc = cntw
                cntw = 2

            if (t[j][i] - t[j + 1][i] == t[j + 1][i] - t[j + 2][i]) and pierwsza(t[j][i], t[j + 1][i], t[j + 2][i]):
                cntk += 1

            else:
                if cntk > maxc:
                    maxc = cntk
                cntk = 2

        if cntw > maxc or cntk > maxc:
            maxc = max(cntw, cntk)

            #print(cntw, cntk)
    return maxc

t = [[3, 3, 5, 3, 4],
     [3, 2, 5, 4, 5],
     [3, 5, 5, 6, 7],
     [4, 1, 5, 1, 1],
     [3, 4, 5, 4, 4]]


print(pull(t))