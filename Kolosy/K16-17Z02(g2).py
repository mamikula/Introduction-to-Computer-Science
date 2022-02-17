#Dana jest tablica int t[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
#W każdej kolumnie znajduje się dokładnie jedna wieża, której numer wiersza zawiera tablica
#int w[N]. Proszę napisać funkcję która wybiera do usunięcia z szachownicy dwie wieże, tak aby
#suma liczb na polach szachowanych przez pozostałe wieże była najmniejsza. Do funkcji należy
#przekazać tablice t i w, funkcja powinna zwrócić numery kolumn z których usunięto wieże.


def sums(board, w, k):
    result = 0
    for i in range(len(board)):
        result += board[w][i]
        result += board[i][k]

    result -= 2*board[w][k]
    return result



