#Dany jest zestaw odważników T[N].
# Napisać funkcję, która sprawdza czy jest możliwe
# odważenie określonej masy.
# Odważniki można umieszczać po jednej stronie program powinien wypisywac odwazniki


def odwazniki(t, masa, i, res):

    if i == len(t):
        if masa == 0:
            for i in range(len(res)):
                print(res[i], end=' ')
            print('\n')
            return True

        else:
            return False

    return (odwazniki(t, masa - t[i], i + 1, res + str(t[i])) or
            odwazniki(t, masa, i + 1, res))

t = [1, 3, 5, 7, 9]
odwazniki(t, 22, 0, '')

