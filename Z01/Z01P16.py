#Dany jest ciąg określony wzorem: A(n+1) = (A(n)%2)*(3*A(n)+1)+(1-A(n)%2)*A(n)/2
#Startując z dowolnej liczby naturalnej >1 ciąg ten osiąga wartość 1. Napisać
#program, który znajdzie wyraz początkowy z przedziału 2-10000 dla którego wartość 1
#jest osiągalna po największej liczbie kroków.

def ciag():
    step = 0
    maxstep = 0
    maxn = 0
    for n in range(2, 10001):
        i = n
        while n != 1:
            n = (n % 2) * (3 * n + 1) + (1 - n % 2) * n / 2
            step += 1
            if step > maxstep:
                maxstep = step
                maxn = i
        step = 0
    print(maxn, maxstep)
    return maxn
ciag()



