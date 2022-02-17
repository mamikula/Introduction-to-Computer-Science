#. Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakończonych zerem stanowiącym
#wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
#wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.

def dec():
    tab = [0]*10
    while True:
        dana = int(input())

        if dana == 0:
            break

        if dana < tab[9]: #sprawdzam czy dana liczba nie jest mniejsza niz moje top10 jezeli tak to pomijam
            continue

        for i in range(0, 10):
            if dana > tab[i]: #jezeli dana liczba jest wieksza niz ta na pozycji i
                for j in range(9, i, -1):
                    tab[j] = tab[j - 1] #cofam elementy od 9 do i o 1 w tablicy

                tab[i] = dana #przypisuje nowa wartosc 
                break

    print(tab[9], tab)

dec()