# Problem 8 Hetmanów (treść oczywista)

def moze(wsp, w, k):
    for i in range(len(wsp)):
        pozx = abs(i - w)
        pozy = abs(wsp[i] - k)
        if wsp[i] == k or pozx == pozy:
            return False
    return True


def hetmany(wsp, n):
    if n == 0:
        return False

    da = False

    if len(wsp) == n:
        print(wsp)
        return True

    else:
        for k in range(n):
            if moze(wsp, len(wsp), k):
                wsp.append(k)
                if hetmany(wsp, n):
                    da = True
                wsp.pop()
    return da


def ustawHetmana(dane, n):
  ile = 0
  if (len(dane) == n):
    return 1
  else:
    for k in range(0, n):
      if (moze(dane, len(dane), k)):
        dane.append(k)
        ile += ustawHetmana(dane, n)
        dane.pop()
  return ile




def main():
    wsp = [] # nr kolumny na które ustawiony jest hetman, wiersz to indeks

    print(hetmany(wsp, 9))
    print(ustawHetmana(wsp, 9))
main()





