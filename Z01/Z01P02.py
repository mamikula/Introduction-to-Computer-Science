#Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, aby w ciągu analogicznym
#do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.

def fib(a, b, szukana):
    while b <= szukana:
        if b == szukana:
            return True
        b = b + a
        a = b - a
    return False

def main():
    szukana = 0
    suma = 1
    while True:
        a = 0
        b = suma
        while b > 0: # b >= a ??
            if fib(a, b, szukana):
                print(a, b)
                return 0
            a += 1
            b -= 1
        suma += 1
main()
