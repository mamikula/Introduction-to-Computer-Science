#Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić
#wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
#wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
#75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
#zadanych liczb.


def pierwsza(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def gen(a, b, nowa, mn):
    if a > 0 and b > 0:
        gen(a // 10, b, nowa + (a % 10) * mn, mn * 10)
        gen(a, b // 10, nowa + (b % 10) * mn, mn * 10)

    elif a > 0 and b == 0:
        gen(a // 10, b, nowa + (a % 10) * mn, mn * 10)

    elif b > 0 and a == 0:
        gen(a, b // 10, nowa + (b % 10) * mn, mn * 10)

    elif a == 0 and b == 0:
        if pierwsza(nowa):
            print(nowa)

gen(16, 381, 0, 1)