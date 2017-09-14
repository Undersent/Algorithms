global comparisons

def lcs(a, b):
    global comparisons
    comparisons=0
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)] #wypelnianie stanow poczatkowych
    # dajemy wszystko na 0
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                comparisons += 1
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                comparisons += 1
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1]) #tworzymy nasza macierz
    # czytamy z naszej macierzy
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:  #jezeli [0][0] to koniec odtwarzania
        if lengths[x][y] == lengths[x-1][y]:  #jezeli gora lub lewo maja taka sama wartosc to przechodzimy do niej
            x -= 1
            comparisons += 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
            comparisons += 1
        else:
            result = a[x-1] + result  #jezeli nie to dopisujemy literke i idziemy po skosie w gore w lewo
            x -= 1
            y -= 1
            comparisons += 1
    return result

import string
import random
import pylab
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
import math



n=100
results=[]
for i in range(1000,100000,100):
    print("lecimy ",i," runde")
    comparisons = 0
    word = id_generator(size=int(math.sqrt(i)))
    word2 = id_generator(size=int(math.sqrt(i)))
    lcs(word,word2)
    results.append(comparisons)

pylab.plot(results)
pylab.show()

