# Napisać program sprawdzający czy zadana liczba jest pierwsza.

def pierwsza():
    dana = 14
    for i in range(2, dana):
        if dana % i == 0:
            print("Nie jest")
            return False
    print("Jest")
    return True

pierwsza()


