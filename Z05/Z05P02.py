#Używając funkcji z poprzedniego zadania proszę napisać funkcję rozwiązującą układ 2 równań
#o 2 niewiadomych.

def podaj():
    parametry = (int(input()), int(input()))
    return parametry

def wyznacznik(xx, yy):
    print(xx[0] * yy[1] - xx[1] * yy[0])
    return xx[0] * yy[1] - xx[1] * yy[0]

def NWD(a, b):
    if a == 0 or b == 0:
        return 1
    a = abs(a)
    b = abs(b)
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def skroc(u):
    print(1)
    sr = NWD(u[0], u[1])
    l = u[0] // sr
    m = u[1] // sr
    return(l, m)

def wyliczanie(xx, yy, wy):
    wg = wyznacznik(xx, yy)
    if wg == 0:
        print('Rownianie nieoznaczone!')
        return 0
    wx = wyznacznik(wy, yy)
    wy = wyznacznik(xx, wy)

    x = (wx, wg)
    y = (wy, wg)
    x = skroc(x)
    y = skroc(y)

    print('x = ', x[0], '/', x[1], end='')
    print('\n')
    print('y = ', y[0], '/', y[1])
    return 0

print('Podaj wspolczynniki przy x')
xx = podaj()
print('Podaj wspolczynniki przy y')
yy = podaj()
print('Podaj wyniki rownan')
ww = podaj()
wyliczanie(xx, yy, ww)
