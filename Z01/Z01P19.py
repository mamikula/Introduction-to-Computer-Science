def e_generator(n):
    e = 0
    f = 1   # silnia
    for i in range(1, n + 1):
        e = e + 1 / f
        print(f)
        f = f * i

    return e


print(e_generator(10))