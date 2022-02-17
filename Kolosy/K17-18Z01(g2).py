#Dana jest tablica wypeªniona liczbami naturalnymi int t[N][N] reprezentuj¡ca szachownice. Prosz¦ napisa¢
#funkcje, która sprawdza, czy jest mo»liwe ustawienie dwóch wzajemnie szachuj¡cych sie skoczków tak, aby
#suma warto±ci pól, na których stoj¡ skoczki, byªa liczb¡ pierwsz¡. Do funkcji nale»y przekaza¢ tablic¦ t,
#funkcja powinna zwróci¢ warto±¢ typu bool.

def prime(a):
    if a < 2:
        return False
    for i in range(2, int((a**0.5)) + 1):
        if a % i == 0:
            return False
    return True

def possible(w, k, N):
    if w >= 0 and w < N and k >= 0 and k < N:
        return True
    return False

def chess(board):
    moves = [(-2,1), (2,-1), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]
    for i in range(len(board)):
        for j in range(len(board)):
            for z in moves:
                if possible(i + z[0], j + z[1], len(board)) and prime(board[i][j] + board[i + z[0]][j + z[1]]):
                    return True

    return False

board1 = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 4, 0, 0],
         [0, 0, 0, 0]]

board2 = [[2, 2, 2, 2],
         [2, 2, 2, 2],
         [2, 2, 2, 2],
         [2, 2, 2, 2]]

board3 = [[5, 5, 5, 5],
         [5, 5, 5, 5],
         [5, 5, 5, 5],
         [5, 5, 5, 5]]

print(chess(board3))