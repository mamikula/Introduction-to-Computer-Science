#Proszę napisać program, który wypełnia N-elementową tablicę t pseudolosowymi liczbami
#nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy długością najdłuższego
#znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy, a długością najdłuższego ciągu
#arytmetycznego o ujemnej różnicy, przy założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych
#indeksach.

N = 10

def podciag(t):
    lm = 1
    lp = 1
    maxlp = 1
    maxlm = 1
    for i in range(2, N):
        if t[i - 2] - t[i - 1] == t[i - 1] - t[i] and t[i - 2] - t[i - 1] > 0:
            lm += 1
        else:
            if maxlm < lm:
                maxlm = lm
            lm = 1
        if t[i - 2] - t[i - 1] == t[i - 1] - t[i] and t[i - 2] - t[i - 1] < 0:
            lp += 1
        else:
            if maxlp < lp:
                maxlp = lp
            lp = 1

        if lp > maxlp:
            maxlp = lp
        if lm > maxlm:
            maxlm = lm

    return(maxlp - maxlm)

def main():
    t = [1, 2, 3, 4, 5, 4, 3, 0, 1, 1]
    print(podciag(t))

main()