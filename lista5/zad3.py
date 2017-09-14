global comparisons

def editDistance(word1,word2):
    len_1=len(word1)
    len_2=len(word2)
    global comparisons
    comparisons=0

    x =[[0]*(len_2+1) for _ in range(len_1+1)]#moja macierz

    for i in range(0,len_1+1): #podstawowa inicjalizacja
        x[i][0]=i

    for j in range(0,len_2+1): #podstawowa inicjalizacja
        x[0][j]=j

    for i in range (1,len_1+1):
        for j in range(1,len_2+1):
            comparisons+=1

            if word1[i-1]==word2[j-1]:    #jezeli taka sama litera to po skosie przepisujemy
                x[i][j] = x[i-1][j-1]
            else :  #jezeli nie to najmniejsza wartosc z trzech sasiednich plus jeden
                x[i][j]= min(x[i][j-1],x[i-1][j],x[i-1][j-1])+1

    return x[i][j]

import string
import random
import pylab
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
import math

"""n=100
results=[]
loop = 5
for i in range(100,500,10):
    print("lecimy ", i, " runde")
    comparisonsFull=0
    for j in range(loop):
        comparisons=0
        word = id_generator(size=i)
        word2 = id_generator(size=i)
        editDistance(word,word2)
        comparisonsFull += comparisons
    results.append(comparisonsFull/loop)

pylab.plot(results)
pylab.show()"""

import re
from collections import Counter

def wordsF(text): return re.findall(r'\w+', text.lower())

words = Counter(wordsF(open('words.txt').read()))

def P(word, N=sum(words.values())): return words[word] / N

#print(len(words)) #32195
#print(sum(words.values())) #1115527
input = input()
listOfDistances =[10,10,10]
listOfWords = ["","",""]
maxWords = 3

for word in words:
    distance = editDistance(input,word)
    for i in range(0,maxWords):
        if listOfDistances[i]>distance != 0:
            listOfWords[i]= word
            listOfDistances[i] = distance
            break

print(listOfWords)
print(listOfDistances)