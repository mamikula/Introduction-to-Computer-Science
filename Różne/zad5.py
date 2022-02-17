#Marcin Mikuła
#Dana jest tablica T[N] wypełniona niepowtarzającymi się liczbami naturalnymi. Proszę zaimplementować
#funkcję trojki(T) która zlicza wszystkie trójki liczb, które spełniają następujące warunki:
#(1) największym wspólnym dzielnikiem trzech liczb jest liczba 1,
#(2) pomiędzy dwoma kolejnymi elementami trójki może być co najwyżej jedna przerwa.
#Funkcja powinna zwrócić liczbę znalezionych trójek.
#Przykładowe wywołania funkcji:
#print(trojki([2,4,6,7,8,10,12])) # 0 trójek
#print(trojki([2,3,4,6,7,8,10])) # 1 trójka (3,4,7)
#print(trojki([2,4,3,6,5])) # 2 trójki (2,3,5),(4,3,5)
#print(trojki([2,3,4,5,6,8,7])) # 5 trójek (2,3,5),(3,4,5),(3,5,8),(5,6,7),(5,8,7)

def NWD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def main():
    a = 13
    b = 26
    c = 39
    print(NWD(NWD(a, b), c))
    return NWD(NWD(a, b), c)


def trojki(t):
    cnt = 0
    for i in range(len(t) - 3): #t[i] zawsze piperwszy element do sprawdzenia
        for j in range(i + 1, i + 3):
            if NWD(t[i], t[j]) == 1:
                for k in range(j + 1, j + 3):
                    #print(t[i], t[j], t[k])
                    if (k < len(t)): #tego brakuje !!!
                        if NWD(t[i], t[j]) == 1 and NWD(t[i], t[k]) == 1 and NWD(t[k], t[j]) == 1:
                            cnt += 1
                                #print(t[i], t[j], t[k])

    return cnt

t1 = [2,4,6,7,8,10,12]
t2 = [2,3,4,6,7,8,10]
t3 = [2,4,3,6,5]
t4 = [2,3,4,5,6,8,7]
print(trojki(t4))