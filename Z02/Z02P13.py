#Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
#liczba zakończona jest unikalną cyfrą.

def main():
    liczba = 0
    l = liczba % 10
    while liczba > 0:
        liczba //= 10
        if l == liczba % 10:
            print("nie jest")
            return
    print("jest")
    return

main()