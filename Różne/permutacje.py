from math import factorial


def permutuj(n):
    permutacje = []
    perm = [i for i in range(1, n+1)]
    i = 1
    while i >= 0:
        permutacje.append(perm)
        perm = perm.copy()
        i = n - 2
        while i >= 0 and perm[i] > perm[i+1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while perm[j] < perm[i]:
                j -= 1
            perm[i], perm[j] = perm[j], perm[i]
            k = i + 1
            l = n - 1
            while l > k:
                perm[k], perm[l] = perm[l], perm[k]
                k += 1
                l -= 1
    print(permutacje)
    print('\n')
    return permutacje


def tabelka(n):
    permutacja = permutuj(n)
    wynik = [[] for _ in range(factorial(n))]

    for a in range(factorial(n)):
        for i in range(factorial(n)):
            temp = []
            for j in range(n):
                first = permutacja[a][j]
                temp.append(permutacja[i][first - 1])
            for k in range(factorial(n)):
                if temp == permutacja[k]:
                    wynik[a].append(k+1)
    for i in range(factorial(n)):
        print(wynik[i])


if __name__ == "__main__":
    tabelka(4)
