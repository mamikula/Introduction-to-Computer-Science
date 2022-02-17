#Napisać program wczytujący trzy liczby naturalne a,b,n i wypisujący rozwinięcie
#dziesiętne ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej
#(n jest rzędu 100)

def rozwiniecie(licz, mian, n):
    if mian == 0:
        print("Nie dzielimy przez 0!!")
        return

    print('postac dziesietna')
    print(licz // mian, end='')
    print('.', end='')
    licz = (licz % mian) * 10

    while n > 0:
        print(licz // mian, end='')
        licz = (licz % mian) * 10
        n -= 1

rozwiniecie(10, 3, 12)