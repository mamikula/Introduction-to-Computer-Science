#Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
#która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest
#równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
#znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.

N = 10


def dl(t, start):
    curr = 1
    longest = 0
    sumt = t[start]
    sumid = start
    for i in range(start + 1, N):
        if t[i] > t[i - 1]:
            sumt += t[i]
            sumid += 1
            curr += 1
        else:
            sumid = i
            sumt = t[i]
            curr = 1

        if sumt == sumid and curr > longest:
            longest = curr
    return longest

def najdl(t):
    longest = 0
    for i in range(N):
        cur = dl(t, i)
        if cur > longest:
            longest = cur
    return longest