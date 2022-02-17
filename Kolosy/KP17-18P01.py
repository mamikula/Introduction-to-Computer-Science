#Dana jest tablica int t[N] wypeªniona liczbami caªkowitymi. Prosz¦ napisa¢ funkcj¦, która sprawdza, czy
#mo»liwe jest "poci¦cie" tablicy na co najmniej 2 kawaki o jednakowych sumach elementów. Do funkcji nale»y
#przekaza¢ tablic¦, funkcja powinna zwróci¢ najwi¦ksz¡ liczb¦ kawaªków, na któr¡ mo»na poci¡¢ tablic¦, lub
#warto±¢ 0, je±li takie poci¦cie nie jest mo»liwe. Na przykªad: dla tablicy [1,2,3,1,5,2,2,2,6] odpowiedzi¡
#powinno by¢ 4, bo [1,2,3|1,5|2,2,2|6].


from random import randint

def kawaleczki(t):
    kaw = 1
    gsum = 0
    best = 0
    for i in range(0, len(t) - 1):
        gsum += t[i] #suma głowna/ suma pierwszego kawalka z ktora nastepne beda porownywane
        sumre = 0 #suma nastepnych kawalkow

        for j in range(i + 1, len(t)):
            sumre += t[j]

            if j == len(t) - 1 and sumre != gsum:
                kaw = 1

            if sumre == gsum: #jezeli znajdzie kolejny kawalek o szukanej sumie, zwieksza ilosc kawalkow i liczy dalej
                sumre = 0
                kaw += 1

        if kaw > best:
            best = kaw
            
        kaw = 1

    if best >= 2:
        print(best)
        return True

    return False

#t = [1,2,3,1,5,2,2,2,6,6]
#t = [0,0,0,0,0]
#t = [-1, 2, -3, 4, 3, -6,4, 2]
print(kawaleczki(t))







