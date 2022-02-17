#Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Proszę napisać
#funkcję, która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie
#z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość znalezionego
#podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.


def palindrom(t):
    l_t = len(t)
    maxlen = 0
    for p in range(l_t):
        if t[p] % 2 == 1:
            for k in range(l_t - 1, p - 1, -1):
                cp = p
                ck = k
                while cp < ck:
                    if t[cp] != t[ck] or t[cp] % 2 == 0:
                        break
                    cp += 1
                    ck -= 1

                if not (cp < ck):
                    maxlen = max(maxlen, k - p + 1)

    return maxlen


t = [0, 0, 0, 1]

print(palindrom(t))