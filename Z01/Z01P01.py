#Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona

def fib():
    a = 0
    b = 1
    while a <= 1000000:
        print(a)
        b = b + a
        a = b - a

fib()