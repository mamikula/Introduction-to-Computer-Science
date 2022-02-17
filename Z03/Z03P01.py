#Napisać program zamieniający liczbę naturalną z systemu 10 na
#podstawę 2-16

def zamiana(a, s):
    if a > 0:
        zamiana(a // s, s)
        if a % s > 9:
            if a % s == 10:
                print('A')
            if a % s == 11:
                print('B')
            if a % s == 12:
                print('C')
            if a % s == 13:
                print('D')
            if a % s == 14:
                print('E')
            if a % s == 15:
                print('F')
        else:
            print(a % s)


def main():
    a = 7546
    s = 12
    zamiana(a, s)

main()