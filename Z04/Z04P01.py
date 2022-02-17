N = 9

def spirala(t):
    a = 1
    w = 0
    k = N - 1
    while w < k:
        for i in range(w, k + 1):
            t[w][i] = a
            a += 1
        for j in range(w + 1, k + 1):
            t[j][k] = a
            a += 1
        for i in range(k - 1, w, -1):
            t[k][i] = a
            a += 1
        for j in range(k, w, -1):
            t[j][w] = a
            a += 1
        w += 1
        k -= 1
    if w == k:
        t[w][k] = a

t = [[0] * N for i in range(N)]

spirala(t)
for i in range(N):
    for j in range(N):
        print(t[i][j], end='       ')
    print('\n')

#for i in t:
    #print(i)
