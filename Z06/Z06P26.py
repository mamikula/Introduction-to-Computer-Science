#Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr
#1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość
#wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy
#bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
#10010(2), 10100(2), 11000(2)


def notprime(a):
    i = 0
    new = 0
    while a > 0:
        if a % 10 == 1:
            new += 2**i
        i += 1
        a //= 10
    for i in range(2, new):
        if new % i == 0:
            print(new)
            return True
    return False

def generator(A, B, new):

    ile = 0

    if A == 0 and B == 0:
        if notprime(new):
            print(new)
            return 1
        else:
            return 0

    elif A > 0 and B > 0:
        ile += generator(A - 1, B, new * 10 + 1)
        ile += generator(A, B - 1, new * 10)

    elif A > 0 and B == 0:
        ile += generator(A - 1, B, new * 10 + 1)

    else:
        ile += generator(A, B - 1, new * 10)
    return ile


def main():

    print("znaleziono dokładnie", generator(2, 5, 1), "liczb")
main()