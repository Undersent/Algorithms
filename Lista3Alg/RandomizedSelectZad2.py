from random import randrange

import pylab

from Lista2 import Generator

global comparisonsRandSelect
global results


class Alg:
    def __init__(self, repeat=30, maxElems=3000, step=100, maxInt=100000):
        self.maxInt = maxInt
        self.repeat = repeat
        self.maxElems = maxElems
        self.step = step

    def drawComparisonsSorted(self):
        global results
        results = []

        global comparisonsRandSelect
        comparisonsRandSelect=0
        for k in range(100,self.maxElems, self.step):
            number = numpy.random.randint(0, k)
            comparedTimes = 0
            print(k)
            for i in range(0, self.repeat):
                a = Generator.generateRandomNumbers(k, 0, self.maxInt);
                a.sort(reverse=True)
                #a = random.sample(range(0, self.maxInt), k)
                RSelect(a, number)
                comparedTimes+= comparisonsRandSelect
                comparisonsRandSelect=0
        #print (comparedTimes/self.repeat)
            results.append(comparedTimes/self.repeat)
        return results

import numpy
def partition(x, pivot_index=0):
    i = 0
    global comparisonsRandSelect

    #print("tablica ", x)
    #print("pivot ", pivot_index)
    if pivot_index != 0: x[0], x[pivot_index] = x[pivot_index], x[0]
    for j in range(len(x) - 1):
        if x[j + 1] < x[0]:
            x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
            comparisonsRandSelect+=1
            i += 1

    x[0], x[i] = x[i], x[0]
    return x, i


def RSelect(x, k):
    if len(x) == 1:
        return x[0]
    else:
        xpart = partition(x, randrange(len(x)))
        #print (xpart)
        x = xpart[0]  # partitioned array
        j = xpart[1]  # pivot index
        if j == k:
            return x[j]
        elif j > k:
            return RSelect(x[:j], k)
        else:
            k = k - j - 1
            return RSelect(x[(j + 1):], k)


Testownik = Alg()
Testownik.drawComparisonsSorted()
pylab.plot(results)
pylab.show()
