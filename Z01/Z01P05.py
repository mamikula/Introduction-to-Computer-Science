#Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.

def pierwN():
    P = 3.0
    eps = 0.0001
    a = 1.0
    b = P
    while abs(b - a) >= eps:
        print(a)
        a = (a + b) / 2
        b = P / a
    return a
pierwN()