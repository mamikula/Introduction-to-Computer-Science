#Dany jest zestaw odważników T[N].
# Napisać funkcję, która sprawdza czy jest możliwe
# odważenie określonej masy.
# Odważniki można umieszczać na obu szalkach.

def odwazniki(t, masa, i):

    if masa == 0:
        return True
    if i == len(t):
        return False

    return (odwazniki(t, masa - t[i], i + 1) or
            odwazniki(t, masa, i + 1) or
            odwazniki(t, masa + t[i], i + 1))

t = [1, 3, 5, 7, 9]
print(odwazniki(t, 2, 0))