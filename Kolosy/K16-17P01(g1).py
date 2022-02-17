#Dane są dwa ciągi określone następująco:
#a1 = 1   an = an−1 + bn/3
#b1 = 2   bn = bn−1 + an−1
#Proszę napisać program, który wczytuje liczbę naturalną k i odnajduje wyraz należący do
#jednego z ciągów o wartości najbliższej k. Program powinien wypisać numer znalezionego
#wyrazu i ciąg z którego on pochodzi. Jeżeli więcej niż jeden wyraz jest jednakowo odległy
#od k, należy wybrać ten o mniejszym numerze.

def ciagi(k):
    an = 1
    bn = 2
    mini = 999999999
    lan = 0
    lab = 0
    minl = 0

    while an < k or bn < k:

        an = an + bn//3
        bn = bn + (an - bn//3)
        lab += 1
        lan += 1

        if mini > k - an and k - an > 0:
            mini = k - an
            minl = lan

        if mini > k - bn and k - bn > 0:
            mini = k - bn
            minl = lab
            
        print(an, lan, bn, lab, minl)

    return mini

print(ciagi(10))