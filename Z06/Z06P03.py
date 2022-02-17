
#Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi koszt
#przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie
#k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
#koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
#polu startowym i ostatnim także wliczamy do kosztu przejścia.

from random import randint

def chess_king(board, line, column, cost):
    if column < 0 or column >= len(board): #wyjscie poza tablice to -1
        return -1

    cost += board[line][column]

    if line == len(board) - 1: #dojscie do konca tablicy zwraca koncowy wynik
        return cost

    price = [-1]*3 #tablica pol na ktore moze stanac krol

    price[0] = chess_king(board, line + 1, column - 1, cost)
    price[1] = chess_king(board, line + 1, column, cost)
    price[2] = chess_king(board, line + 1, column + 1, cost)

    min = -1 #najmniejsza wartoś na polach mozliwych do zajecia
    first = True

    for i in range(3):
        if price[i] != -1 and (price[i] < min or first):
            min = price[i]
            first = False


    return min

def main():
    board = [[randint(1, 10) for _ in range(8)] for _ in range(8)]
    print(chess_king(board, 0, 3, 0))

    for i in board:
        print(i)

main()