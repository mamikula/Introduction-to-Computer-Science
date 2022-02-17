#Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych
#czynników niż 2,3,5. Jedynka też jest taką liczbą. Napisz program, który wylicza
#ile takich liczb znajduje się w przedziale od 1 do N włącznie.

def main():
    N = 1000
    licznik = 0
    for j in range(1, N + 1):
        i = j
        while i % (2 or 3 or 5) == 0:
            if i % 2 == 0:
                i /= 2
            if i % 3 == 0:
                i /= 3
            if i % 5 == 0:
                i /= 5
        if i == 1:
            licznik += 1
            print(j)
    return licznik

main()
