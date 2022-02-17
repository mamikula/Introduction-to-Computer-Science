#Napisać program, który oblicza pole figury pod wykresem funkcji y=1/x w przedziale
#od 1 do k, metodą prostokątów.

def f(x):
    return 1/x

def main():
    pole = 0
    k = 20
    dokladnosc = 0.1
    for i in range(1, k + 1):
        pole = pole + f(i + dokladnosc) * dokladnosc
        i = i + dokladnosc

    print(pole)
    return pole
main()