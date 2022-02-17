#2. W grze mag-mino wykorzystuje się klocki, które mają kształt prostokątów, na których obydwu końcach znajduje
#się liczba oczek od 0 do 9. Na każdym klocku z dwóch jego końców liczba oczek jest inna. W komplecie liczącym 90
#klocków do gry występują wszystkie kombinacje oczek i każda kombinacja występuje dokładnie jeden raz. Proszę
#napisać funkcję, która dla danego zbioru N klocków wyznacza najdłuższy ciąg jaki można z nich ułożyć.
#Na przykład dla zbioru 8 klocków: [2|8] [0|1] [2|3] [3|6] [2|6] [2|9] [3|4] [6|7]
#najdłuższy ciąg jaki można ułożyć ma długość 5 i ma postać : [8|2] [2|3] [3|6] [6|2] [2|9]

#1. Pomysł: Generwoanie tablic z krotkami i sprawdzanie czy prawa 1 kolcka - lewa 2 klocka da 0 i szukanie najdluzszego takiego ciagu

def mag_mino(magset, id, path, taken):
    longest = 0
    if id == len(magset):
        for i in range(len(path) - 1):
            if path[i][1] - path[i + 1][0] == 0:
                print(path)
                if taken > longest:
                    return taken
                else:
                    return longest


    cords = magset[id]
    # bierze klocek normalnie
    path[id][0] = cords[0]
    path[id][1] = cords[1]
    mag_mino(magset, id + 1, path, taken + 1)

    #bierze odwrocony o 180 klocek
    path[id][0] = cords[1]
    path[id][1] = cords[0]
    mag_mino(magset, id + 1, path, taken + 1)

    #nie bierze klocka
    mag_mino(magset, id + 1, path, taken)

def main():
    magset = [(2,8), (0,1), (2,3), (3,6), (2,6), (2,9), (3,4), (6,7)]
    path = [[0] * 2 for _ in range(10)]
    mag_mino(magset, 0, path, 0)

main()