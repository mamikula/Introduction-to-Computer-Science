# Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca
# sumę iloczynów elementów wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby.
# Można założyć, że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym
# etapie funkcja powinna wpisać podzielniki do tablicy pomocniczej.
# Przykład: 60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71

#z apendem troche lepiej dziala, zeby wersa z append działała, należy zakomentować 1


def divisors(primes, number): #podzielniki
    for i in range(2, number):
        if number % i == 0:
            while number % i == 0:
                number //= i

            primes.append(i) #odkomentowac tutaj
            #primes[i] = i   #1
    print(primes)
    return primes



def fun(primes, id, new):
    sumend = 0
    if new == 0: #1
        return 0 #1

    if id == len(primes):
        print(new)

        if new == 1:
            return 0
        else:
            return new

    else:
        sumend += fun(primes, id + 1, new * primes[id])
        sumend += fun(primes, id + 1, new)

    return sumend






def sum_product(number):
    primes = [] #* 20 #1 dac pusty nawias
    #print(primes)
    primes = divisors(primes, number)
    print(fun(primes, 0, 1))

sum_product(10)
