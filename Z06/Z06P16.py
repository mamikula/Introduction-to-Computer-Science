#Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą liczbę samogłosek
#oraz sumy kodów
#ascii liter z których są zbudowane są identyczne, na przykład ula → 117, 108, 97
#oraz exe → 101, 120, 101. Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe zbudowanie wyrazu
#z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja powinna wypisać
#znaleziony wyraz.

def letters(word):
    val = 0
    counter = 0
    vowels = ['a', 'e', 'y', 'u', 'i', 'o'] #samogłoski
    for i in range(len(word)):
        val += ord(word[i])
        counter += word[i] in vowels #ciekawy sposob zliczania samoglosek
    return (counter, val)


def words(w1, w2):
    tmp1 = letters(w1)
    gens = rekur('', 0, w2)
    for i in range(len(gens)):
        new = gens[i]
        if letters(new) == tmp1:
            print(w1, new)


def rekur(new, id, w2):

    if id == len(w2):
        #print(new)
        return [new]  #jedno elementowa tablica, zawierajaca wszystkie wygenerowane ciagi

    x = rekur(new + w2[id], id + 1, w2)
    y = rekur(new, id + 1, w2)

    return (x + y) 




#print(rekur('', 0, 'ula'))
#print(rekur('', 0, 'aidexe'))

words('ula', 'aeidxe')
#rekur('', 0, 'ula')

