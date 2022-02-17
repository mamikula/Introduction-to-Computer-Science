#Dwie listy zawieraja niepowtarzajace sie (w obrebie listy) liczby naturalne.
#W obu listach liczby sa posortowane rosnaco. Prosze napisac funkcje usuwajaca z kazdej listy liczby wystepujace w drugiej. Do funkcji
#nalezy przekaza¢ wskazania na obie listy, funkcja powinna zwrócic laczna liste usunietych elementów.


def newlist(t1, t2):
    i = 0
    j = 0
    newtab=[]
    while i < len(t1) and j < len(t2):

        if t1[i] == t2[j]:
            newtab.append(t1[i])
            t1[i] = -1
            t2[j] = -1
            j += 1
            i += 1

        elif t1[i] > t2[j]:
            j += 1

        elif t1[i] < t2[j]:
            i += 1


    #print(t1, t2)
    return(newtab)

t1 = [1, 3, 5, 7]
t2 = [1, 2, 3, 4, 5]

print(newlist(t1, t2))