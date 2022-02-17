#Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
#która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest
#równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
#znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.

N = 9

def sub(t, start):
    longest = 0
    curr = 1
    sumid = start
    sumval = t[start]
    for i in range(start + 1, N):
        if t[i] > t[i - 1]:
            sumid += i
            sumval += t[i]
            curr += 1
        else:
            sumid = i
            sumval = t[i]
            curr = 1

        if sumid == sumval and curr > longest:
            longest = curr

    return longest

def endsub(t):
    longest = 0
    for i in range(0, N):
        curr = sub(t, i)
        if curr > longest:
            longest = curr

    return longest

t1 = [0, 0, 0, 3, 4, 8, 6, 7, 8]
t2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print(endsub(t1))
print(endsub(t2))
