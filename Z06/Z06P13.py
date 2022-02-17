#Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej
# na sumę składników. Na przykład dla liczby 4 są to:
# 1+3, 1+1+2, 1+1+1+1, 2+2

def skladniki(dana, ostatni,  s):

    if dana == 0:
        print(s)

    for i in range(ostatni, dana + 1):
        skladniki(dana - i, i, s + str(i))

skladniki(5, 1, '')



