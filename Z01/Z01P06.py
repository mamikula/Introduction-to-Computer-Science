#Proszę napisać program rozwiązujący równanie x
#x = 2020 metodą bisekcji

def bis():
    n = 20
    eps = 0.1
    x = 1 # czy da sie jakos wyznaczac to x??
    roznica = x**x - n
    while abs(roznica) >= eps:
        if roznica > n:
            x = x - x / 2
        elif roznica < n:
            x = x + x / 2
        roznica = x**x - n
    print(x)

bis()
